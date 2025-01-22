N = int(input())

if N == 1:
    print(1)
else:
    dp = [0 for _ in range(N+1)]
    dp[1], dp[2] = 1, 2
    
    for i in range(3, N+1):
        dp[i] = (dp[i-2] + dp[i-1])%15746
    
    print(dp[N])