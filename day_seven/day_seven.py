def main():
    partone()
    parttwo()

def partone():
    path = ""
    size = 0
    files = {}
    currDirTotalSize = 0
    pairTxt = open('input.txt', 'r')
    commandList = [line.strip() for line in pairTxt]
    for line in commandList:
        if line != "$ cd ..":
            if line[0:4] == "$ cd":
                if path == "":
                    path = "/"
                elif path != "/":
                    path += "/" + line[5:]
                else:
                    path += line[5:]
                files[path] = 0
            if line[0].isnumeric():
                temp = line.split(" ")
                files[path] += int(temp[0])
            if line == commandList[len(commandList)-1]:
                temp = path.rfind("/")
                if temp == 0:
                    newPath= "/"
                else:
                    newPath = path[0:temp]
                currDirTotalSize = files[path]
                path = newPath
                files[path] += currDirTotalSize
        else:
            temp = path.rfind("/")
            if temp == 0:
                newPath= "/"
            else:
                newPath = path[0:temp]
            currDirTotalSize = files[path]
            path = newPath
            files[path] += currDirTotalSize
    while path != "/":
        temp = path.rfind("/")
        if temp == 0:
            newPath= "/"
        else:
            newPath = path[0:temp]
        currDirTotalSize = files[path]
        path = newPath
        files[path] += currDirTotalSize

    for key in files:
        if files[key] <= 100000:
            size += files[key]
    print(size)

        

def parttwo():
    path = ""
    size = 0
    files = {}
    currDirTotalSize = 0
    pairTxt = open('input.txt', 'r')
    commandList = [line.strip() for line in pairTxt]
    for line in commandList:
        if line != "$ cd ..":
            if line[0:4] == "$ cd":
                if path == "":
                    path = "/"
                elif path != "/":
                    path += "/" + line[5:]
                else:
                    path += line[5:]
                files[path] = 0
            if line[0].isnumeric():
                temp = line.split(" ")
                files[path] += int(temp[0])
            if line == commandList[len(commandList)-1]:
                temp = path.rfind("/")
                if temp == 0:
                    newPath= "/"
                else:
                    newPath = path[0:temp]
                currDirTotalSize = files[path]
                path = newPath
                files[path] += currDirTotalSize
        else:
            temp = path.rfind("/")
            if temp == 0:
                newPath= "/"
            else:
                newPath = path[0:temp]
            currDirTotalSize = files[path]
            path = newPath
            files[path] += currDirTotalSize
    while path != "/":
        temp = path.rfind("/")
        if temp == 0:
            newPath= "/"
        else:
            newPath = path[0:temp]
        currDirTotalSize = files[path]
        path = newPath
        files[path] += currDirTotalSize

    best = 70000000
    for key in files:
        if key == "/":
            continue
        temp = files["/"] - files[key]
        if temp <= 40000000:
            if files[key] < best:
                best = files[key]
    print(best)

if __name__ == '__main__':
    main()
