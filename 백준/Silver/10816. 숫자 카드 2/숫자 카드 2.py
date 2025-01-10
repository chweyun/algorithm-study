from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

# 카드 개수를 미리 세기
card_count = Counter(cards)

# m_arr에 있는 각 숫자에 대해 카드 개수 출력
for num in m_arr:
    print(card_count.get(num, 0), end=' ')