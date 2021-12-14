ROUNDS = 40


def parse_data(data):
    polymer = data[0]
    rules = dict()

    for i in range(2, len(data)):
        polymer_from, polymer_to = data[i].split(' -> ')
        rules[polymer_from] = polymer_to

    return polymer, rules


def get_freq_helper(polymer, rules, rounds, memo):
    if rounds == 0:
        return dict()

    if (polymer, rounds) in memo:
        return memo[(polymer, rounds)]

    freq_left = get_freq_helper(
        polymer[0] + rules[polymer], rules, rounds - 1, memo)
    freq_right = get_freq_helper(
        rules[polymer] + polymer[1], rules, rounds - 1, memo)

    freq = {rules[polymer]: 1}

    for key, values in freq_left.items():
        if key in freq:
            freq[key] += values
        else:
            freq[key] = values

    for key, values in freq_right.items():
        if key in freq:
            freq[key] += values
        else:
            freq[key] = values

    memo[(polymer, rounds)] = freq

    return freq


def get_freq(polymer, rules, rounds):
    freq = dict()

    for letter in polymer:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    memo = dict()

    for i in range(len(polymer) - 1):
        freq_helper = get_freq_helper(polymer[i:i+2], rules, rounds, memo)

        for key, values in freq_helper.items():
            if key in freq:
                freq[key] += values
            else:
                freq[key] = values

    return freq


def get_result(polymer, freq):
    max_freq = freq[polymer[0]]
    min_freq = freq[polymer[0]]

    for value in freq.values():
        if value > max_freq:
            max_freq = value
        if value < min_freq:
            min_freq = value

    return max_freq - min_freq


def solve_puzzle(data):
    polymer, rules = parse_data(data)

    freq = get_freq(polymer, rules, ROUNDS)

    return get_result(polymer, freq)
