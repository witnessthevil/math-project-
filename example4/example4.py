from collections import defaultdict, OrderedDict
from itertools import combinations,chain
import json 

ele = set(range(1,10))
possible_allocation = [i for i in combinations(list(range(1,10)),3)]

preference = {
    "A" : [1,2,3,4,5,6,7,8,9],
    "B" : [3,4,2,6,8,7,1,5,9],
    "C" : [5,8,2,7,9,1,3,4,6]
}
def finding_least_ranking(resource:dict) -> int:
    player_least_index = []
    for player in list(resource.keys())[:len(preference)]:
        P_preference = preference[player]
        highest_idx = max(list(map(lambda x: P_preference.index(x) + 1 ,resource[player])))
        player_least_index.append(highest_idx)
    return max(player_least_index)

def finding_Borda_score(resource:dict) -> int:
    player_borda_score = []
    for player in list(resource.keys())[:len(preference)]:
        P_preference = preference[player]
        idx_score_list = list(map(lambda x: 9 -  P_preference.index(x),resource[player]))
        player_borda_score.append(sum(idx_score_list))
    return min(player_borda_score)

def all_allocation(tuple:tuple):
    A_get = set(tuple)
    others = ele - A_get
    allo_for_B_and_C = [set(j) for j in combinations(others,3)]
    allo = list(map(lambda x: {"A":A_get,"B":x,"C":others -x},allo_for_B_and_C))
    return allo

all_allo = list(chain.from_iterable([all_allocation(i) for i in possible_allocation]))

# len(all_allo) = 1680 = 9C3 * 6C3

stage_list = []

for i in all_allo:
    resource_list = {}
    resource_list.setdefault('A',list(i["A"]))
    resource_list.setdefault('B',list(i["B"]))
    resource_list.setdefault('C',list(i["C"]))
    resource_list.setdefault('h_l_ranking',0)
    resource_list.setdefault('lowest_Borda_score',0)
    resource_list['h_l_ranking'] += finding_least_ranking(resource_list)
    resource_list['lowest_Borda_score'] += finding_Borda_score(resource_list)
    stage_list.append(resource_list)

highest_least_ranking = sorted(stage_list,key=lambda x: x['h_l_ranking'],reverse=False)
Borda_ranking = sorted(stage_list,key=lambda x: x['lowest_Borda_score'],reverse=True)

with open('./example4/example4_result(least_ranking).json','a') as f:
    for rank_allocation in highest_least_ranking:
        f.write(json.dumps(rank_allocation) + "\n")

with open('./example4/example4_result(Borda_Score).json','a') as g:
    for j in Borda_ranking:
        g.write(json.dumps(j) + "\n")
    
        