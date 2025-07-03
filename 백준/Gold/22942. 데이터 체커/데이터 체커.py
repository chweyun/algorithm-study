import sys
input = sys.stdin.readline

N = int(input())
arr, circle, stack = [], [], []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

for i, v in enumerate(arr):
    circle.append((v[0]-v[1], i, True))
    circle.append((v[0]+v[1], i, False))
circle.sort(key=lambda x: x[0])

for j in circle:
    x, idx, is_left = j
    if is_left:
        stack.append(idx)
    elif stack[-1] == idx:
        stack.pop()
    else:
        break

if stack:
    print("NO")
else:
    print("YES")