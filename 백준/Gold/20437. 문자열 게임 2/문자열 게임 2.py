import sys
input = sys.stdin.readline
from collections import defaultdict

for _ in range(int(input())):
    W, T = input().strip(), int(input())
    words = defaultdict(list)

    for i in range(len(W)):
        if W.count(W[i]) >= T:
            words[W[i]].append(i)

    if words:
        min_count, max_count = float('inf'), 0

        for word in words:
            for i in range(len(words[word])-T+1):
                length = words[word][i+T-1] - words[word][i] + 1
                max_count = max(max_count, length)
                min_count = min(min_count, length)

        print(min_count, max_count)
    else:
        print(-1)