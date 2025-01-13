score = []
sum_1 = 0
sum_2 = 0
dict_ = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

for _ in range(20):
    score.append(list(map(str, input().split())))
    a, b = float(score[-1][1]), score[-1][2]

    if b == 'P':
        continue

    sum_1 += a*dict_.get(b)
    sum_2 += a

print(sum_1/sum_2)
