import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result, stack = [0] * n, []

for i in range(n):
    while stack:
        if stack[-1][1] > arr[i]:
            result[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()

    stack.append((i, arr[i]))

print(*result)