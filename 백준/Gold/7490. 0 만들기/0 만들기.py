import sys
input = sys.stdin.readline

def calculate(arr):
    stack = []
    arr = arr.copy()

    while arr:
        now = arr.pop()
        if now == '+':
            continue
        elif now == '-':
            stack.append(stack.pop()*-1)
        elif now == ' ':
            target = stack.pop()
            nxt = int(arr.pop())
            stack.append(target + nxt*(10**len(str(target))))
        else:
            stack.append(int(now))
    return sum(stack) == 0

def dfs(now, arr):
    if now == n:
        if calculate(arr):
            print(''.join(map(str, arr)))
            return arr
    else:
        if arr[-1] not in ['+', '-', ' ']:
            dfs(now, arr + [' '])
            dfs(now, arr + ['+'])
            dfs(now, arr + ['-'])
        else:
            dfs(now+1, arr + [str(now+1)])

for _ in range(int(input())):
    n = int(input())
    dfs(1, ['1'])
    print()