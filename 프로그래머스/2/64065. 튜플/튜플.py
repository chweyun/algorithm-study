def solution(s):
    answer = []
    s = ''.join(s[1:-1].split('{')).split('}')[:-1]

    for i in range(len(s)):
        if s[i][0] == ',':
            s[i] = s[i][1:]
    s.sort(key=lambda k : len(k))

    for i in s:
        for x in i.split(','):
            if x == ',' or int(x) in answer:
                continue
            answer.append(int(x))
            
    return answer