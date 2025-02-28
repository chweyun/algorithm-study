import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    l = int(input())
    now = list(map(int, input().split()))
    next_x, next_y = map(int, input().split())
    dx = (-2, -2, -1, -1, 1, 1, 2, 2)
    dy = (-1, 1, -2, 2, -2, 2, -1, 1)
    visited = [[float("INF")]*l for _ in range(l)]

    def bfs(now_pivot):
        deq = deque([(now_pivot, 0)])

        while deq:
            popped = deq.popleft()
            now_x, now_y, total = popped[0][0], popped[0][1], popped[1]

            if now_x == next_x and now_y == next_y:
                print(total)
                break

            for i in range(8):
                if 0<=now_x+dx[i]<l and 0<=now_y+dy[i]<l and visited[now_x+dx[i]][now_y+dy[i]] > total+1:
                    visited[now_x+dx[i]][now_y+dy[i]] = total+1
                    deq.append(([now_x+dx[i], now_y+dy[i]], total+1))

    bfs(now)