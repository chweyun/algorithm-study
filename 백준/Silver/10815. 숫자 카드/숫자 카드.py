import sys
input = sys.stdin.readline

N = int(input())
Ncard = list(map(int, input().split())) # 상근이가 가진 카드
Ncard.sort()
M = int(input())
Mcard = list(map(int, input().split())) # 상근이가 가진 건지 구분해야 하는 숫자들
res = []

def binary(array, start, end, target) :
    while start <= end :
        mid = (start + end) // 2
        if array[mid] == target :
            return 1
        elif array[mid] > target :
            end = mid-1
        else :
            start = mid+1
    return 0

for i in range(M) :
    res.append(binary(Ncard, 0, N-1, Mcard[i]))

for i in range(len(res)) :
    print(res[i], end=" ")

