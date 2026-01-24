# 🤔

numCards:int = int(input())

listCards:list[int] = [int(x) for x in input().split()]

total:int = 0

listCards.sort()

start:int = 0

for i in range (1, len(listCards)):
    if listCards[i] != listCards[i-1]+1:
        total += listCards[start]
        start = i

        if i == len(listCards)-1:
            total += listCards[len(listCards)-1]

if len(listCards) == 1:
    print(listCards[0])
else:
    print(total)
