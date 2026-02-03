import sys

inp = [x.strip('\n') for x in sys.stdin.readlines()[1:]]

[print(f"Takk {x}") for x in inp]
