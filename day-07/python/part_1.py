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

    for target in crabs:
        fuel = 0
        for crab, count in crabs.items():
            fuel += abs(crab - target) * count

            if fuel > min_fuel:
                break

        if fuel < min_fuel:
            min_fuel = fuel

    return min_fuel


def solve_puzzle(data):
    crabs = parse_data(data)

    return find_min_fuel(crabs)
