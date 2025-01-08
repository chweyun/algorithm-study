n, m = map(int, input().split())
board = []
result = 99999

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        changeCount1 = 0  # 첫 칸이 'B'로 시작하는 경우
        changeCount2 = 0  # 첫 칸이 'W'로 시작하는 경우

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:  # 첫 칸과 같은 색이어야 하는 경우
                    if board[x][y] != 'B':  # 'B'로 시작할 경우
                        changeCount1 += 1
                    if board[x][y] != 'W':  # 'W'로 시작할 경우
                        changeCount2 += 1
                else:  # 첫 칸과 다른 색이어야 하는 경우
                    if board[x][y] != 'W':  # 'B'로 시작할 경우
                        changeCount1 += 1
                    if board[x][y] != 'B':  # 'W'로 시작할 경우
                        changeCount2 += 1

        result = min(result, changeCount1, changeCount2)

print(result)


