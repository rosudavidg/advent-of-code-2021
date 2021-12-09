import itertools

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

ALL_SEGMENTS = (set('abcefg'),
                set('cf'),
                set('acdeg'),
                set('acdfg'),
                set('bcdf'),
                set('abdfg'),
                set('abdefg'),
                set('acf'),
                set('abcdefg'),
                set('abcdfg'),
                )


def solve(target, data):
    count = 0

    for line in data:
        outputs = line.split('|')[1]
        for display in outputs.split():
            if len(display) in target:
                count += 1

    return count


def parse_input(data):
    lines = []
    for line in data:
        left, right = line.split('|')

        left_split = list(map(list, left.strip().split(' ')))
        right_split = list(map(list, right.strip().split(' ')))

        lines.append((left_split, right_split))

    return lines


def solve_line(line):
    left, right = line
    digits = left + right
    solutions = list(itertools.permutations(
        ['a', 'b', 'c', 'd', 'e', 'f', 'g']))

    for solution in solutions:
        mapping = {
            solution[0]: 'a',
            solution[1]: 'b',
            solution[2]: 'c',
            solution[3]: 'd',
            solution[4]: 'e',
            solution[5]: 'f',
            solution[6]: 'g',
        }
        found = True

        for digit in digits:
            if set([mapping[segment] for segment in digit]) not in ALL_SEGMENTS:
                found = False
                break

        if found:
            break

    s = 0
    for digit in right:
        number = ALL_SEGMENTS.index(
            set([mapping[segment] for segment in digit]))
        s = s * 10 + number

    return s


def solve_lines(lines):
    return sum(map(solve_line, lines))


def solve_puzzle(data):
    lines = parse_input(data)

    return solve_lines(lines)
