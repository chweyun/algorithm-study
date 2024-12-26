def solution(n, tops):
    # dp1: 눕힌 마름모로 끝낸 경우, dp2: 눕힌 마름모를 제외한 타일로 끝낸 경우
    MOD = 10007
    dp1, dp2 = [0 for _ in range(n)], [0 for _ in range(n)]
    dp1[0] = 1
    dp2[0] = 2 + tops[0]

    for i in range(1, n):
        dp1[i] = dp1[i-1] + dp2[i-1]
        dp2[i] = dp1[i-1]*(tops[i]+1) + dp2[i-1]*(tops[i]+2)


        dp1[i] = (dp1[i-1] + dp2[i-1]) % MOD
        dp2[i] = (dp1[i-1] * (tops[i] + 1) + dp2[i-1] * (tops[i] + 2)) % MOD

    return (dp1[n-1] + dp2[n-1]) % MOD