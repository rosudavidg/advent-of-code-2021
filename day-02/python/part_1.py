def solve_puzzle(data):
    h, d = 0, 0

    for line in data:
        direction, offset = line.split()
        offset = int(offset)

        if direction == 'forward':
            h += offset
        elif direction == 'down':
            d += offset
        elif direction == 'up':
            d -= offset

    return h * d
