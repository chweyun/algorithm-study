import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = list(map(int, input().split()))
result = deque()

for i in range(N):
    now, act = i+1, arr[N-i-1]

    if not result:
        result.append(now)
    else:
        if act == 1:
            result.appendleft(now)
        elif act == 2:
            result.insert(1, now)
        else:
            result.append(now)

print(*result)