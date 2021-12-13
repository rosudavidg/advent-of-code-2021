HORIZONTALLY = 'y'
VERTICALLY = 'x'
EMPTY = '.'
DOT = '#'


def print_grid(grid):
    for line in grid:
        print(''.join(line))

    print()


def parse_input(data):
    points = []
    folds = []

    i = 0
    while i < len(data) and data[i] != '':
        points.append(list(map(int, data[i].split(','))))
        i += 1

    i += 1
    while i < len(data):
        direction, lines = data[i].split('fold along ')[1].split('=')

        folds.append((direction, int(lines)))
        i += 1

    height = max(map(lambda x: x[1], points)) + 1
    width = max(map(lambda x: x[0], points)) + 1

    grid = [[EMPTY for _ in range(width)] for _ in range(height)]

    for x, y in points:
        grid[y][x] = DOT

    return grid, folds


def count_dots(grid):
    return sum(map(lambda line: line.count(DOT), grid))


def make_horizontally_fold(grid, lines):
    left_top = lines
    left_bottom = len(grid) - lines - 1

    new_height = max([left_top, left_bottom])
    new_grid = [[EMPTY for _ in range(len(grid[0]))]
                for _ in range(new_height)]

    top_offset = new_height - left_top
    for i in range(left_top):
        for j in range(len(grid[0])):
            new_grid[i + top_offset][j] = grid[i][j]

    for i in range(lines + 1, len(grid)):
        for j in range(len(grid[0])):
            new_i = new_height - (i - lines)
            new_symbol = DOT if grid[i][j] == DOT else new_grid[new_i][j]
            new_grid[new_i][j] = new_symbol

    return new_grid


def make_vertically_fold(grid, lines):
    left_left = lines
    left_right = len(grid[0]) - lines - 1

    new_width = max([left_left, left_right])
    new_grid = [[EMPTY for _ in range(new_width)]
                for _ in range(len(grid))]

    left_offset = new_width - left_left
    for j in range(left_left):
        for i in range(len(grid)):
            new_grid[i][j + left_offset] = grid[i][j]

    for j in range(lines + 1, len(grid[0])):
        for i in range(len(grid)):
            new_j = new_width - (j - lines)
            new_symbol = DOT if grid[i][j] == DOT else new_grid[i][new_j]
            new_grid[i][new_j] = new_symbol

    return new_grid


def make_fold(grid, fold):
    if fold[0] == HORIZONTALLY:
        return make_horizontally_fold(grid, fold[1])

    if fold[0] == VERTICALLY:
        return make_vertically_fold(grid, fold[1])

    return grid


def make_folds(grid, folds):
    for fold in folds:
        grid = make_fold(grid, fold)

    return grid


def solve_puzzle(data):
    grid, folds = parse_input(data)

    grid = make_folds(grid, folds[:1])

    return count_dots(grid)
