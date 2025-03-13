import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    revenue = 0
    max_price = 0

    for i in range(N-1, -1, -1):
        if max_price < arr[i]:
            max_price = arr[i]
        else:
            revenue += max_price-arr[i]
    print(revenue)