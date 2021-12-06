VERTICAL = 1
HORIZONTAL = 2
DIAGONAL = 3


def parse_input(data):
    lines = [list(map(lambda e: list(map(int, e.split(','))),
                  line.split('->'))) for line in data]

    return lines


def get_dimensions(lines):
    puzzle_height = 0
    puzzle_width = 0

    puzzle_height = max(map(lambda e: max(e[0][0], e[1][0]), lines))
    puzzle_width = max(map(lambda e: max(e[0][1], e[1][1]), lines))

    return puzzle_height, puzzle_width


def get_orientation(p1, p2):
    if p1[0] == p2[0]:
        return HORIZONTAL

    if p1[1] == p2[1]:
        return VERTICAL

    return DIAGONAL


def add_line(puzzle, p1, p2):
    if p1[0] > p2[0]:
        p2, p1 = p1, p2

    if p1[1] > p2[1]:
        p2, p1 = p1, p2

    orientation = get_orientation(p1, p2)
    x1, y1 = p1
    x2, y2 = p2

    if orientation == HORIZONTAL:
        x = x1

        for y in range(y1, y2 + 1):
            puzzle[x][y] += 1
    elif orientation == VERTICAL:
        y = y1

        for x in range(x1, x2 + 1):
            puzzle[x][y] += 1
    elif orientation == DIAGONAL:
        if x2 - x1 == y2 - y1:
            d = x2 - x1 + 1
            for i in range(d):
                puzzle[x1 + i][y1 + i] += 1
        elif x1 < x2:
            d = x2 - x1 + 1
            for i in range(d):
                puzzle[x1 + i][y1 + i] += 1
        elif x2 < x1:
            d = x1 - x2 + 1
            for i in range(d):
                puzzle[x1 - i][y1 + i] += 1

    return puzzle


def generate_puzzle(lines, puzzle_height, puzzle_width):
    puzzle = [[0 for _ in range(puzzle_width + 1)]
              for _ in range(puzzle_height + 1)]

    for (x1, y1), (x2, y2) in lines:
        add_line(puzzle, (x1, y1), (x2, y2))

    return puzzle


def get_result(puzzle):
    return sum(list(map(lambda e: len(list(filter(lambda x: x > 1, e))), puzzle)))


def solve_puzzle(data):
    lines = parse_input(data)
    puzzle_height, puzzle_width = get_dimensions(lines)
    puzzle = generate_puzzle(lines, puzzle_height, puzzle_width)

    return get_result(puzzle)
