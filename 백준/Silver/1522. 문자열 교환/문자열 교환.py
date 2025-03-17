import sys
input = sys.stdin.readline

ab = list(map(str, input().strip()))
total_a = ab.count('a')
max_a = 0

for i in range(len(ab)):
    a_count = 0
    for j in range(total_a):
        if i+j < len(ab) and ab[i+j] == 'a':
            a_count += 1
        elif i+j >= len(ab) and ab[i+j-len(ab)] == 'a':
            a_count += 1

    max_a = max(max_a, a_count)

print(total_a - max_a)