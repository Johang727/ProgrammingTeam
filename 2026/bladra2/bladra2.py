import sys

inp:list[str] = sys.stdin.read().split()
it = iter(inp)
i = lambda: int(next(it))

v = i(); a = i(); t = i()

print(v*t + (.5*a*(t**2)))