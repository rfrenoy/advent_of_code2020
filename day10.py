import copy
import numpy as np


def read_file(buff):
    return [int(x) for x in buff.readlines()]


def rating_differences(adapter_ratings):
    return [adapter_ratings[i+1]-rating for i, rating in enumerate(adapter_ratings[:-1])]

def solve1(adapter_ratings):
    differences = rating_differences(adapter_ratings)
    return differences.count(1) * differences.count(3)

memory = {}
def solve2(adapter_ratings):
    h = hash(tuple(adapter_ratings))
    if h in memory:
        return memory[h]
    if len(adapter_ratings) <= 2:
        return 1
    differences = rating_differences(adapter_ratings[:4])
    try:
        reduce_idx = min(np.argwhere(np.array(differences) < 3).reshape(-1))
    except:
        reduce_idx = 0
    if reduce_idx > 0:
        return solve2(adapter_ratings[reduce_idx:])
    if differences[0] > 3:
        return 0
    cum_differences = np.cumsum(differences)
    idxs = np.argwhere(cum_differences <= 3).reshape(-1)
    res = 0
    for idx in idxs:
        tmp = solve2(adapter_ratings[idx+1:])
        memory[hash(tuple(adapter_ratings[idx+1:]))] = tmp
        res += tmp
    return res

if __name__ == '__main__':
    CHARGING_OUTLET_RATING = 0
    ACCEPTED_DIFFERENCES = [1, 2, 3]
    with open('data/day10.txt', 'r') as in_f:
        adapter_ratings = read_file(in_f)
    device_built_in_adapter_rating = max(adapter_ratings) + 3
    adapter_ratings = adapter_ratings + [CHARGING_OUTLET_RATING, device_built_in_adapter_rating]
    list.sort(adapter_ratings)
    print(solve1(adapter_ratings))
    print(solve2(adapter_ratings))
