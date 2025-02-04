from collections import deque

N, K = map(int, input().split())
visited = [False]*100001

def bfs(v):
    deq = deque([(v,0)])
    visited[v] = True

    while deq:
        node, count = deq.popleft()

        if node == K:
            print(count)
            break

        for nxt in [node-1, node+1, node*2]:
            if 0<=nxt<=100000 and not visited[nxt]:
                visited[nxt] = True
                deq.append((nxt, count+1))

bfs(N)