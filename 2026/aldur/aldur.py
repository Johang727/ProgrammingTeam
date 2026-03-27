import sys

inp:list[str] = sys.stdin.read().split()

it = iter(inp)

friends = []

for _ in range(int(next(it))):
    friends.append(int(next(it)))
    
print(min(friends))