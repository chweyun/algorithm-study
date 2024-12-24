from itertools import combinations, product, repeat
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    dic = {}

    for a_combi in combinations(range(n), n//2):
        b_combi = [x for x in range(n) if x not in a_combi]

        a, b = [], []
        for sum_ in product(range(6), repeat=n//2):
            a.append(sum(dice[i][j] for i, j in zip(a_combi, sum_)))
            b.append(sum(dice[i][j] for i, j in zip(b_combi, sum_)))
        b.sort()

        win = sum(bisect_left(b, num) for num in a)
        dic[win] = list(a_combi)

    max_keys = max(dic.keys())

    return [x+1 for x in dic[max_keys]]