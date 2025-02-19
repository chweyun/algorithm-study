import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n, k, t, m = map(int, input().split())  # 팀 개수 n, 문제 개수 k, 내 팀 ID t, 로그 개수 m
    score = [[0] * (k+1) for _ in range(n)]  # 점수 저장 (k개의 문제 + 제출 횟수)
    last_submission = {}  # 마지막 제출 시간 저장

    for x in range(m):
        i, j, s = map(int, input().split())  # 팀 ID i, 문제 번호 j, 획득한 점수 s
        score[i-1][j-1] = max(score[i-1][j-1], s)  # 최고 점수 갱신
        score[i-1][-1] += 1  # 제출 횟수 증가
        last_submission[i-1] = x  # 마지막 제출 시간 갱신

    # (팀 ID, 총점, 제출 횟수, 마지막 제출 시간)으로 정렬
    ranking = sorted(
        [(i+1, sum(score[i][:-1]), score[i][-1], last_submission.get(i, 0)) for i in range(n)],
        key=lambda x: (-x[1], x[2], x[3])
    )

    # 내 팀 ID(t)의 순위 찾기
    for rank, (team_id, _, _, _) in enumerate(ranking, start=1):
        if team_id == t:
            print(rank)
            break
