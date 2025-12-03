from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

total_joltage = 0
with open(INPUT_FILE) as f:
    for bank in f.read().splitlines():
        digits = [int(i) for i in bank]
        first = max(digits[:-1])
        first_index = digits.index(first)
        second = max(digits[first_index + 1 :])
        bank_joltage = 10 * first + second
        total_joltage += bank_joltage

print(total_joltage)
