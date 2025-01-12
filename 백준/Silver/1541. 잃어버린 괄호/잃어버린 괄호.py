n = list(map(str, input().split('-')))
isMinus = n[0] == '-'

for i in range(len(n)):
    l = list(map(int, n[i].split('+')))
    n[i] = sum(l)

res = n[0]
if isMinus:
    res = -(n[0])

for i in range(1, len(n)):
    res -= n[i]

print(res)
