from itertools import combinations

input_ = []
for i in range(9):
    input_.append(int(input()))

input_.sort()
sum_ = sum(input_)

for j in combinations(input_,2):
    if sum_ - j[0] - j[1] == 100:
        input_.remove(j[0])
        input_.remove(j[1])
        break

for k in range(7):
    print(input_[k])