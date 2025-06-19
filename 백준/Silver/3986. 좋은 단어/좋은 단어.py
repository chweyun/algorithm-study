import sys
input = sys.stdin.readline

N = int(input())
result = 0

for _ in range(N):
    now = input().strip()
    stack = []

    for i in now:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()

    if not stack:
        result += 1

print(result)