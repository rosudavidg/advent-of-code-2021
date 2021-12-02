def solve_puzzle(data):
    data = list(map(int, data))

    res = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            res += 1

    return res
