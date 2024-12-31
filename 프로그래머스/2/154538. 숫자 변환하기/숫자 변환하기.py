from collections import  deque

def solution(x, y, n):
    queue = deque()
    visited = set()

    queue.append((x,0))

    while queue:
        i, j = queue.popleft()

        if i > y or i in visited:
            continue

        visited.add(i)

        if i == y:
            return j

        for k in (i+n, i*2, i*3):
            if k <= y and k not in visited:
                queue.append((k, j+1))

    return -1