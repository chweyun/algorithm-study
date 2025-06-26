import sys
input = sys.stdin.readline

inp = input().strip()
parentheses, stack = [], []
couple = { ")": "(", "]": "[" }
answer, temp = 0, 1

for i, v in enumerate(inp):
    if i > 0 and v in couple.keys() and inp[i-1] == couple[v]:
        parentheses.append((v, True))
    else:
        parentheses.append((v, False))

for i, v in enumerate(parentheses):
    value, is_deep = v

    if value in couple.values():
        stack.append(v)
        temp *= 2 if value == "(" else 3
    else:
        if not stack:
            print(0)
            exit()

        prev_value, prev_is_deep = stack.pop()
        if couple[value] != prev_value:
            print(0)
            exit()
        else:
            if is_deep:
                answer += temp
            temp //= 2 if value == ")" else 3
            
if not stack:
    print(answer)
else:
    print(0)