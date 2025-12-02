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
        for pattern_length in range(n // 2, 0, -1):
            repetitions, remainder = divmod(n, pattern_length)
            if remainder == 0:
                if all(
                    digits[i * pattern_length : (i + 1) * pattern_length]
                    == digits[:pattern_length]
                    for i in range(repetitions)
                ):
                    total += number
                    break

print(total)
