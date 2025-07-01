import sys
input = sys.stdin.readline

arr = input().strip()
stack, count, checked = [], 0, False

for i, v in enumerate(arr):
    if checked:
        checked = False
        continue

    if v == "(":
        if i < len(arr)-1 and arr[i+1] == ")":
            count += len(stack)
            checked = True
        else:
            stack.append(i)
    else:
        stack.pop()
        count += 1

print(count)