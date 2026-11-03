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


for i in range(num_portals):
    #left_portal= portal_list[i][1] + 9*portal_list[i][0] - portal_list[i+1][0]
    #right_portal = portal_list[i+1][1] + portal_list[i+1][0]
    # i think these variables ^ replace the if comparisions down here -V
    if portals[i][1] + portals[i][0]*8 > portals[i+1][1] + portals[i+1][0]*8:
        portal_in = i

print(portal_in, portal_out)