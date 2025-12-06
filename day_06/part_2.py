from operator import add, mul
from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

grid = []
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        grid.append(list(line))

numbers_grid = grid[:-1]
operations = grid[-1]
columns = list(map(list, zip(*numbers_grid)))
total = 0
for column, operation in zip(columns, operations):
    if operation == "*":
        result = 1
        func = mul
    elif operation == "+":
        result = 0
        func = add
    try:
        number = int("".join(column).strip())
        result = func(result, number)
    except ValueError:
        total += result
total += result
print(total)
