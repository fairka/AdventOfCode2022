def main():
    partone()
    parttwo()



def partone():
    stacks = []
    pairTxt = open('input.txt', 'r')
    listInstructions = [line.strip("\n") for line in pairTxt]
    finalIndex = 0

    for i in range(len(listInstructions)):
        stacks.append([])
        if listInstructions[i] == "":
            finalIndex = i - 1
            stacks.pop()
            break

    for i in range(finalIndex, -1, -1):
        counter = 0
        temp = listInstructions[i]

        for j in range(len(temp)):
            if (j+1) % 4 == 0:
                counter +=1
            if temp[j].isalpha():
                    stacks[counter].append(temp[j])

    for i in range(finalIndex+2, len(listInstructions)):
        temp = listInstructions[i].split()
        for j in range(int(temp[1])):
            box = stacks[int(temp[3])-1].pop()
            stacks[int(temp[5])-1].append(box)
    
    topStack = ""

    for list in stacks:
        if list:

            topStack += list[-1]
    print(topStack)
        

                    
                     
   

def parttwo():
    stacks = []
    pairTxt = open('input.txt', 'r')
    listInstructions = [line.strip("\n") for line in pairTxt]
    finalIndex = 0

    for i in range(len(listInstructions)):
        stacks.append([])
        if listInstructions[i] == "":
            finalIndex = i - 1
            stacks.pop()
            break

    for i in range(finalIndex, -1, -1):
        counter = 0
        temp = listInstructions[i]
        for j in range(len(temp)):
            if (j+1) % 4 == 0:
                counter +=1
            if temp[j].isalpha():
                    stacks[counter].append(temp[j])

    for i in range(finalIndex+2, len(listInstructions)):
        temp = listInstructions[i].split()
        for j in range(int(temp[1])-1, -1, -1):
            box = stacks[int(temp[3])-1].pop(len(stacks[int(temp[3])-1])-j-1)
            stacks[int(temp[5])-1].append(box)

    
    topStack = ""

    for list in stacks:
        if list:

            topStack += list[-1]
    print(topStack)

if __name__ == '__main__':
    main()
