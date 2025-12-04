from pathlib import Path

import numpy as np
from scipy.signal import convolve2d

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

with open(INPUT_FILE) as f:
    grid = np.array([list(line) for line in f.read().splitlines()])
grid = (grid == "@").astype(int)
kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])


convolution = convolve2d(grid, kernel, mode="same")
print(((grid == 1) & (convolution < 4)).sum())
