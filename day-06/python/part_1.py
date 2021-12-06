PERIOD = 80


def parse_input(data):
    return list(map(int, data[0].split(',')))


def get_number_of_lanternfishes(timers_list):
    timers = {i: 0 for i in range(9)}
    for timer in timers_list:
        timers[timer] += 1

    for week in range(int(PERIOD / 7)):
        new_timers = {i: 0 for i in range(9)}

        for left, count in timers.items():
            if left >= 7:
                new_timers[left - 7] += count
            else:
                new_timers[left] += count
                new_timers[left + 2] += count

        timers = new_timers

    period_left = PERIOD % 7
    new_timers = {i: 0 for i in range(9)}
    for left, count in timers.items():
        if left - period_left >= 0:
            new_timers[left - period_left] += count
        else:
            new_timers[6 - (period_left - left)] += count
            new_timers[8 - (period_left - left)] += count

    timers = new_timers

    return sum([left for left in timers.values()])


def solve_puzzle(data):
    timers = parse_input(data)

    return get_number_of_lanternfishes(timers)
