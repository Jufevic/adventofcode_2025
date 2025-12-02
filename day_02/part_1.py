from pathlib import Path

from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

with open(INPUT_FILE) as f:
    line = f.readline()

total = 0
for ranges in line.split(","):
    start, end = parse("{:d}-{:d}", ranges)
    for number in range(start, end + 1):
        digits = str(number)
        n = len(digits)
        if digits[: n // 2] == digits[n // 2 :]:
            total += number

print(total)
