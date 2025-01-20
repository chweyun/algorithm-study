n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

floor = len(dp)-1

while floor > 0:
    for i in range(floor):
        dp[floor-1][i] += max(dp[floor][i], dp[floor][i+1])

    floor -= 1

print(dp[0][0])