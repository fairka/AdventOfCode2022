def main():
    partone()
    parttwo()

def partone():
    temp = []
    total = 0
    pairTxt = open('input.txt', 'r')
    stringtemp = ""
    for line in pairTxt:
        buffer = line.strip('\n')
    
    for i in range(len(buffer)):
        stringtemp += buffer[i]
        if buffer[i] not in temp:
            if len(temp) == 3:
                total = i
                break
            temp.append(buffer[i])
        else:
            temp.append(buffer[i])
            x = temp.index(buffer[i])
            for i in range(x+1):
                temp.pop(0)
   
    print(total+1)



def parttwo():
    temp = []
    total = 0
    pairTxt = open('input.txt', 'r')
    stringtemp = ""
    for line in pairTxt:
        buffer = line.strip('\n')
    
    for i in range(len(buffer)):
        stringtemp += buffer[i]
        if buffer[i] not in temp:
            if len(temp) == 13:
                total = i
                break
            temp.append(buffer[i])
        else:
            temp.append(buffer[i])
            x = temp.index(buffer[i])
            for i in range(x+1):
                temp.pop(0)  
    print(total+1)
 


if __name__ == '__main__':
    main()
