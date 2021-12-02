def solve_puzzle(data):
    data = list(map(int, data))

    res = 0
    window = 3
    prev = sum(data[:window])

    for i in range(window, len(data)):
        curr = prev - data[i - window] + data[i]

        if curr > prev:
            res += 1

        prev = curr

    return res
