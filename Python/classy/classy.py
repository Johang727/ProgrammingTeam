classNums = {"upper":1, "middle":2, "lower":3}


numCases = int(input())

for i in range(numCases):
    people = []
    numPeople = int(input())
    for j in range(numPeople):
        inp = input().split()
        classes = inp[1].split('-')
        name = inp[0][:-1]
        classesButBetter = [classNums[x] for x in classes]
        
        while len(classesButBetter) < 10:
            classesButBetter.insert(0, 2)
        classesButBetter.reverse()

        stringyList = ''.join(str(classesButBetter))

        people.append((stringyList, name))

    people.sort()
    for item in people:
        print(item[1])
    print("==============================")
