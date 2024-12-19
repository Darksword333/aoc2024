import re

with open("/workspaces/aoc2024/day3/input.txt", "r") as f:
    input_data = f.read()

def main(input_data):
    motif = r"mul\((\d+),(\d+)\)|(?P<do>do\(\))|(?P<dont>don't\(\))"

    matches = re.finditer(motif, input_data)
    instructions = []
    result = 0
    enable = True
    for match in matches:
        if match.group(1) and match.group(2):  # C'est une instruction mul(X, Y)
            instructions.append(('mul', int(match.group(1)), int(match.group(2))))
        elif match.group('do'):  # C'est un do()
            instructions.append(('do',))
        elif match.group('dont'):  # C'est un don't()
            instructions.append(('dont',))
    for element in instructions:
        if element[0] == "mul" and enable == True:
            result += element[1] * element[2]
        elif element[0] == "do":
            enable = True
        elif element[0] == "dont":
            enable = False
    return result


print(main(input_data))