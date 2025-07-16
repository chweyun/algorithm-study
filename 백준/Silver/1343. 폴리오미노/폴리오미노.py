import sys
input = sys.stdin.readline

board = input().strip()
idx = 0
new_board = ''

while idx < len(board):
    if board[idx:idx+4] == 'XXXX':
        idx += 4
        new_board += 'AAAA'
    elif board[idx:idx+2] == 'XX':
        idx += 2
        new_board += 'BB'
    elif board[idx] == 'X':
        new_board = -1
        break
    else:
        new_board += board[idx]
        idx += 1

print(new_board)