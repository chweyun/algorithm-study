import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

def bfs(k, start):
    visited = [False] * (N + 1)
    visited[start] = True
    deq = deque([start])
    count = 0

    while deq:
        now = deq.popleft()
        for nxt, cost in graph[now]:
            if not visited[nxt] and cost >= k:
                visited[nxt] = True
                count += 1
                deq.append(nxt)

    return count

for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(k, v))