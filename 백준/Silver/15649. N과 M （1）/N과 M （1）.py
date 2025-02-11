n, m = map(int, input().split())
res = []

def dfs():
    if len(res) == m:
        print(' '.join(map(str, res)))
    else:
        for i in range(1, n+1):
            if i not in res:
                res.append(i)
                dfs()
                res.pop()

dfs()