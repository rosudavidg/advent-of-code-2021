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
                low_points.append(heights[i][j])

    return low_points


def get_risk_score(low_points):
    return sum(list(map(lambda e: e + 1, low_points)))


def solve_puzzle(data):
    heights = parse_input(data)

    low_points = get_low_points(heights)

    print(low_points)

    return get_risk_score(low_points)
