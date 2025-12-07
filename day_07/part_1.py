from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

start = 0
rows = []
with open(INPUT_FILE) as f:
    for line in f.read().splitlines()[::2]:
        if "S" in line:
            start = line.index("S")
        else:
            rows.append({i for i, value in enumerate(line) if value == "^"})

total = 0
beams = {start}
for splitters in rows:
    for split in splitters & beams:
        total += 1
        beams.remove(split)
        beams.add(split - 1)
        beams.add(split + 1)
print(total)
