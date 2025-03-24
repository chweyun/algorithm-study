import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))

left, right = 0, w - 1  # 양쪽 끝에서 시작
left_max, right_max = block[left], block[right]
result = 0

while left < right:
    if left_max < right_max:  # 왼쪽이 낮다면 왼쪽 포인터 이동
        left += 1
        if block[left] < left_max:
            result += left_max - block[left]
        else:
            left_max = block[left]
    else:  # 오른쪽이 낮다면 오른쪽 포인터 이동
        right -= 1
        if block[right] < right_max:
            result += right_max - block[right]
        else:
            right_max = block[right]

print(result)
