from collections import defaultdict
from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

start = 0
rows = []
with open(DEMO_INPUT_FILE) as f:
    for line in f.read().splitlines()[::2]:
        if "S" in line:
            start = line.index("S")
        else:
            rows.append({i for i, value in enumerate(line) if value == "^"})


beams = defaultdict(int)
beams[start] = 1
for splitters in rows:
    for split in splitters & beams.keys():
        value = beams.pop(split)
        beams[split - 1] += value
        beams[split + 1] += value
print(sum(beams.values()))
