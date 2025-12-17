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
edges = [(a, b) for a, b in zip(tiles, tiles[1:] + [tiles[0]])]

max_area = 0
for (x_a, y_a), (x_b, y_b) in combinations(tiles, 2):
    x_a, x_b = sorted([x_a, x_b])
    y_a, y_b = sorted([y_a, y_b])
    # Verify no edge intersect the rectangle
    for ((x_c, y_c), (x_d, y_d)) in edges:
        x_c, x_d = sorted([x_c, x_d])
        y_c, y_d = sorted([y_c, y_d])
        # Vertical line
        if x_c == x_d and x_a < x_c < x_b and y_c < y_b and y_a < y_d:
            break
        # Horizontal line
        if y_c == y_d and y_a < y_c < y_b and x_c < x_b and x_a < x_d:
            break
    else:
        area = (x_b - x_a + 1) * (y_b - y_a + 1)
        if area > max_area:
            max_area = area
print(max_area)
