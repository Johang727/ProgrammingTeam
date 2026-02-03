import sys

"""
Sample in 0:

4
-1 1 -1 2
9 -1 -1 -1
-1 3 -1 4
7 1 2 -1

First line = num cities

Lines after first: 

-1: no direct flights
other: cost of flight


Sample out 0:
8
1 2 1
1 4 2
2 1 9
3 2 3
3 4 4
4 1 7
4 2 1
4 3 2

m = number of direct flights

uvc

u = depart city
v = landing city
c = cost



"""

inp:str = sys.stdin.read()

flights:list[list[int]] = [[int(y) for y in x.split()] for x in inp.splitlines()]

flights.pop(0)

final:list[str] = []



#print(flights)

for dep, city in enumerate(flights):
    for dest, cost in enumerate(city):
        if cost != -1:
            final.append(f"{dep+1} {dest+1} {cost}")


print(len(final))

for x in final:
    print(x)