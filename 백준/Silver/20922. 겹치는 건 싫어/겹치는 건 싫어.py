import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
left, max_len, counter = 0, 0, defaultdict(int)

for right in range(n):
    counter[arr[right]] += 1

    while counter[arr[right]] > k:
        counter[arr[left]] -= 1
        left += 1
    max_len = max(max_len, right - left + 1)

print(max_len)