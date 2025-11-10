import sys


inp:list[int] = [int(x.strip("\n")) for x in sys.stdin.readlines()]


numItems:int = inp.pop(0)
samsItems:dict[int, int] = {}

for i in range(numItems):
    currItem = inp.pop(0)
    samsItems[currItem] = 1

requests:int = inp.pop(0)

samsItems[0] = samsItems.get(0, 0) + 3*requests

for i in range(0, 25):
    if samsItems.get(i, 0) >= 2:
        #print(i, samsItems.get(i, 0))
        
        samsItems[i+1] = samsItems.get(i+1, 0) + (samsItems.get(i, 0) // 2)
        samsItems[i] = samsItems.get(i, 0) - ((samsItems.get(i, 0) // 2) *2)


samsOrganizedItems:list[int] = []

for key, value, in samsItems.items():
    #print(key, value)
    if value:
        samsOrganizedItems.append(key)


samsOrganizedItems.sort()

samsStringyItems:str = ""

for item in samsOrganizedItems:
    samsStringyItems += f"{item} "

print(samsStringyItems.rstrip())
