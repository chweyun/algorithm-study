from collections import deque

N, K = map(int, input().split())
deq = deque([N])
visited = [-1 for _ in range(200001)]
visited[N] = 0
min_sec = float("inf")

while deq:
    now_pivot = deq.popleft()

    if visited[now_pivot] >= min_sec:
        break

    if now_pivot == K:
        min_sec = min(min_sec, visited[now_pivot])
        continue

    if 0<=now_pivot-1<=200000 and (visited[now_pivot-1] == -1 or visited[now_pivot-1] > visited[now_pivot]+1):
        deq.append(now_pivot-1)
        visited[now_pivot-1] = visited[now_pivot]+1
    if 0<=now_pivot+1<=200000 and (visited[now_pivot+1] == -1 or visited[now_pivot+1] > visited[now_pivot]+1):
        deq.append(now_pivot+1)
        visited[now_pivot+1] = visited[now_pivot]+1
    if 0<=now_pivot*2<=200000 and (visited[now_pivot*2] == -1 or visited[now_pivot*2] > visited[now_pivot]):
        deq.append(now_pivot*2)
        visited[now_pivot*2] = visited[now_pivot]

print(min_sec)
