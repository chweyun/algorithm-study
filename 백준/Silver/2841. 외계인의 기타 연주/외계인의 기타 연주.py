import sys
input = sys.stdin.readline

N, P = map(int, input().split())
melody = [list(map(int, input().split())) for _ in range(N)]
level = [[], [], [], [], [], []]
count = 0

for (i, j) in melody:
    while True:
        if not level[i-1]:
            level[i-1].append(j)
            count += 1
            break
        elif level[i-1][-1] == j:
            break
        elif level[i-1][-1] < j:
            level[i-1].append(j)
            count += 1
            break
        else:
            level[i-1].pop()
            count += 1
            continue

print(count)