def main():
    part1()
    part2()
    

def part1():
    total = 0

    with open('input.txt', 'r') as f:
        sack = [line.strip() for line in f]
        for rucksack in sack:
            temp = [x for x in rucksack]
            A = temp[:len(temp) // 2]
            B = temp[len(temp) // 2:]

        
            for char in A:
                if char in B:
                    if char.isupper():
                        total += ord(char) - 38
                    else:
                        total += ord(char) - 96
                    break
    print (total)

def part2():
    total = 0
    temp1 = []
    temp2 = []
    temp3 = []
    with open('input.txt', 'r') as f:
        sack = [line.strip() for line in f]

        for i in range(len(sack)):
            if (i+1) % 3 == 0:
                temp1 = [x for x in sack[i-2]]
                temp2 = [x for x in sack[i-1]]
                temp3= [x for x in sack[i]]
                for char in temp1:
                    if char in temp2 and char in temp3:
                        if char.isupper():
                            total += ord(char) - 38
                        else:
                            total += ord(char) - 96
                        break
    print(total) 

if __name__ == '__main__':
    main()
