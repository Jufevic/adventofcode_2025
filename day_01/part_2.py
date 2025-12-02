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
            new_dial = dial - steps
        else:
            new_dial = dial + steps
        turns, new_remainder = divmod(new_dial, 100)
        # General case
        total += abs(turns)
        if direction == "L":
            # Special case: don't count twice if starting from 0
            if dial == 0 and turns < 0:
                total -= 1
            # Special case: arriving to 0 counts
            if new_remainder == 0:
                total += 1
        dial = new_remainder

print(total)
