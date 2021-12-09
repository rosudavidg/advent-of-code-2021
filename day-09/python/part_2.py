def parse_input(data):
    return [list(map(int, str(line))) for line in data]


def is_low_point(heights, height, width, i, j):
    if i > 0 and heights[i - 1][j] <= heights[i][j]:
        return False

    if j > 0 and heights[i][j - 1] <= heights[i][j]:
        return False

    if i < height - 1 and heights[i + 1][j] <= heights[i][j]:
        return False

    if j < width - 1 and heights[i][j + 1] <= heights[i][j]:
        return False

    return True


def get_low_points(heights):
    low_points = []
    height = len(heights)
    width = len(heights[0])

    for i in range(height):
        for j in range(width):
            if is_low_point(heights, height, width, i, j):
                low_points.append((i, j))

    return low_points


def find_basin_size(heights, low_point):
    height = len(heights)
    width = len(heights[0])
    queue = [low_point]
    used = []
    size = 0

    while len(queue) != 0:
        point = queue.pop(0)
        h, w = point

        if heights[h][w] != 9:
            size += 1
            used.append(point)
            if h - 1 >= 0 and (h - 1, w) not in used and (h - 1, w) not in queue:
                queue.append((h - 1, w))
            if w - 1 >= 0 and (h, w - 1) not in used and (h, w - 1) not in queue:
                queue.append((h, w - 1))
            if h + 1 < height and (h + 1, w) not in used and (h + 1, w) not in queue:
                queue.append((h + 1, w))
            if w + 1 < width and (h, w + 1) not in used and (h, w + 1) not in queue:
                queue.append((h, w + 1))

    return size


def find_basins_sizes(heights, low_points):
    return [find_basin_size(heights, low_point) for low_point in low_points]


def solve_puzzle(data):
    heights = parse_input(data)

    low_points = get_low_points(heights)

    basins_sizes = find_basins_sizes(heights, low_points)

    top_basins = sorted(basins_sizes, reverse=True)[:3]
    return top_basins[0] * top_basins[1] * top_basins[2]
