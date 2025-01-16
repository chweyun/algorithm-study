a = list(map(int, input().split()))
c = int(input())
n = int(input())

result = 1

for i in range(n, 101):
    fn = a[0]*i + a[1]
    gn = i

    if fn > gn*c:
        result = 0

print(result)