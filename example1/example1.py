from collections import defaultdict, OrderedDict
from itertools import combinations
import json 


ele = {1,2,3,4}
possible_allocation = [i for i in combinations([1,2,3,4],2)]
preference = {
    "A" : [1,2,3,4],
    "B" : [2,4,3,1],
}

def finding_least_ranking(resource:dict) -> int:
    player_least_index = []
    for player in list(resource.keys())[:2]:
        P_preference = preference[player]
        highest_idx = max(list(map(lambda x: P_preference.index(x) + 1 ,resource[player])))
        player_least_index.append(highest_idx)
    return max(player_least_index)

def finding_Borda_score(resource:dict) -> int:
    player_borda_score = []
    for player in list(resource.keys())[:len(preference)]:
        P_preference = preference[player]
        idx_score_list = list(map(lambda x: 4 -  P_preference.index(x),resource[player]))
        player_borda_score.append(sum(idx_score_list))
    return min(player_borda_score)

with open('./example1/example1_result.json','a') as f:
    for A_get in possible_allocation:
        resource_list = {}
        resource_list.setdefault('A',[])
        resource_list.setdefault('B',[])
        resource_list.setdefault('h_l_ranking',0)
        resource_list.setdefault('lowest_Borda_score',0)
        list_Aget = set(A_get)
        B_get = ele - list_Aget
        resource_list['A'] += list(A_get)
        resource_list['B'] += list(B_get)
        resource_list['h_l_ranking'] += finding_least_ranking(resource_list)
        resource_list['lowest_Borda_score'] += finding_Borda_score(resource_list)
        f.write(json.dumps(resource_list) + "\n")




