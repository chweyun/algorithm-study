import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville)>=2:
        a, b = heapq.heappop(scoville), heapq.heappop(scoville)
        if a >= K:
            return answer

        heapq.heappush(scoville, a+(b*2))
        answer += 1
        
    if heapq.heappop(scoville) < K:
        return -1

    return answer