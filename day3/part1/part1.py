import re

# Lecture du fichier
with open("/workspaces/aoc2024/day3/input.txt", "r") as f:
    input_data = f.read()

def main(input_data):
    motif = r'mul\((\d+),(\d+)\)'
    matches = re.findall(motif, input_data)

    total = sum(int(x) * int(y) for x, y in matches)
    return total

print(main(input_data))