elfMax = 0
elfTemp = 0
topThree = []


# with open('input.txt', 'r') as f:
#     elvesList = [line.strip() for line in f]
#     for eachItem in elvesList:
#         if(eachItem != ''):
#             elfTemp += int(eachItem)

#         else:
#             if elfTemp > elfMax:
#                 elfMax = elfTemp
#             print(topThree)
#             if (len(topThree) < 3):
#                 topThree.append(elfMax)
#                 topThree = sorted(topThree)
#             if (len(topThree) == 3):
#                 topThree = sorted(topThree)
#                 for eachElf in range(0, len(topThree)):
#                     if (elfTemp > topThree[eachElf]):
#                         topThree[eachElf] = elfTemp
#                         break
#             elfTemp = 0

elvesTxt = open('input.txt', 'r')

elvesList = [line.strip() for line in elvesTxt]
for eachItem in elvesList:
    if(eachItem != ''):
        elfTemp += int(eachItem)
    
    else:
        if elfTemp > elfMax:
            elfMax = elfTemp
        if (len(topThree) < 3):
            topThree.append(elfMax)
            topThree = sorted(topThree)
        if (len(topThree) == 3):
            topThree = sorted(topThree)
            for eachElf in range(0, len(topThree)):
                if(elfTemp > topThree[eachElf]):
                    topThree[eachElf] = elfTemp
                    break
        elfTemp = 0


print(sum(topThree))
print (elfMax)    
