import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l_cursor, r_cursor = [], []
    logger = input().strip()

    for i in logger:
        if i == '-':
            if l_cursor:
                l_cursor.pop()
        elif i == '<':
            if l_cursor:
                r_cursor.append(l_cursor.pop())
        elif i == '>':
            if r_cursor:
                l_cursor.append(r_cursor.pop())
        else:
            l_cursor.append(i)

    print(''.join(l_cursor + r_cursor[::-1]))