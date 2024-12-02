with open("/workspaces/aoc2024/day1/part1/input1.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

def main(input):
    list1 = []
    list2 = []
    min1 = 0
    min2 = 0
    add = 0
    for i in range(len(input)):
        if i%2 == 0:
            list1.append(input[i])
        elif i%2 == 1:
            list2.append(input[i])
    while len(list1) != 0 and len(list2) != 0:
        min1 = min(list1)
        min2 = min(list2)
        add+= abs(min1 - min2)
        list1.remove(min1)
        list2.remove(min2)
    return add

def min(liste):
    min = 0
    for i in range(len(liste)):
        if liste[i] < min:
            min = i
    return min

print(main(input))