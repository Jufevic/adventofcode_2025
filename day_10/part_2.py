from pathlib import Path
import re
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

all_buttons = []
all_joltages = []
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        if match := re.match(r"\[(.*)\] \((.*)\) \{(.*)\}", line):
            _, buttons, joltages = match.groups()
            buttons = [[int(i) for i in group.split(",")] for group in buttons.split(") (")]
            all_buttons.append(buttons)
            joltages = tuple(int(i) for i in joltages.split(","))
            all_joltages.append(joltages)

total_presses = 0

for buttons, joltages in zip(all_buttons, all_joltages):
    n_buttons = len(buttons)
    A = np.zeros((len(joltages), n_buttons), dtype=int)
    for col, button in enumerate(buttons):
        A[button, col] = 1
    c = np.ones(n_buttons)  # Minimize total number of button presses
    b = np.array(joltages)
    # Build the problem
    constraints = LinearConstraint(A, b, b)
    # Numbers of button presses must be positive
    bounds = Bounds(lb=np.zeros(n_buttons), ub=np.full(n_buttons, np.inf))
    # Numbers of button presses must be integers
    integrality = np.ones(n_buttons)
    # Solve the problem
    res = milp(
        c=c,
        constraints=constraints,
        bounds=bounds,
        integrality=integrality
    )
    total_presses += int(res.fun)

print(total_presses)
