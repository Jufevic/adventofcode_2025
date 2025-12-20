from collections import defaultdict
from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input_1.txt'

graph = defaultdict(set)

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        parent, children = parse("{}: {}", line)
        for child in children.split():
            graph[parent].add(child)


def paths_between(start, end):
    """Give the number of paths between `start` and `end` nodes

    :param start: start node
    :param end: end node
    :return: number of paths
    """
    frontier = {start: 1}
    total = 0
    while frontier:
        new_frontier = defaultdict(int)
        for node, weight in frontier.items():
            if node == end:
                total += weight
                continue
            for child in graph[node]:
                new_frontier[child] += weight
        frontier = new_frontier
    return total

print(paths_between("svr", "fft") * paths_between("fft", "dac") * paths_between("dac", "out"))
