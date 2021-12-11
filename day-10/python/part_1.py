CLOSING = {
    '<': '>',
    '(': ')',
    '[': ']',
    '{': '}',
}

CLOSINGS = ['}', '>', ')', ']']

SCORE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def get_illegal(line):
    aux = []

    for c in line:
        if c in CLOSINGS:
            if CLOSING[aux[len(aux) - 1]] == c:
                del aux[len(aux) - 1]
            else:
                return c
        else:
            aux.append(c)

    return None


def get_illegals(data):
    illegals = []

    for line in data:
        illegal = get_illegal(line)
        if illegal is not None:
            illegals.append(illegal)

    return illegals


def get_score(illegals):
    return sum(list(map(lambda e: SCORE[e], illegals)))


def solve_puzzle(data):
    illegals = get_illegals(data)

    return get_score(illegals)
