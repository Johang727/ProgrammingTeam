'''input

1
5
mom: upper-upper-lower-middle class
dad: middle-middle-middle-lower-middle class
queenelizabeth: upper-upper-upper class
chair: lower-lower class
unclebob: middle-middle-lower-middle class

'''

classNums = {"upper":1, "middle":2, "lower":3}


numCases = int(input())

for i in range(numCases):
    peopleList = []
    numPeople = int(input())
    for j in range(numPeople):
        inp = input().split(); #print(inp)
        classes = inp[1].split('-'); #print(classes)
        name = inp[0][:-1]
        classesButBetter = [classNums[x] for x in classes]; #print(classesButBetter)
        #peopleDict[name] = classesButBetter
        
        while len(classesButBetter) < 10:
            classesButBetter.insert(0, 2)
        classesButBetter.reverse()

        stringyList = ''.join(str(classesButBetter))

        peopleList.append((stringyList, name))


        
    peopleList.sort()
    for item in peopleList:
        print(item[1])
    print("==============================")


#print(peopleDict)
#print(peopleList)
"""for item in peopleList:
    print(item)

peopleList.sort()
print("\n after sort \n")
for item in peopleList:
    print(item)
#print(maxVal)"""

