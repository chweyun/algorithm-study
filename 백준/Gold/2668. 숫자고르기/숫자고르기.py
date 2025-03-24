import sys
input = sys.stdin.readline

n = int(input())
arr, result = [[] for _ in range(n+1)], []
for i in range(n):
    arr[int(input())].append(i+1)

def dfs(start_idx, now_arr):
    if start_idx == now_arr[-1] and visited[now_arr[-1]]:
        result.append(start_idx)

    for v in arr[now_arr[-1]]:
        if not visited[v]:
            visited[v] = True
            nxt = now_arr + [v]
            dfs(start_idx, nxt)


for j in range(1, n+1):
    if len(arr[j]) > 0:
        visited = [False] * (n+1)
        dfs(j, [j])

result.sort()
print(len(result))
for x in result:
    print(x)