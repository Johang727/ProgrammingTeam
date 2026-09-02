import sys

inp:list[int] = [int(x.strip("\n")) for x in sys.stdin.readlines()]

a:int = int(inp[0])
b:int = int(inp[1])
c:int = int(inp[2])


lowest:int = min(a, b, c)
lowest_idx:int = inp.index(lowest)

if lowest_idx == 0:
    print("Monnei")
elif lowest_idx == 1:
    print("Fjee")
else:
    print("Dolladollabilljoll")