import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = [list(map(int, input().strip())) for _ in range(n)]
dp = [[1]*m for _ in range(n)]

def check_rect(pivot_x, pivot_y):
    a, b, c = dp[pivot_y][pivot_x+1], dp[pivot_y+1][pivot_x+1], dp[pivot_y+1][pivot_x]
    return min(a, b, c)

result = 1
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if num[i][j]==0 or i==n-1 or j==m-1:
            dp[i][j] = num[i][j]
        else:
            dp[i][j] = check_rect(j, i) + 1

print(max(map(max, dp))**2)