from collections import defaultdict
from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

graph = defaultdict(set)

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        parent, children = parse("{}: {}", line)
        for child in children.split():
            graph[parent].add(child)

frontier = {"you": 1}
total = 0
while frontier:
    new_frontier = defaultdict(int)
    for node, weight in frontier.items():
        if node == "out":
            total += weight
            continue
        for child in graph[node]:
            new_frontier[child] += weight
    frontier = new_frontier

print(total)