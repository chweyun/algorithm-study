import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    now = input().strip()
    stack = []

    for i in now:
        if i == '(':
            stack.append(i)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)

    print('NO' if len(stack) else 'YES')


