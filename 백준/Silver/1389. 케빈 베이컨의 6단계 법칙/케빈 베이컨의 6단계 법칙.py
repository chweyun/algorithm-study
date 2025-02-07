from collections import deque

N, M = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(M)]
adj = [[] for _ in range(N+1)]

for i, j in friends:
    adj[i].append(j)
    adj[j].append(i)

def bfs(start):
    bacon = [99999]* (N+1)
    bacon[start] = 0
    deq = deque([start])

    while deq:
        now = deq.popleft()
        for nxt in adj[now]:
            if bacon[nxt] == 99999:
                deq.append(nxt)
                bacon[nxt] = bacon[now]+1
    return sum(bacon[1:])

result = []
for i in range(1, N+1):
    result.append((i, bfs(i)))

print(min(result, key=lambda x: (x[1], x[0]))[0])

