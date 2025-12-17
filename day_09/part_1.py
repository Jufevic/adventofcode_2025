from pathlib import Path
from parse import parse
from itertools import combinations

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

tiles = []
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        x, y = parse("{:d},{:d}", line)
        tiles.append((x, y))

areas = []
for (x_a, y_a), (x_b, y_b) in combinations(tiles, 2):
    areas.append((abs(x_a - x_b) + 1) * (abs(y_a - y_b) + 1))
print(max(areas))