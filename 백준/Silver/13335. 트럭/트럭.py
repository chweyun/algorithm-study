import sys
from collections import deque
input = sys.stdin.readline

N, W, L = map(int, input().split())
truck = list(map(int, input().split()))
now_idx, count = 0, 1
deq = deque([truck[now_idx]])

while sum(deq) or now_idx < N-1:
    nxt_idx = now_idx + 1
    if len(deq) < W and nxt_idx < len(truck):
        count += 1
        if sum(deq) + truck[nxt_idx] <= L:
            deq.append(truck[nxt_idx])
            now_idx += 1
        else:
            deq.append(0)
    elif deq:
        deq.popleft()

print(count + W)