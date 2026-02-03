import sys, time


start = time.time()


inp:list[int] = [int(x) for x in sys.stdin.readlines()]
myDict:dict[int, int] = {} # num citations | num papers
myList:list[int] = [] # sorted list w/o dupes.
bigNums:int = 0 # keeps track of num papers w/ biggest citations 
numLines:int = inp.pop(0) # numbers of papers you have written

backupVal:int = 0

for i in range(numLines):
    myNum:int = inp.pop(0).strip() # current working number
    if myNum not in myDict:
        myList.append(myNum)
    myDict[myNum] = myDict.get(myNum, 0) + 1

print(time.time()-start)

myList.sort(reverse=True)


for i in range(len(myList)):
    bigNums += myDict.get(myList[i], 0) # gets how many papers exist
    if(bigNums >= myList[i]): # if enough papers have these references
        if(backupVal > myList[i]):
            print(str(backupVal))
        else:
            print(myList[i]) # print it out
        break
    else:
        backupVal = bigNums
    


if bigNums < myList[len(myList) - 1]:
    print(str(bigNums))

print(time.time()-start)