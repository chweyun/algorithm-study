import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
li = [n+1 for n in range(N)]

for i in permutations(li, N):
    print(" ".join(map(str, i)))