ROUNDS = 10


def parse_data(data):
    polymer = data[0]
    rules = dict()

    for i in range(2, len(data)):
        polymer_from, polymer_to = data[i].split(' -> ')
        rules[polymer_from] = polymer_to

    return polymer, rules


def play_round(polymer, rules):
    new_polymer = ''

    for i in range(len(polymer) - 1):
        new_polymer += polymer[i]
        new_polymer += rules[polymer[i:i+2]]

    new_polymer += polymer[-1]

    return new_polymer


def play_rounds(polymer, rules, rounds):
    for _ in range(rounds):
        polymer = play_round(polymer, rules)
        print(polymer)
        print()

    return polymer


def get_result(polymer):
    freq = dict()

    for letter in polymer:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

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

    polymer = play_rounds(polymer, rules, ROUNDS)

    return get_result(polymer)
