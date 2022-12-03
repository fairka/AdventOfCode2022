list = []
total = 0
temp1 = []
temp2 = []
temp3 = []

with open('input.txt', 'r') as f:
    sack = [line.strip() for line in f]
    #print(sack)

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

        
        #print(temp1)
        # A = temp[:len(temp) // 2]
        # B = temp[len(temp) // 2:]

    
#         for char in A:
#             if char in B:
#                 print(char)
#                 if char.isupper():
#                     total += ord(char) - 38
#                 else:
#                     total += ord(char) - 96
#                 break
print(total)        
        