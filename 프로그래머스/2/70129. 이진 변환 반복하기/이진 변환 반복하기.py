def solution(s):
    count = 0
    zero = 0

    while s != '1':
        count += 1
        temp = 0

        for i in s:
            if i == '0':
                temp += 1

        zero += temp
        len_after = len(s) - temp
        s = str(bin(len_after)[2:])

    return [count, zero]