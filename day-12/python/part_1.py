from typing import get_args
from copy import deepcopy

SMALL_CAVE = 0
LARGE_CAVE = 1


def is_large_cave(name):
    return ord(name[0]) >= ord('A') and ord(name[0]) <= ord('Z')


def add_node(nodes, adjacents, name):
    type = LARGE_CAVE if is_large_cave(name) else SMALL_CAVE

    node = (name, type)

    if node not in nodes:
        nodes.append(node)

    if node not in adjacents:
        adjacents[node] = []

    return node


def parse_data(data):
    nodes = []
    adjacents = {}

    for line in data:
        name1, name2 = line.split('-')

        node1 = add_node(nodes, adjacents, name1)
        node2 = add_node(nodes, adjacents, name2)

        adjacents[node1].append(node2)
        adjacents[node2].append(node1)

    return nodes, adjacents


def get_paths_helper(current_path, adjacents, paths, end_node):
    current_node = current_path[len(current_path) - 1]

    if current_node == end_node:
        paths.append(deepcopy(current_path))
        return

    new_adjacents = deepcopy(adjacents)

    if current_node[1] == SMALL_CAVE:
        del new_adjacents[current_node]
        for adj in new_adjacents.values():
            if current_node in adj:
                adj.remove(current_node)

    for adjacent in adjacents[current_node]:
        get_paths_helper(current_path + [adjacent],
                         new_adjacents,
                         paths,
                         end_node)


def get_paths(graph, start_name='start', end_name='end'):
    start_node = (start_name, LARGE_CAVE if is_large_cave(
        start_name) else SMALL_CAVE)
    end_node = (end_name, LARGE_CAVE if is_large_cave(
        end_name) else SMALL_CAVE)

    nodes, adjacents = deepcopy(graph)
    current_path = [start_node]
    paths = []

    get_paths_helper(current_path, adjacents, paths, end_node)

    return paths


def solve_puzzle(data):
    graph = parse_data(data)

    paths = get_paths(graph, start_name='start', end_name='end')

    return len(paths)
