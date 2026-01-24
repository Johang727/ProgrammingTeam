import sys
""" test in 1
2 - number of cases
3 - number of clothing items
hat headgear
sunglasses eyewear
turban headgear
3 - number of clothing items
mask face
sunglasses face
makeup face
"""

file:list[str] = [x.strip("\n") for x in sys.stdin.readlines()]

for i in range(int(file[0])): # should be num cases
    pass