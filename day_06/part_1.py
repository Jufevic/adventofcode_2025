from functools import reduce
from operator import add, mul
from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

with open(INPUT_FILE) as f:
    lines = f.read().splitlines()

problem_lines = lines[:-1]
operation_line = lines[-1]
problems = [[int(i) for i in line.split()] for line in problem_lines]
# Transpose problem matrix
problems = list(map(list, zip(*problems)))
operations = operation_line.split()

total = 0
for problem, operation in zip(problems, operations):
    if operation == "+":
        result = reduce(add, problem, initial=0)
    else:
        result = reduce(mul, problem, initial=1)
    total += result
print(total)
