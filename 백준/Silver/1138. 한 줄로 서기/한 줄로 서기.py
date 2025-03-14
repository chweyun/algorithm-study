import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = [float('inf') for _ in range(n)]
result[arr[0]] = 1

for i in range(1, n):
    cnt = arr[i] # 나보다 키큰, 내 왼쪽에 있어야 하는 사람 수
    tmp = 0

    while cnt or result[tmp] < i+1:
        if result[tmp] > i+1:
            cnt -= 1
        tmp += 1

    result[tmp] = i+1

print(' '.join(map(str, result)))