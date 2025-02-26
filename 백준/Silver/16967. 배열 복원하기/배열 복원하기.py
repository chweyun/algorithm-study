import sys
input = sys.stdin.readline
h, w, x, y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h+x)]
result = [[float('inf')]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        result[i][j] = arr[i][j]

for i in range(x, h):
    for j in range(y, w):
        result[i][j] -= result[i-x][j-y]

for row in result:
    print(' '.join(map(str, row)))
