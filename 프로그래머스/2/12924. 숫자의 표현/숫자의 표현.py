def solution(n):
    dp = [0 for _ in range(n)]
    answer = 1

    for i in range(1, n):
        tmp = i
        while dp[i] < n:
            dp[i] += tmp
            tmp += 1
        if dp[i] == n:
            answer += 1

    return answer