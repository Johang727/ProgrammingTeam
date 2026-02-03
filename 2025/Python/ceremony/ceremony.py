"""
laser modes:
horizontal = 1 floor at a time
vertical = one tower at a time
"""
from collections import Counter

amount:int = int(input())
buildings:list[int] = [int(x) for x in input().split()]

phoneBook:dict[int,int] = Counter(buildings)


best:int = amount # we can always solve it with only vertical blasts, however.. we wanna minimize it

x:int = 0

#print(f"Number of Buildings: {amount}\n\n")

for h in sorted(phoneBook.keys()):
    #print(f"Current Best = {best}\nX = {x}\nCurrent Building Consideration = {h}\n")
    x += phoneBook[h]
    best = min(best, h+amount-x)

print(best)




""" Attempt #1 | time limit exceeded
amount:int = int(input())
buildings:list[int] = [int(x) for x in input().split()]

buildings.sort()

#print(buildings)

passes:int = 0

def laserHorizontal() -> None:
    # remove 1 from all
    global buildings
    buildings = [x-1 if x !=0 else x for x in buildings]
    

def laserVertical(i:int) -> None:
    global amount, buildings
    buildings.pop(i)
    amount-=1



for i in range(0, amount*2):
    passes+=1
    print(f"Current State: {buildings}\nPass {passes}")


    if buildings.count(1)+buildings.count(2) > 1:
        laserHorizontal()
    else:
        #destroy the tallest one
        laserVertical(amount-1)
    
    if buildings == [0]*amount:
        break

print(f"End State: {buildings} in {passes} Passes") # more readable format

print(passes) # expected output
"""