from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

grid = []
with open(DEMO_INPUT_FILE) as f:
    for line in f.read().splitlines():
        grid.append(list(line))

height = len(grid)
width = len(grid[0])


def removable_locations(grid):
    locations = []
    for row, line in enumerate(grid):
        for column, element in enumerate(line):
            if element != "@":
                continue
            neighbours = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (dx, dy) == (0, 0):
                        continue
                    if (
                        0 <= row + dy < height
                        and 0 <= column + dx < width
                        and grid[row + dy][column + dx] == "@"
                    ):
                        neighbours += 1
            if neighbours < 4:
                locations.append((row, column))
    return locations

total = 0
while len(locations := removable_locations(grid)) > 0:
    total += len(locations)
    for row, column in locations:
        grid[row][column] = "."

print(total)
