from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []

def bfs(now_x, now_y, chicken_comb):
    min_dist = 999999
    for ch in chicken_comb:
        dist = abs(now_x-ch[0]) + abs(now_y-ch[1])
        min_dist = min(dist, min_dist)

    return min_dist

def count_dist_for_m(chicken_comb):
    total_dist = 0

    for h in home:
        total_dist += bfs(h[0], h[1], chicken_comb)
    return total_dist



for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

min_dist = []
for i in combinations(chicken, M):
    dist = count_dist_for_m(i)
    if not min_dist or min_dist[1] > dist:
        min_dist = [(i), dist]

print(min_dist[1])