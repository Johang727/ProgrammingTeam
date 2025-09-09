"""
laser modes:
horizontal = 1 floor at a time
vertical = one tower at a time
"""

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

"""def drawBuildings() -> None:
    highest:int = buildings[amount]"""


while True:
    passes+=1
    print(f"Current State: {buildings}\nPass {passes}")


    if buildings.count(1)+buildings.count(2) > 1:
        laserHorizontal()
    else:
        #destroy the tallest one
        laserVertical(amount-1)
    
    if buildings == [0]*amount:
        break

print(f"End State: {buildings} in {passes} Passes")

#print(passes)