import sys
input = sys.stdin.readline

par = {
    "]": "[",
    ")": "(",
}

while True:
    now = input()
    result = False

    if now == '.\n':
        break

    queue = []
    for i in now:
        if i in par.values():
            queue.append(i)

        elif i in par.keys():
            if queue and queue[-1] == par[i]:
                queue.pop()
            else:
                queue.append(i)
                break

    if not queue:
        result = True

    print("yes" if result else "no")

