def main():
    partone()
    parttwo()



def partone():
    count = 0
    pairTxt = open('input.txt', 'r')
    listpairs = [line.strip() for line in pairTxt]

    for eachLine in listpairs:
        x = eachLine.split(',')
        y = x[0].split('-')
        z = x[1].split('-')
        print(y)
        print(z)


        if int(y[0]) >= int(z[0]) and int(y[1]) <= int(z[1]) or int(z[0]) >= int(y[0]) and int(z[1]) <= int(y[1]):
            count +=1
    print(count)

def parttwo():
    count = 0
    pairTxt = open('input.txt', 'r')
    listpairs = [line.strip() for line in pairTxt]

    for eachLine in listpairs:
        x = eachLine.split(',')
        y = x[0].split('-')
        z = x[1].split('-')
        print(y)
        print(z)


        if int(y[0]) >= int(z[0]) and int(y[0]) <= int(z[1]) or int(z[0]) >= int(y[0]) and int(z[0]) <= int(y[1]):
            count +=1
    print(count)

if __name__ == '__main__':
    main()
