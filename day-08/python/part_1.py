SEGMENTS = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}


def solve(target, data):
    count = 0

    for line in data:
        outputs = line.split('|')[1]
        for display in outputs.split():
            if len(display) in target:
                count += 1

    return count


def solve_puzzle(data):
    target = [len(SEGMENTS[e]) for e in [1, 4, 7, 8]]

    return solve(target, data)
