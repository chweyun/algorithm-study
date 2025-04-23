import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kit = list(map(int, input().split()))
visited = [False] * n
result = 0

def dfs(now_w, day):
    global result

    if day == n:
        result += 1
        return

    for i in range(n):
        if not visited[i] and now_w - k + kit[i] >= 500 :
            visited[i] = True
            dfs(now_w - k + kit[i], day+1)
            visited[i] = False

for idx in range(n):
    visited[idx] = True
    dfs(500, 1)
    visited[idx] = False

print(result)