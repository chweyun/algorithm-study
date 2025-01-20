# dp[n][d] = 길이가 n, 마지막 숫자가 d인 계단 수 갯수

dp = [[0] * 10 for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, 101):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i-1][j-1]
        if j < 9:
            dp[i][j] += dp[i-1][j+1]

result = 0
n = int(input())
for i in range(10):
    result += dp[n][i]

print(result % 1000000000)