import sys
input = sys.stdin.readline

n = int(input())
arr, result, answer, idx, i = [], [], [], 0, 1
for _ in range(n):
    arr.append(int(input()))

while idx < n:
    if result and result[-1] == arr[idx]:
        result.pop()
        answer.append("-")
        idx += 1
    elif not result or result[-1] < arr[idx]:
        result.append(i)
        answer.append("+")
        i += 1
    else:
        print("NO")
        exit()

for ans in answer:
    print(ans)