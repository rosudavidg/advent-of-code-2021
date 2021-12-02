def solve_puzzle(data):
    h, d, aim = 0, 0, 0

    for line in data:
        direction, offset = line.split()
        offset = int(offset)

        if direction == 'forward':
            h += offset
            d += (offset * aim)
        elif direction == 'down':
            aim += offset
        elif direction == 'up':
            aim -= offset

    return h * d
