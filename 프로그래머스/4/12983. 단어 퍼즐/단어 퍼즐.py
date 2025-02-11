def solution(strs, t):
    dp = [0 for _ in range(len(t)+1)]
    strs = set(strs)

    for i in range(1, len(dp)):
        dp[i] = float('inf')
        if i-4 > 0:
            k = i-4
        else:
            k = 1

        for j in range(k, i+1):
            if t[j-1:i] in strs:
                dp[i] = min(dp[i], dp[i-len(t[j-1:i])]+1)

    if dp[-1] == float('inf'):
        return -1
    else:
        return dp[-1]