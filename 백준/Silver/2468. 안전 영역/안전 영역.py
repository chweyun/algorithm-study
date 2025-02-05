import sys

sys.setrecursionlimit(10**6)
N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
max_safe_count = 1
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def is_valid(now_x, now_y, rain):
    if 0<=now_x<N and 0<=now_y<N and not visited[now_x][now_y] and adj[now_x][now_y]>rain:
        return True
    return False

def dfs(now, rain, visited):
    x, y = now
    visited[x][y] = True

    for nxt in range(4):
        if is_valid(x+dx[nxt], y+dy[nxt], rain):
            dfs((x+dx[nxt], y+dy[nxt]), rain, visited)

for rain in range(1, 100):
    visited = [[False]*N for _ in range(N)]
    count = 0
    for x in range(N):
        for y in range(N):
            if not visited[x][y] and adj[x][y] > rain:
                dfs((x, y), rain, visited)
                count += 1
    max_safe_count = max(count, max_safe_count)

print(max_safe_count)
