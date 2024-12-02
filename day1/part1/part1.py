with open("/workspaces/aoc2024/day1/input.txt", "r") as f:
    input = f.read()
input = input.split()


def main(input):
    list1 = []
    list2 = []
    min1 = 0
    min2 = 0
    add = 0
    for i in range(len(input)):
        if i%2 == 0:
            list1.append(int(input[i]))
        elif i%2 == 1:
            list2.append(int(input[i]))
    while len(list1) > 0 and len(list2) > 0:
        min1 = get_min_index(list1)
        min2 = get_min_index(list2)
        add+= abs(list1[min1] - list2[min2])
        list1.pop(min1)
        list2.pop(min2)
    return add

def get_min_index(liste):
    min = 0
    for i in range(len(liste)):
        if liste[i] < liste[min]:
            min = i
    return min

print(main(input))