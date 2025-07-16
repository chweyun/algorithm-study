N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))
rope.sort()

result = []
for r in rope:
    result.append(r*N)
    N -= 1
print(max(result))