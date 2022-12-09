from collections import defaultdict, OrderedDict
from itertools import combinations, product
import json 


ele = {1,2,3,4}
possible_allocation = [i for i in combinations([1,2,3,4],2)]
preference = {
    "A" : [1,2,3,4],
    "B" : [1,3,4,2],
}

def finding_ranking(resource:dict) -> list:
    player_least_index = []
    for player in list(resource.keys())[:2]:
        P_preference = preference[player]
        highest_idx = list(map(lambda x: P_preference.index(x) + 1 ,resource[player]))
        player_least_index.append(highest_idx)
    return player_least_index


with open('./example12/example12.json','a') as f:
    for A_get in possible_allocation:
        resource_list = {}
        resource_list.setdefault('A',[])
        resource_list.setdefault('B',[])
        resource_list.setdefault('A_ranking',[])
        resource_list.setdefault('B_ranking',[])
        list_Aget = set(A_get)
        B_get = ele - list_Aget
        resource_list['A'] += list(A_get)
        resource_list['B'] += list(B_get)
        A_rank, B_rank = finding_ranking(resource_list)[0],finding_ranking(resource_list)[1]
        resource_list['A_ranking'] += sorted(A_rank)
        resource_list['B_ranking'] += sorted(B_rank)
        comparison = [(a,b) for a,b in zip(resource_list['A_ranking'],resource_list['B_ranking'])]
        if all(list(map(lambda x: x[0] >= x[1],comparison))) == True:
            resource_list['envy-free'] = False
        if all(list(map(lambda x: x[0] <= x[1],comparison))) == True:
            resource_list['envy-free'] = False
        f.write(json.dumps(resource_list) + "\n")