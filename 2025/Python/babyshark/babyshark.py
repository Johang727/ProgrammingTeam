inp:str = [x.lower() for x in input().split()]

currentConcec:int = 1

biggestConcec:int = 1

biggestWord:str = inp[0]


for i in range(1, len(inp)):
    if inp[i-1] == inp[i]:
        currentConcec += 1
    else:
        currentConcec = 1
    if currentConcec > biggestConcec:
        biggestConcec = currentConcec
        biggestWord = inp[i]


print(biggestWord)
