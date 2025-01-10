n = int(input())
city = list(map(int, input().split()))
m = int(input())

l, r = 0, max(city)
mid = (l+r)//2
result = 0

while l <= r:
    temp = []
    for i in city:
        temp.append(i if i <= mid else mid)

    if sum(temp) <= m:
        l = mid+1
        result = mid
    else:
        r = mid-1
    mid = (l+r)//2

print(result)