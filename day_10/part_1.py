from pathlib import Path
import re
from itertools import combinations
import numpy as np

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

all_lights = []
all_buttons = []
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        if match := re.match(r"\[(.*)\] \((.*)\) \{(.*)\}", line):
            lights, buttons, _ = match.groups()
            lights = np.array([char == "#" for char in lights])
            all_lights.append(lights)
            buttons = [[int(i) for i in group.split(",")] for group in buttons.split(") (")]
            all_buttons.append(buttons)


total_presses = 0
for lights, buttons in zip(all_lights, all_buttons):
    n = len(lights)
    for k in range(1, n + 1):
        for pressed_buttons in combinations(buttons, k):
            current_lights = np.full((n,), False)
            for positions in pressed_buttons:
                current_lights[positions] = np.logical_not(current_lights[positions])
            if (current_lights == lights).all():
                break
        else:
            continue
        break
    total_presses += k

print(total_presses)
