import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
arr = [[c == 'T' for c in input().strip()] for _ in range(R)]
arr[R-1][0] = True
dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)
result = 0

# dfs + back tracking
def dfs(now_x, now_y, dist):
    global result

    if now_x == 0 and now_y == C-1 and dist == K:
        result += 1
        return

    for i in range(4):
        nxt_x, nxt_y = now_x+dx[i], now_y+dy[i]
        if 0<=nxt_x<R and 0<=nxt_y<C and not arr[nxt_x][nxt_y]:
            arr[nxt_x][nxt_y] = True
            dfs(nxt_x, nxt_y, dist+1)
            arr[nxt_x][nxt_y] = False

dfs(R-1, 0, 1)
print(result)