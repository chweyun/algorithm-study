import sys
input = sys.stdin.readline
from collections import deque

S, T = input().strip(), input().strip()
deq = deque([T])

while deq:
    now = deq.popleft().strip()

    if len(now) == len(S):
        if now == S:
            print(1)
            sys.exit()
        continue

    if now[-1] == 'A':
        deq.append(now[:-1])
    if now[0] == 'B':
        deq.append(now[:0:-1])

print(0)