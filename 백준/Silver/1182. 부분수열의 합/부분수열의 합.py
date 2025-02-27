import sys
from collections import deque
input = sys.stdin.readline
n, s = map(int, input().split())
num = list(map(int, input().split()))
result = 0
visited = [False for _ in range(n)]

def bfs(start):
    global result
    deq = deque([(num[start], start)])
    while deq:
        total, idx = deq.popleft()

        if total == s:
            result += 1

        for i in range(idx+1, n):
            deq.append((total+num[i], i))

for i in range(n):
    bfs(i)

print(result)