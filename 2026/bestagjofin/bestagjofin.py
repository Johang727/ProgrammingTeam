import sys

inp:list[str] = sys.stdin.read().split()

it = iter(inp)

gifts:int = int(next(it))

curr_max = 0
best_friend = "nobody :c"

for _ in range(gifts):
    curr_friend = next(it)
    curr_cool = int(next(it))

    if curr_cool > curr_max:
        best_friend = curr_friend
        curr_max = curr_cool

print(best_friend)