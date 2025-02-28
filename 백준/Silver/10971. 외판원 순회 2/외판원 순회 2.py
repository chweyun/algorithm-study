import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
result = float("INF")

def dfs(now, total, count):
    global result
    visited[now] = True

    if count == N-1 and W[now][0] != 0:
        result = min(result, total+W[now][0])
        visited[now] = False
        return

    for i in range(N):
        if not visited[i] and W[now][i] != 0:
            dfs(i, total+W[now][i], count+1)
            visited[i] = False

dfs(0, 0, 0)
print(result)