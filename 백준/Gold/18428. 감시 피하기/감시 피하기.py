import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
dx, dy = (1,-1, 0, 0), (0, 0, 1, -1)
teacher, total, answer = 0, 0, False
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            teacher += 1

def check_wall(x, y):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        while 0<=nx<N and 0<=ny<N and arr[nx][ny] != 'O':
            if arr[nx][ny] == 'S':
                return False
            nx, ny = nx+dx[i], ny+dy[i]

    return True


def brute(count):
    global answer

    if count == 3:
        cnt = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 'T' and check_wall(i, j):
                    cnt += 1

        if cnt == teacher:
            answer = True
            return

    else:
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 'X':
                    arr[i][j] = 'O'
                    count += 1

                    brute(count)

                    arr[i][j] = 'X'
                    count -= 1


brute(0)
if answer:
    print("YES")
else:
    print("NO")