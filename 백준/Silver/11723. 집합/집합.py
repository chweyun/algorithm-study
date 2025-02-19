import sys

input = sys.stdin.readline
M = int(input())
dic = set()

for _ in range(M):
    calc = list(map(str, input().split()))

    if len(calc) == 1:
        calculation, num = calc[0], None
    else:
        calculation, num = calc[0], int(calc[1])


    if calculation == 'add':
        dic.add(num)
    elif calculation == 'remove' and num in dic:
        dic.discard(num)
    elif calculation == 'check':
        print(1) if num in dic else print(0)
    elif calculation == 'toggle':
        dic.discard(num) if num in dic else dic.add(num)
    elif calculation == 'all':
        dic.update(range(1,21))
    else:
        dic.clear()


