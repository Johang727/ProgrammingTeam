#!/usr/bin/python
"""

N S: N = # of portals, S = stronghold pos
xi ti: xi = position of portal i in nether, ti: time to repair and enter portal i 

KATTIS_3 Input
5 41
1 20 
2 5 
3 1
4 5
5 20

"""


"""Input handling. Turns the input into a list of strings without whitespace."""
import sys
inp = sys.stdin.read().split()
it = iter(inp)
next_int = lambda: int(next(it))

"""Parse the first line into variables"""
num_portals:int = next_int()
stronghold_position:int = next_int()

"""A list of tuples containing the (position, time to repair) of each portal."""
portals:list[ tuple[int, int] ] = []
for _ in range(num_portals):
    portal:tuple[int, int] = (next_int(), next_int())
    portals.append(portal)


portal_in:int = -1 # Portal you enter ?
portal_out:int = -1 # Portal you leave ?


time_nether: list[int] = []
time_overworld: list[int] = []

for i in range(num_portals):
    time_in_nether: int = (8*portals[i][0]) + portals[i][1] + (stronghold_position//8) - portals[i][0]

    time_nether.append(time_in_nether)

    time_in_overworld: int = portals[i][0] + portals[i][1] + stronghold_position - 8*portals[i][0]

    time_overworld.append(time_in_overworld)

"""time = 8x1 ... what mean ?"""

