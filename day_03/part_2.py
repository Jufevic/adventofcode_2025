from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

total_joltage = 0
with open(INPUT_FILE) as f:
    for bank in f.read().splitlines():
        digits = [int(i) for i in bank]
        bank_joltage = 0
        for index in range(11, -1, -1):
            if index == 0:
                first = max(digits)
            else:
                first = max(digits[:-index])
            first_index = digits.index(first)
            digits = digits[first_index + 1 :]
            bank_joltage = 10 * bank_joltage + first
        total_joltage += bank_joltage
        print(f"{bank_joltage=}")

print(total_joltage)
