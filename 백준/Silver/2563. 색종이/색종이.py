n = int(input())
list_ = []
for _ in range(n):
    list_.append(list(map(int, input().split())))

result = [[0 for _ in range(100)] for _ in range(100)]

for i in list_:
    for x in range(i[0], i[0]+10):
        for y in range(i[1], i[1]+10):
            result[x][y] = 1

total_sum = sum(sum(row) for row in result)
print(total_sum)

