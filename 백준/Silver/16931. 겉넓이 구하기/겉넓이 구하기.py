import sys
input = sys.stdin.readline
n, m = map(int, input().split())
square = [list(map(int, input().split())) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        if i==0:
            result += square[i][j]
        elif square[i][j] > square[i-1][j]:
            result += (square[i][j]-square[i-1][j])

for i in range(m):
    for j in range(n):
        if i==0:
            result += square[j][i]
        elif square[j][i] > square[j][i-1]:
            result += (square[j][i]-square[j][i-1])

result *=2
result += n*m*2
print(result)