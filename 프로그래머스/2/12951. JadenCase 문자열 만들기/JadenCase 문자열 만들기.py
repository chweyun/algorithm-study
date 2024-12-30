def solution(s):
    result = list(map(str, s))

    if type(result[0]) == str:
        result[0] = result[0].upper()

    for i in range(len(result) - 1):
        if result[i] == ' ' and result[i+1] != ' ' and type(result[i+1]) == str :
            result[i+1] = result[i+1].upper()
        elif type(result[i+1]) == str:
            result[i+1] = result[i+1].lower()

    return ''.join(result)