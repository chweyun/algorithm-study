import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
deq = deque()

for _ in range(N):
    now = list(map(str, input().split()))

    if now[0] == 'push_front':
        deq.appendleft(now[1])
    elif now[0] == 'push_back':
        deq.append(now[1])
    elif now[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif now[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif now[0] == 'size':
        print(len(deq))
    elif now[0] == 'empty':
        print(0 if deq else 1)
    elif now[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    else:
        if deq:
            print(deq[-1])
        else:
            print(-1)
