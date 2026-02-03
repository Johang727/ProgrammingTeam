import sys

inp = [sorted([int(x) for x in line.strip().split()]) for line in sys.stdin.readlines]

print(inp)