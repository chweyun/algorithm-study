n, l = map(int, input().split())
hole = list(map(int, input().split()))
hole.sort()
count = 0

while hole:
    i, j = 0, 0

    while len(hole) > j and hole[i] + l-1 >= hole[j]:
        j += 1

    hole = hole[j:]
    count += 1

print(count)


