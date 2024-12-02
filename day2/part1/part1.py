with open("/workspaces/aoc2024/day2/input.txt", "r") as f:
    input = f.read()
input = input.split("\n")

def main(input):
    tab = []
    tabtemp = []
    safe = 0
    val = 0
    #Création du tableau de tableau
    for i in range(len(input)):
        tabtemp = input[i].split(" ")
        for i in range(len(tabtemp)):
            tabtemp[i] = int(tabtemp[i])
        tab.append(tabtemp)
    safe = len(tab)

    #Vérification de la sécurité
    for i in range(len(tab)):
        if tab[i][0] > tab[i][1]:
            for j in range(len(tab[i])-1):
                val = abs(tab[i][j]-tab[i][j+1])
                if tab[i][j] < tab[i][j+1] or val < 1 or val > 3:
                    safe -= 1
                    break
        elif tab[i][0] < tab[i][1]:
            for j in range(len(tab[i])-1):
                val = abs(tab[i][j]-tab[i][j+1])
                if tab[i][j] > tab[i][j+1] or val < 1 or val > 3:
                    safe -= 1
                    break
    return safe
    
print(main(input))