def solution(begin, end):
    block = [0] * (end - begin + 1)

    for n in range(1, 10000001):
        start = max(n * 2, (begin + n - 1) // n * n) 
        for i in range(start, end + 1, n):
            if begin <= i <= end:
                block[i - begin] = n

    return block
