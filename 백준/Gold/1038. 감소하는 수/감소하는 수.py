from itertools import combinations

N = int(input())
result = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        result.append(int("".join(map(str, num))))

result.sort()
print(result[N] if len(result) > N else -1)