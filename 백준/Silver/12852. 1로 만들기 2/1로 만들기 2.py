n = int(input())
dp = [[99999, []] for _ in range(n + 1)]
dp[1][0] = 0

for i in range(1, n+1):
    v = dp[i][0]

    if i+1 <= n and v+1 < dp[i+1][0]:
        dp[i+1][0] = v+1
        dp[i+1][1] = dp[i][1].copy() + [i]
    if i*2 <= n and v+1 < dp[i*2][0]:
        dp[i*2][0] = v+1
        dp[i*2][1] = dp[i][1].copy() + [i]
    if i*3 <= n and v+1 < dp[i*3][0]:
        dp[i*3][0] = v+1
        dp[i*3][1] = dp[i][1].copy() + [i]

dp[n][1] = dp[n][1] + [n]

print(dp[n][0])
print(' '.join(map(str, reversed(dp[n][1]))))