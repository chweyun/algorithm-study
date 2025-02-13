from collections import deque

def bfs():
    result = 1
    deq = deque([(A, result)])

    while deq:
        now, count = deq.popleft()
        if now == B:
            print(count)
            return
        if now*2 <= B:
            deq.append((now*2, count+1))
        if now*10+1 <= B:
            deq.append((now*10+1, count+1))
    print(-1)

A,B = map(int, input().split())
bfs()