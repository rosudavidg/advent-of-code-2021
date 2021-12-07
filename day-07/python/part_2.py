def parse_data(data):
    crabs_list = list(map(int, data[0].split(',')))
    crabs_dict = dict()

    for crab in crabs_list:
        if crab in crabs_dict:
            crabs_dict[crab] += 1
        else:
            crabs_dict[crab] = 1

    return crabs_dict


def find_min_fuel(crabs):
    min_fuel = 9999999999
    min_val = min(crabs.keys())
    max_val = max(crabs.keys())

    for target in range(min_val, max_val + 1):
        fuel = 0
        for crab, count in crabs.items():
            diff = abs(crab - target)
            fuel += int(diff * (diff + 1) / 2) * count

            if fuel > min_fuel:
                break

        if fuel < min_fuel:
            min_fuel = fuel

    return min_fuel


def solve_puzzle(data):
    crabs = parse_data(data)

    return find_min_fuel(crabs)
