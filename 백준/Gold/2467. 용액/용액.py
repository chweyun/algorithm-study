import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
l, r = 0, n-1
total, res = abs(arr[l] + arr[r]), (l, r)

while l < r:
    temp = arr[l] + arr[r]
    if abs(temp) < total:
        total, res = abs(temp), (l, r)
        if total == 0:
            break

    if temp < 0:
        l += 1
    else:
        r -= 1

print(arr[res[0]], arr[res[1]])