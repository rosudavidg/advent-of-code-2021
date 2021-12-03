def solve_puzzle(data):
    size = len(data[0])
    arr = [0 for i in range(size)]

    for number in data:
        for index, bit in enumerate(number):
            arr[index] += int(bit)

    gamma = ['1' if e > len(data) / 2 else '0' for e in arr]
    beta = ['0' if e > len(data) / 2 else '1' for e in arr]

    gamma_str = ''
    for i in gamma:
        gamma_str += i

    beta_str = ''
    for i in beta:
        beta_str += i

    return int(gamma_str, 2) * int(beta_str, 2)
