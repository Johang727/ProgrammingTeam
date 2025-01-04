# Created by TJ and Johang
""" Attempt 1 - Too Slow
goodDict = {}
ins = int(input())
for i in range(ins):
    newIn = input().split()
    for j in range(int(newIn[0]), int(newIn[1])):
        goodDict[j] = goodDict.get(j, 0) + 1

goodVal = []

for i in goodDict:
    if goodDict[i] == ins:
        goodVal.append(i)

goodVal.sort()

if len(goodVal) == 0:
    print("bad news")
else:
    print(f"{ins} {goodVal[0]}")
"""

""" Attempt 2 - Wrong Answer #4
inp = int(input())
smallList = []
bigList = []
for i in range(inp):
    newIn = input().split()
    smallList.append(int(newIn[0]))
    bigList.append(int(newIn[1]))

smallList.sort()
smallList.reverse()
bigList.sort()

#print(smallList)

valueW = bigList[0] - smallList[0] + 1

if valueW > 0:
    print(f"{inp} {smallList[0]}")
else:
    print("bad news")
"""
