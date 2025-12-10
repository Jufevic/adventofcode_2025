from pathlib import Path
import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

junctions = set()
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        junctions.add(tuple(map(int, line.split(","))))

pairs = [(a, b) for a, b in combinations(junctions, 2)]
circuits = {box: {box} for box in junctions}
for a, b in sorted(pairs, key=lambda x: euclidean(x[0], x[1]))[:1000]:
    joined_circuit = circuits[a] | circuits[b]
    for circuit in joined_circuit:
        circuits[circuit] = joined_circuit
unique_circuits = []
seen = set()
for box, circuit in circuits.items():
    if box in seen:
        continue
    seen |= circuit
    unique_circuits.append(circuit)

sizes = [len(circuit) for circuit in unique_circuits]
a, b, c = sorted(sizes, reverse=True)[:3]
print(a * b * c)