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

for a, b in sorted(pairs, key=lambda x: euclidean(x[0], x[1])):
    joined_circuit = circuits[a] | circuits[b]
    for circuit in joined_circuit:
        circuits[circuit] = joined_circuit
    if all(len(circuit) > 1 for circuit in circuits.values()):
        break

print(a[0] * b[0])