def solution(cards):
    answer = []
    visited = [False] * (len(cards)+1)

    for card_pivot in cards:
        if not visited[card_pivot]:
            queue = []

            while card_pivot not in queue:
                queue.append(card_pivot)
                card_pivot = cards[card_pivot-1]
                visited[card_pivot] = True

            answer.append(len(queue))

    if answer[0] == len(cards):
        return 0
    else:
        answer.sort()
        return answer[-1] * answer[-2]