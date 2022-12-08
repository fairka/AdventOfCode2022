def main():
    partone()
    parttwo()

def partone():
    pairTxt = open('input.txt', 'r')
    Lines = [line.strip() for line in pairTxt]
    outer = []
    seen = 0
    for line in Lines:
        outer.append(list(line))
    
    for row in range(len(outer)):
        for col in range(len(outer[row])):
            visible = 4
            for a in range(col):
                if outer[row][a] >=  outer[row][col]:
                    visible -= 1
                    break
            for b in range(col+1, len(outer[row])):
                if outer[row][b] >= outer[row][col]:
                    visible -= 1
                    break
            for c in range(row):
                if outer[c][col] >= outer[row][col]:
                    visible -= 1
                    break
            for d in range(row+1,len(outer)):
                if outer[d][col] >= outer[row][col]:
                    visible -= 1
                    break
            if visible != 0:
                seen +=1
    print(seen)
            

        

def parttwo():
    pairTxt = open('input.txt', 'r')
    Lines = [line.strip() for line in pairTxt]
    outer = []
    best = 0
    for line in Lines:
        outer.append(list(line))
    
    for row in range(len(outer)):
        for col in range(len(outer[row])):
            scenic = [0,0,0,0]
            for a in range(col-1, -1, -1):
                if outer[row][a] >=  outer[row][col]:
                    scenic[0] = (col-a)
                    break
                scenic[0] =(col)
            for b in range(col+1, len(outer[row])):
                if outer[row][b] >= outer[row][col]:
                    scenic[1] = (b - col)
                    break
                scenic[1] = (len(outer[row])-1 - col)
            for c in range(row-1,-1,-1):
                if outer[c][col] >= outer[row][col]:
                    scenic[2] = (row-c)
                    break
                scenic[2] = (row)
            for d in range(row+1,len(outer)):
                if outer[d][col] >= outer[row][col]:
                    scenic[3] = (d - row)
                    break
                scenic[3] = (len(outer)-1 - row)
            
            score = int(scenic[0]) * int(scenic[1]) * int(scenic[2]) * int(scenic[3])
            if score > best:
                best = score
    print(best)

if __name__ == '__main__':
    main()
