"""
3 4 # num ints - num queries
2+3*4 # initial
s 1 2 # num_q moves
a
f 2
a
"""

# will have to do running modulo, rather than in place bc hits int limit

import sys

inp:list[str] = sys.stdin.read().strip().split()
it = iter(inp)

n = lambda: next(it)

num_ints:int = int(n())
num_q:int = int(n())

eq = list(n())

print(eval("".join(eq)))

trans = str.maketrans({"*":"+", "+":"*"})


for _ in range(num_q):
    match n():
        case "s":
            # swap num i and num j
            i:int = int(n())
            j:int = int(n())

            #print(j)
            x:str = eq[(i-1)*2]
            y:str = eq[(j-1)*2]

            eq[(i-1)*2] = y
            eq[(j-1)*2] = x
            

            #print(eq)

            print(eval("".join(eq)) % 1000000007)

        case "a":
            str_eq = "".join(eq)
            str_eq = str_eq.translate(trans)
            
            print(eval(str_eq) % 1000000007)
            eq = list(str_eq)

        case "f":
            i = int(n())
            eq[(i-1)*2 + 1] = eq[(i-1)*2 + 1].translate(trans)
            print(eval("".join(eq)) % 1000000007)


