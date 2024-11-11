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