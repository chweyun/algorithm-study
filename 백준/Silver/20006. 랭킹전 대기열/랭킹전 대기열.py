import sys
from collections import deque
input = sys.stdin.readline

p, m = map(int, input().split())
arr = deque([list(map(str, input().split())) for _ in range(p)])
room = []

def possible_room_num(now_level):
    for r in range(len(room)):
        if abs(int(room[r][0][0]) - now_level) <= 10 and len(room[r]) < m:
            return r
    return -1

for i in range(p):
    level, name = arr.popleft()
    room_num = possible_room_num(int(level))

    if room_num == -1:
        room.append([(level, name)])
    else:
        room[room_num].append((level, name))

for i in range(len(room)):
    now_room = room[i]
    now_room.sort(key=lambda x: x[1])
    print("Started!") if len(now_room) == m else print("Waiting!")

    for j in now_room:
        print(" ".join(list(j)))

