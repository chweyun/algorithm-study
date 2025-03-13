import sys
input = sys.stdin.readline

text = list(input().strip())
stack = []
n = int(input())

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'L' and text:
        stack.append(text.pop())  # 왼쪽에서 하나 빼서 오른쪽으로 이동
    elif cmd[0] == 'D' and stack:
        text.append(stack.pop())  # 오른쪽에서 하나 빼서 왼쪽으로 이동
    elif cmd[0] == 'B' and text:
        text.pop()  # 왼쪽에서 삭제
    elif cmd[0] == 'P':
        text.append(cmd[1])  # 왼쪽에 문자 추가
print(''.join(text + stack[::-1]))
