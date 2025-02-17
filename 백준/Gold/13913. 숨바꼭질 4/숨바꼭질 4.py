from collections import deque

N, K = map(int, input().split())
visited = [float('inf') for _ in range(200001)]
visited[N] = 0
prev = [-1 for _ in range(200001)]
deq = deque([(N, 0)])
count = 0

while deq:
    now, sec = deq.popleft()

    if now == K:
        print(sec)
        break

    for i in [now+1, now-1, now*2]:
        if 0<=i<200000 and visited[i]>sec+1:
            visited[i] = visited[now] + 1
            prev[i] = now
            deq.append((i, sec+1))

result = []
cur = K
while cur!=-1:
    result.append(cur)
    cur = prev[cur]

print(' '.join(map(str, result[::-1])))