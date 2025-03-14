import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
max_x, max_y = 0, 0

for i in range(n):
    if arr[i][1] > max_y:
        max_x, max_y = arr[i][0], arr[i][1]

arr.sort(key=lambda x: x[0])
result = max_y

# 가장 높은 기둥의 왼쪽 처리
now_pivot = arr[0][1]
for l in range(n):
    if arr[l][0] == max_x:
        break

    now_x, now_y = arr[l][0], arr[l][1]
    now_pivot = max(now_pivot, arr[l][1])
    result += now_pivot * (arr[l+1][0]-arr[l][0])

# 가장 높은 기둥의 오른쪽 처리
now_pivot = arr[-1][1]
for r in range(n-1, -1, -1):
    if arr[r][0] == max_x:
        break

    now_x, now_y = arr[r][0], arr[r][1]
    now_pivot = max(now_pivot, arr[r][1])
    result += now_pivot * (arr[r][0]-arr[r-1][0])

print(result)


