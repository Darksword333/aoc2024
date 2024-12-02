with open("/workspaces/aoc2024/day1/input.txt", "r") as f:
    input = f.read()
input = input.split()

def main(input):
    list1 = []
    list2 = []
    occurence = 0
    mult = 0
    for i in range(len(input)):
        if i%2 == 0:
            list1.append(int(input[i]))
        elif i%2 == 1:
            list2.append(int(input[i]))
    for i in range(len(list1)):
        occurence = occur(list1[i], list2)
        mult+= list1[i] * occurence
    return mult

def occur(x, list):
    occurence = 0
    for i in range(len(list)):
        if x == list[i]:
            occurence+=1
    return occurence

print(main(input))