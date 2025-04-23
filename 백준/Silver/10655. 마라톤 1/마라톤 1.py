import sys
input = sys.stdin.readline

n = int(input())
checked = [list(map(int, input().split())) for _ in range(n)]
dist = [0]*n
max_dist = 0
result = 0

for i in range(1, n-1):
    bf_val = abs(checked[i-1][0] - checked[i][0]) + abs(checked[i-1][1] - checked[i][1])
    af_val = abs(checked[i][0] - checked[i+1][0]) + abs(checked[i][1] - checked[i+1][1])
    val = bf_val + af_val - (abs(checked[i-1][0] - checked[i+1][0]) + abs(checked[i-1][1] - checked[i+1][1]))
    max_dist = max(max_dist, val)
    result += bf_val
    
result += abs(checked[n-2][0] - checked[n-1][0]) + abs(checked[n-2][1] - checked[n-1][1])
print(result - max_dist)