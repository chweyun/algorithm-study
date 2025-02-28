import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
result = 0

for i in range(N):
    li = A.copy()
    start = A[i]
    total = 0

    while li:
        next_pivot = li[-1] if len(li)-li.index(start) > li.index(start) else li[0]
        total += (abs(next_pivot-start))
        li.pop(li.index(start))
        start = next_pivot
        
    result = max(result, total)

print(result)