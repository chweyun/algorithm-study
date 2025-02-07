def solution(q, speeds):
    result = []

    while q:
        count = 1
        while q[0]+speeds[0]*count < 100:
            count += 1

        for i in range(len(q)):
            q[i] = q[i]+speeds[i]*count

        total = 0
        while q and q[0] >= 100:
            q.pop(0)
            speeds.pop(0)
            total += 1

        result.append(total)
    
    return result
