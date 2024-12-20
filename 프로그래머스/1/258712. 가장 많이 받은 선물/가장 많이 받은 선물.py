def solution(friends, gifts):
    total = {friend: {f: 0 for f in friends} for friend in friends}
    result = [0 for _ in range(len(friends))]

    for i in gifts:
        give, take = i.split(' ')
        total[give][take] += 1

    # 선물 지수
    for i in total:
        give = sum(list(total[i].values()))
        take = sum(inner[i] for inner in total.values())
        total[i]['jisu'] = give - take


    print(total)

    for i in range(len(friends)):
        for j in range(i):
            ps1, ps2 = list(total.keys())[i], list(total.keys())[j]

            if (total[ps1][ps2] > total[ps2][ps1]):
                result[i] += 1
            elif (total[ps1][ps2] < total[ps2][ps1]):
                result[j] += 1
            else:
                ps1_jisu = total[ps1]['jisu']
                ps2_jisu = total[ps2]['jisu']

                if (ps1_jisu > ps2_jisu):
                    result[i] += 1
                elif (ps1_jisu < ps2_jisu) :
                    result[j] += 1
                else : 
                    continue

    return max(result)