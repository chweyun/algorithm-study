import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
deq = deque()

for i in range(N):
    now = list(map(str, input().split()))

    if now[0] == 'push':
        deq.append(now[1])
    elif now[0] == 'pop':
        if len(deq):
            print(deq.popleft())
        else:
            print(-1)
    elif now[0] == 'size':
        print(len(deq))
    elif now[0] == 'empty':
        print(0 if len(deq) else 1)
    elif now[0] == 'front':
        if len(deq):
            print(deq[0])
        else:
            print(-1)
    else:
        if len(deq):
            print(deq[-1])
        else:
            print(-1)
