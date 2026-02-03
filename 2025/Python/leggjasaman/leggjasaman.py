import sys
sum = 0

values = [int(x.strip("\n")) for x in sys.stdin.readlines()]

for x in values:
    sum += x

print(sum)