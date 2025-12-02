from pathlib import Path

from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

dial = 50
total = 0
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        direction, steps = parse("{}{:d}", line)
        if direction == "L":
            dial -= steps
        else:
            dial += steps
        dial %= 100
        if dial == 0:
            total += 1

print(total)
