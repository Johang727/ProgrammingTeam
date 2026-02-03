"""
Sample input: 4 (length of a new plank or n)
Expected out: 7

Output a single integer: the number of ways you can glue together a plank of length n meters using 1, 2, 3 meter planks.

The planks are 2x4s.
"""

numWays:int = 0

def walkThePlank(length:int) -> None:
    global numWays
    if length >= 3:
        walkThePlank(length-3)
    if length >= 2:
        walkThePlank(length-2)
    if length >= 1:
        walkThePlank(length-1)
    if length == 0:
        numWays += 1

length = int(input())

walkThePlank(length)

print(numWays)
x