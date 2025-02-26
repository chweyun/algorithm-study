import sys
input = sys.stdin.readline
N = int(input()) # N(1 ≤ N ≤ 100,000,000)

if N < 10:
    print(N)
    sys.exit()

last_len = len(str(N))-1
result = 0
while last_len >= 1:
    if last_len > 1:
        result += (9*(10**(last_len-1)))*last_len
    else:
        result += 9*last_len
    last_len -= 1

target = 1
if len(str(N))-1 > 1:
    target = len(str(N))-1

result += (N-(10**target)+1) * len(str(N))

print(result)