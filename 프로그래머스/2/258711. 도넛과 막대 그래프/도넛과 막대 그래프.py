def solution(edges):
    data = {}
    result = [0, 0, 0, 0]
    graph_no = 0

    for i in edges:
        _out, _in = i[0], i[1]

        if _out not in data:
            data[_out] = [[],[]]
        if _in not in data:
            data[_in] = [[],[]]

        data[_out][1].append(_in)
        data[_in][0].append(_out)

    for node in data:
        # 새로운 정점
        if len(data[node][0]) == 0 and len(data[node][1]) >= 2:
            result[0] = node
            graph_no = len(data[node][1])
            del data[node]
            break

    for node in data:
        data[node][0] = [v for v in data[node][0] if v != result[0]]
        data[node][1] = [v for v in data[node][1] if v != result[0]]

    for node in data:
        # 막대 : 아웃풋 0, 인풋 0 or 1
        if (len(data[node][0]) == 1 or len(data[node][0]) == 0) and len(data[node][1]) == 0:
            result[2] += 1
        # 8자 : 아웃풋 2 이상, 인풋 2 이상
        elif len(data[node][0]) >= 2 and len(data[node][1]) >= 2:
            result[3] += 1

    result[1] = graph_no - result[2] - result[3]
    
    return result