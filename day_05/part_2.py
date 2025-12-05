from pathlib import Path

from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

with open(DEMO_INPUT_FILE) as f:
    intervals_block, ingredients_block = f.read().split("\n\n")

intervals = []
for line in intervals_block.splitlines():
    start, end = parse("{:d}-{:d}", line)
    intervals.append([start, end])

intervals.sort()
# Merge intervals
result = []
for start, end in intervals:
    if not result or start > result[-1][1] + 1:
        result.append([start, end])
    result[-1][1] = max(result[-1][1], end)
intervals = result

total = 0
for start, end in intervals:
    total += end - start + 1

print(total)