"""
6 4 # num_houses, num_cables
1 2 x   
2 3
3 4
5 6

5
6

"""

import sys

sys.setrecursionlimit(100000000)

inp:list[str] = sys.stdin.read().split()
it = iter(inp)
i = lambda: int(next(it))

houses:int = i()
cables:int = i()

connections:dict[int,list[int]] = {}

houses_visted = [0]*(houses+1)

def visit_house(house:int):
    for cable in connections[house]:
        if houses_visted[cable] == 0:
            houses_visted[cable] = 1
            visit_house(cable)

for _ in range(cables):
    house1 = i()
    house2 = i()

    connections.setdefault(house1, []).append(house2)
    connections.setdefault(house2, []).append(house1)

#print(connections)

if 1 in connections.keys():
    houses_visted[1] = 1
    visit_house(1)

counter:int = 0
for x in range(2, houses + 1):
    if houses_visted[x] == 0:
        print(x)
    else:
        counter += 1

if counter == houses - 1:
    print("Connected")