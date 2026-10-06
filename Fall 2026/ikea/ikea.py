#!/usr/bin/env python3

"""
Case 1:

In:
2
2
EKET 123
VINTERFINT 234

Out:
123
EKET
"""

import sys

inp:list[str] = sys.stdin.read().split()
it = iter(inp)

# (weight, item_name)
weights:list[tuple[int,str, int]] = []

num_people:int = int(next(it))
num_items:int = int(next(it))

for i in range(num_items):
    item:str = next(it)
    weight:int = int(next(it))

    weights.append((weight, item, i))

# divide by earliest
weights.sort(key=lambda t: (t[0], t[2]))

"""minimum amount of items they need to carry"""
min_items:int = num_items // num_people

light_items_weight:int = 0
heavy_items_weight:int = 0


if (num_items % num_people) == 0:
    for i in range(min_items):
        light_items_weight += weights[i][0]
        #print(f"Current Weight: {light_items_weight}")
else:
    for i in range(min_items + 1):
        light_items_weight += weights[i][0]
        #print(f"Current Weight: {light_items_weight}")
        #print(f"Added {weights[i][1]} to Light Items")
    for i in range(min_items + 1, min_items*2 +1):
        heavy_items_weight += weights[i][0]
        #print(f"Current Weight: {light_items_weight}")
        #print(f"Current Weight (Heavy): {heavy_items_weight}")

        #print(f"Added {weights[i][1]} to Heavy Items")

    if light_items_weight < heavy_items_weight:
        min_items += 1
    else:
        # remove the lightest heavy item
        #print("Remove the lightest heavy item.")
        #print(f"Current Weight: {light_items_weight}")
        light_items_weight -= weights[min_items][0]
        #print(f"Current Weight: {light_items_weight}")

print(light_items_weight)
carried_items:list[tuple[int,str, int]] = weights[:min_items]
carried_items.sort(key=lambda t: t[1])

for _, item, _ in carried_items:
    print(item)