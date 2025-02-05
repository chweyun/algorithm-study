from collections import deque

TOTAL, NOW, GOAL, UP, DOWN = map(int, input().split())
visited = [False] * (TOTAL+1)

def bfs():
    deq = deque([(NOW, 0)])
    visited[NOW] = True

    while deq:
        v, count = deq.popleft()

        if v == GOAL:
            return print(count)

        for nxt in [v+UP, v-DOWN]:
            if 0<nxt<=TOTAL and not visited[nxt]:
                deq.append((nxt, count+1))
                visited[nxt] = True
    print("use the stairs")

bfs()