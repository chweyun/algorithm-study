n, k = int(input()), int(input())
start, end = 1, k
answer = -1

while start <= end:
    mid = (start+end)//2

    sum_ = 0
    for i in range(1, n+1):
        sum_ += min(mid//i, n)

    if sum_ >= k:
        answer = mid
        end = mid-1
    else:
        start = mid+1

print(answer)