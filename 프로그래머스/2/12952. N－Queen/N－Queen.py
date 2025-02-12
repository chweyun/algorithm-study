def solution(n):
    global cnt
    cnt = 0
    cols = set()
    diag1 = set()
    diag2 = set()

    def dfs(row):
        global cnt
        if row == n:
            cnt += 1
        else:
            for col in range(n):
                if col in cols or (row+col) in diag1 or (row-col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row+col)
                diag2.add(row-col)

                dfs(row+1)

                cols.remove(col)
                diag1.remove(row+col)
                diag2.remove(row-col)


    dfs(0)
    return cnt