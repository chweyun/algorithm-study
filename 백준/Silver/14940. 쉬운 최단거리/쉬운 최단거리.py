import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
result = [[-1 for _ in range(m)] for _ in range(n)]
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

def bfs(i, j):
    deq = deque([([i, j], 0)])
    while deq:
        now, count = deq.popleft()
        for i in range(4):
            nxt = [now[0]+dx[i], now[1]+dy[i]]
            if 0<=nxt[0]<n and 0<=nxt[1]<m and grid[nxt[0]][nxt[1]] == 1 and result[nxt[0]][nxt[1]] == -1:
                result[nxt[0]][nxt[1]] = count+1
                deq.append(([nxt[0], nxt[1]], count+1))


for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            result[i][j] = 0
            bfs(i, j)
        elif grid[i][j] == 0:
            result[i][j] = 0

for i in range(n):
    print(' '.join(map(str, result[i])))