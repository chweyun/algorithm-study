from collections import deque

coin = 0

def check(n, hand, deck):
    global coin
    
    # 코인을 사용하지 않고, 손에 든 카드로만 턴을 넘긴다.
    for x in hand:
        if (n+1) - x in hand:
            hand.remove(x)
            hand.remove((n+1) - x)
            return True

    # 코인을 1개 사용하여, 손에 든 카드 1장, 뽑은 카드 1장으로 턴을 넘긴다.
    for x in hand:
        if coin < 1:
            break

        if (n+1) - x in deck:
            hand.remove(x)
            deck.remove((n+1) - x)
            coin -= 1
            return True

    # 코인을 2개 사용하여, 뽑은 카드로만 턴을 넘긴다.
    for x in deck:
        if coin < 2:
            break

        if (n+1) - x in deck:
            deck.remove(x)
            deck.remove((n+1) - x)
            coin -= 2
            return True

    # 전부 불가능 > 라운드 종료
    return False

def solution(initial_coin, cards):
    n = len(cards)
    turn = 1
    hand, deck, cards = [], [], deque(cards)
    global coin
    coin = initial_coin

    for i in range(n//3):
        hand.append(cards.popleft())

    while True:
        if len(cards) == 0:
            break

        turn += 1
        deck.append(cards.popleft())
        deck.append(cards.popleft())

        if not check(n, hand, deck):
            turn -= 1
            break

    return turn