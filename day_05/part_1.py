from pathlib import Path

from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

with open(INPUT_FILE) as f:
    intervals_block, ingredients_block = f.read().split("\n\n")

intervals = []
for line in intervals_block.splitlines():
    start, end = parse("{:d}-{:d}", line)
    intervals.append([start, end])

total = 0
for line in ingredients_block.splitlines():
    ingredient = int(line)
    for start, end in intervals:
        if start <= ingredient <= end:
            total += 1
            break

print(total)