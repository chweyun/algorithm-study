import sys
from collections import deque
input = sys.stdin.readline

h, w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
dx, dy = (-1, 0, 1, -1, 1, -1, 0, 1), (-1, -1, -1, 0, 0, 1, 1, 1)
max_dist = 0

def bfs(y, x):
    visited = [[False]*w for _ in range(h)]
    visited[y][x] = True
    deq = deque([(x, y, 0)])

    while deq:
        now_x, now_y, now_count = deq.popleft()
        if arr[now_y][now_x]:
            return now_count

        for i in range(8):
            nxt_x, nxt_y = now_x+dx[i], now_y+dy[i]
            if 0<=nxt_x<w and 0<=nxt_y<h and not visited[nxt_y][nxt_x]:
                visited[nxt_y][nxt_x] = True
                deq.append((nxt_x, nxt_y, now_count+1))
    return 0

for i in range(h):
    for j in range(w):
        dist = bfs(i, j)
        max_dist = max(max_dist, dist)

print(max_dist)