from collections import deque

N = int(input())
adj = [list(input().strip()) for _ in range(N)]
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

visited = set()  # ✅ 리스트 대신 set() 사용
result = []  # ✅ 단지 크기 저장 리스트

def bfs(start_x, start_y):
    deq = deque([(start_x, start_y)])
    visited.add((start_x, start_y))
    count = 1  # ✅ 단지 크기

    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and adj[nx][ny] == '1':
                deq.append((nx, ny))
                visited.add((nx, ny))
                count += 1  # ✅ 단지 크기 증가

    result.append(count)  # ✅ 단지 크기 저장

# ✅ 모든 좌표 탐색 후 bfs 실행
for i in range(N):
    for j in range(N):
        if adj[i][j] == '1' and (i, j) not in visited:
            bfs(i, j)

# ✅ 결과 출력 (오름차순 정렬)
print(len(result))
for size in sorted(result):
    print(size)
