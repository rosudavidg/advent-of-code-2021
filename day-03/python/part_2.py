from copy import deepcopy

OXYGEN = 0
CO2 = 1


def get_keep_value(data, ones, gas):
    if gas == OXYGEN:
        return 0 if ones >= len(data) / 2 else 1

    if gas == CO2:
        return 1 if ones >= len(data) / 2 else 0


def find_rating(data, size, gas):
    bit = size - 1

    while len(data) > 1:
        ones = sum(map(lambda e: (e >> bit) & 0x1, data))
        keep_value = get_keep_value(data, ones, gas)
        data = list(filter(lambda e: (e >> bit) & 0x1 == keep_value, data))
        bit -= 1

    return data[0]


def find_oxygen_generator_rating(data, size):
    return find_rating(data, size, OXYGEN)


def find_co2_scrubber_rating(data, size):
    return find_rating(data, size, CO2)


def solve_puzzle(data):
    size = len(data[0])
    data = list(map(lambda e: int(e, 2), data))

    oxygen_generator_rating = find_oxygen_generator_rating(
        deepcopy(data), size)
    co2_scrubber_rating = find_co2_scrubber_rating(deepcopy(data), size)

    return oxygen_generator_rating * co2_scrubber_rating
