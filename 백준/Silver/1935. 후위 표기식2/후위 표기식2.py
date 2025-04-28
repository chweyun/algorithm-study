import sys
input = sys.stdin.readline

N = int(input())
aft = list(input().strip())
num = [int(input()) for _ in range(N)]

for i in range(len(aft)-1, -1, -1):
    if aft[i] not in ('+', '-', '/', '*'):
        aft[i] = num[ord(aft[i]) - 65]

stack, i = [], 0
while i < len(aft):
    if aft[i] not in ('+', '-', '/', '*'):
        stack.append(aft[i])
    else:
        b, a = stack.pop(), stack.pop()
        if aft[i] == '+':
            stack.append(a+b)
        elif aft[i] == '-':
            stack.append(a-b)
        elif aft[i] == '*':
            stack.append(a*b)
        else:
            stack.append(a/b)
    i += 1

print(f"{stack[0]:.2f}")