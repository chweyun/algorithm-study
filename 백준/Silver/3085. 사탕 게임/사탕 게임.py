import sys
input = sys.stdin.readline

N = int(input())
candy = [list(input().strip()) for _ in range(N)]
dx, dy = (1, 0), (0, -1)
result = 0

def check_cur_max_num():
    curr = 1

    # 가로 확인
    for i in range(N):
        temp = 1
        pivot = 1
        while pivot < N:
            if candy[i][pivot] == candy[i][pivot-1]:
                temp += 1
                curr = max(curr, temp)
            else:
                temp = 1

            pivot += 1

    # 세로 확인
    for j in range(N):
        temp = 1
        pivot = 1
        while pivot < N:
            if candy[pivot][j] == candy[pivot-1][j]:
                temp += 1
                curr = max(curr, temp)
            else:
                temp = 1

            pivot += 1

    return curr

def swap(a, b):
    temp = candy[a[0]][a[1]]
    candy[a[0]][a[1]] = candy[b[0]][b[1]]
    candy[b[0]][b[1]] = temp

for i in range(N):
    for j in range(N):
        for next_dir in range(2):
            if 0 <= i+dx[next_dir] < N and  0 <= j+dy[next_dir] < N and candy[i][j] != candy[i+dx[next_dir]][j+dy[next_dir]]:
                swap([i, j], [i+dx[next_dir], j+dy[next_dir]])
                result = max(result, check_cur_max_num())
                swap([i, j], [i+dx[next_dir], j+dy[next_dir]])

print(result)