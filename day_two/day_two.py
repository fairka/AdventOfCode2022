totalScore = 0
scoreTemp =0

def rockFunction(response):
    scoreTemp =0
    if(response == "X"):
        scoreTemp += 3
    elif(response == "Y"):
        scoreTemp += 4
    elif(response == "Z"):
        scoreTemp += 8
    return scoreTemp

def paperFunction(response):
    scoreTemp =0
    if(response == "X"):
        scoreTemp += 1
    elif(response == "Y"):
        scoreTemp += 5
    elif(response == "Z"):
        scoreTemp += 9
    return scoreTemp

def scissorFunction(response):
    scoreTemp =0
    if(response == "X"):
        scoreTemp += 2
    elif(response == "Y"):
        scoreTemp += 6
    elif(response == "Z"):
        scoreTemp += 7
    return scoreTemp

roundsTxt = open('input.txt', 'r')
listRounds = [line.strip() for line in roundsTxt]

for eachGame in listRounds:
    if(eachGame[0] == "A"):
        scoreTemp += rockFunction(eachGame[2])
    elif(eachGame[0] == "B"):
        scoreTemp += paperFunction(eachGame[2])
    elif(eachGame[0] == "C"):
        scoreTemp += scissorFunction(eachGame[2])
    totalScore += scoreTemp
    scoreTemp = 0

print (totalScore)