def solution(info, query):
    answer = []
    case = dict()

    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    case.setdefault((a, b, c, d), list())

    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        case[(a,b,c,d)].append(int(i[4]))
    for c in case:
        case[c].sort()

    for q in query:
        q = q.split()
        score = case[(q[0], q[2], q[4], q[6])]
        wanted = int(q[7])
        
        l, r = 0, len(score)
        
        while l < r:
            mid = (l + r) // 2
            if score[mid] >= wanted:
                r = mid
            else:
                l = mid + 1
        answer.append(len(score) - l)
        
    return answer