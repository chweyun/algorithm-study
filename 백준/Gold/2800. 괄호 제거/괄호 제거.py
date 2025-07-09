import sys
input = sys.stdin.readline
from itertools import combinations

inp = list(input().strip())
bracket_tmp, bracket = [], []
answer = set()

for i in range(len(inp)):
    if inp[i] == "(":
        bracket_tmp.append(i)
    elif inp[i] == ")":
        bracket.append((bracket_tmp.pop(), i))

for i in range(len(bracket)):
    for j in combinations(bracket, i+1):
        tmp = inp.copy()
        for k in j:
            tmp[k[0]], tmp[k[1]] = "", ""
        answer.add("".join(tmp))

for i in sorted(list(answer)):
    print(i)