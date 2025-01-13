n = int(input())
input_ = []
for _ in range(n):
    input_.append(input())
answer = 0

for i in input_:
    temp_list = []

    for j in i:
        if j not in temp_list:
            temp_list.append(j)
        elif temp_list[-1] == j:
            continue
        else:
            temp_list[0] = -1
            break

    if temp_list[0] != -1:
        answer += 1

print(answer)