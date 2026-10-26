#!/usr/bin/python

"""
Input:
20 4 total_obs mario_found 
5  # obs found
10
12
16

Output
0
1
2
3
4
6
7
8
9
11
13
14
15
17
18
19
Mario got 4 of the dangerous obstacles.

"""

import sys

inp = sys.stdin.read().split()
it = iter(inp)

total_obs:int = int(next(it))
mario_found:int = int(next(it))

mario_dictionary:dict[int,int] = {}


for _ in range(mario_found):
    current_obs:int = int(next(it))
    mario_dictionary[current_obs] = mario_dictionary.get(current_obs, 0) + 1

#print(mario_dictionary)

for i in range(total_obs):
    if i not in mario_dictionary.keys():
        print(i)

print(f"Mario got {len(mario_dictionary)} of the dangerous obstacles.")