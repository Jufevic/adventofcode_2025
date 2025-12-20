from pathlib import Path
import numpy as np
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

with open(INPUT_FILE) as f:
    blocks = f.read().split("\n\n")

regions_block = blocks[-1]

can_fit = 0
for region_line in regions_block.splitlines():
    height, width, presents = parse("{:d}x{:d}: {}", region_line)
    if 8 * sum(int(i) for i in presents.split()) < height * width:
        can_fit += 1

print(can_fit)