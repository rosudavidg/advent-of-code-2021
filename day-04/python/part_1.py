BOARD_SIZE = 5


def parse_input(data):
    numbers_to_draw = list(map(int, data[0].split(',')))
    boards = list()

    board_count = int((len(data) - 1) / (BOARD_SIZE + 1))

    for board_id in range(board_count):
        board = list()
        for board_line in range(BOARD_SIZE):
            row = list(
                map(int, data[2 + board_id * (BOARD_SIZE + 1) + board_line].split()))
            board.append(row)
        boards.append(board)

    return numbers_to_draw, boards


def is_bingo(freqs, board_id, line, column):
    return all(freqs[board_id][line]) or all([row[column] for row in freqs[board_id]])


def play_game(numbers_to_draw, boards):
    freqs = [[[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
             for _ in range(len(boards))]

    for number in numbers_to_draw:
        for board_id, board in enumerate(boards):
            for line in range(BOARD_SIZE):
                for column in range(BOARD_SIZE):
                    if board[line][column] == number:
                        freqs[board_id][line][column] = True
                        if is_bingo(freqs, board_id, line, column):
                            return freqs, board_id, number


def find_result(boards, freqs, board_id, number):
    return number * sum(e for line_id, line in enumerate(boards[board_id]) for column_id,
                        e in enumerate(line) if not freqs[board_id][line_id][column_id])


def solve_puzzle(data):
    numbers_to_draw, boards = parse_input(data)
    freqs, board_id, number = play_game(numbers_to_draw, boards)

    return find_result(boards, freqs, board_id, number)
