import sys

inp:list[str] = [x.strip("\n") for x in sys.stdin.readlines()]

total:int = 0

user_intervals, min_users = [int(x) for x in inp.pop(0).split()]


intervals:dict[float, int] = {}

#print(user_intervals); print(min_users); print(inp)


while inp:
    start, end = [int(x) for x in inp.pop(0).split()]

    for i in range(start, end):
        intervals[i+0.5] = intervals.get(i+0.5, 0) + 1

for values in intervals.values():
    if values >= min_users:
        total += 1

print(total)
