STEPS = 100
SIZE = 10


def parse_data(data):
    return list(map(lambda line: list(map(int, [c for c in line])), data))


def get_neighbours(i, j):
    neighbours = []

    if i > 0:
        neighbours.append((i - 1, j))
    if j > 0:
        neighbours.append((i, j - 1))
    if i < SIZE - 1:
        neighbours.append((i + 1, j))
    if j < SIZE - 1:
        neighbours.append((i, j + 1))
    if i > 0 and j > 0:
        neighbours.append((i - 1, j - 1))
    if i < SIZE - 1 and j < SIZE - 1:
        neighbours.append((i + 1, j + 1))
    if i > 0 and j < SIZE - 1:
        neighbours.append((i - 1, j + 1))
    if i < SIZE - 1 and j > 0:
        neighbours.append((i + 1, j - 1))

    return neighbours


def play_step(grid):
    flashes = 0
    will_flash = []
    will_flash_used = []

    for i in range(SIZE):
        for j in range(SIZE):
            grid[i][j] += 1

            if grid[i][j] > 9:
                will_flash.append((i, j))

    while len(will_flash) > 0:
        i, j = will_flash.pop()
        will_flash_used.append((i, j))
        flashes += 1

        for i_n, j_n in get_neighbours(i, j):
            grid[i_n][j_n] += 1

            if grid[i_n][j_n] > 9 and (i_n, j_n) not in will_flash and (i_n, j_n) not in will_flash_used:
                will_flash.append((i_n, j_n))

    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] > 9:
                grid[i][j] = 0

    return flashes


def play_steps(grid):
    flashes = 0

    for _ in range(STEPS):
        flashes += play_step(grid)

    return flashes


def solve_puzzle(data):
    grid = parse_data(data)

    flashes = play_steps(grid)

    return flashes
