import sys
input = sys.stdin.readline

vowels = ('a', 'e', 'i', 'o', 'u')

L, C = map(int, input().split())
chars = list(map(str, input().split()))
chars.sort()
visited = [False for _ in range(C)]

# a, c, i, s, t, w
def dfs(start_idx, cons_num, vowels_num, result):
    if len(result) == L and cons_num >=2 and vowels_num>=1:
        return print("".join(result))

    for i in range(start_idx+1, C):
        if not visited[i]:
            result.append(chars[i])
            visited[i] = True
            dfs(i, cons_num, vowels_num+1, result) if chars[i] in vowels else dfs(i, cons_num+1, vowels_num, result)
            result.pop()
            visited[i] = False


for i in range(C-L+1):
    visited[i] = True
    if chars[i] in vowels:
        dfs(i, 0, 1, [chars[i]])
    else:
        dfs(i, 1, 0, [chars[i]])