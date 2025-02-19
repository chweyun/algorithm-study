import sys

input = sys.stdin.readline
N, M = map(int, input().split())
dic = {}

for i in range(N):
    word = input().strip()

    if len(word) < M:
        continue

    if word in dic:
        dic[word] = dic[word]+1
    else:
        dic[word] = 1

result = sorted(dic, key=lambda x: (-dic[x], -len(x), x))
[print(result[i]) for i in range(len(result))]