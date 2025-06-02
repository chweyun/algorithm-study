import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M = int(input()), int(input())
dic = defaultdict(list)
result = [-1 for _ in range(N+1)]

# 초기화 (첫번째 원소: 더 작은 값, 두번째 원소: 더 큰 값)
for i in range(1, N+1):
    dic[i] = [[], []]

for i in range(M):
    a, b = map(int, input().split())
    dic[b][0].append(a)
    dic[a][1].append(b)

for i in range(1, N+1):
    for j in range(2):
        dic[i][j] = set(dic[i][j])

def dfs(v):
    global count
    visited[v] = True
    deq.append((v, [0, 1]))

    while deq:
        cur, order = deq.pop()
        for odr in order:
            for nxt in dic[cur][odr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    deq.append((nxt, [odr]))


for i in range(1, N+1):
    visited, count, deq = [False] * (N+1), 0, deque()
    visited[0] = True
    dfs(i)
    print(visited.count(False))
