#!/usr/bin/env python

"""
Input: 

t: test cases
n m: number of dominos, number of lines
x y: if x falls, y falls

Output:
n: number of manual pushes

1
3 2
1 2
2 3

outputs 1
"""


import sys;

inp:list[str] = sys.stdin.read().split();

it = iter(inp);

cases:int = int(next(it));
dominos:int = int(next(it));
collisions:int = int(next(it));


print(f"""Cases: {cases}
Dominos: {dominos}
Collisions: {collisions}""");


colls:dict[int,list[int]] = {};

for _ in range(collisions):
    domino:int = int(next(it));
    target:int = int(next(it));

    colls.setdefault(domino, []).append(target);

print(colls);


# i think tj's computer works now
# si senor
# aye aye captain