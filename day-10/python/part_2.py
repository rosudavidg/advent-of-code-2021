CLOSING = {
    '<': '>',
    '(': ')',
    '[': ']',
    '{': '}',
}

CLOSINGS = ['}', '>', ')', ']']

SCORE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def get_incomplete(line):
    aux = []

    for c in line:
        if c in CLOSINGS:
            if CLOSING[aux[len(aux) - 1]] == c:
                del aux[len(aux) - 1]
            else:
                return None
        else:
            aux.append(c)

    return aux


def get_all_incomplete(data):
    all_incomplete = []

    for line in data:
        incomplete = get_incomplete(line)
        if incomplete is not None:
            all_incomplete.append(incomplete)

    return all_incomplete


def get_score(incomplete):
    missings = list(
        map(lambda l: list(map(lambda e: CLOSING[e], l))[::-1], incomplete))

    scores = []

    for line in missings:
        s = 0
        for e in line:
            s = s * 5 + SCORE[e]

        scores.append(s)

    return sorted(scores)[int(len(scores) / 2)]


def solve_puzzle(data):
    incomplete = get_all_incomplete(data)

    return get_score(incomplete)
