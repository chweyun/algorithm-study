from collections import deque

N, M = map(int, input().split())
adj = [list(input().strip()) for _ in range(N)]
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
visited = [[False]*M for _ in range(N)]

def is_valid(next_x, next_y):
    if 0<=next_x<N and 0<=next_y<M and adj[next_x][next_y] == '1' and not visited[next_x][next_y]:
        return True
    return False

def bfs():
    deq = deque([(0, 0)])
    visited[0][0] = True
    adj[0][0] = 1

    while deq:
        x, y = deq.popleft()
        for nxt in range(4):
            nx, ny = x+dx[nxt], y+dy[nxt]
            if is_valid(nx, ny):
                visited[nx][ny] = True
                deq.append((nx, ny))
                adj[nx][ny] = adj[x][y] + 1

bfs()
print(adj[N-1][M-1])