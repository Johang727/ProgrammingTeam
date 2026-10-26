#!/usr/bin/python

import random

num_cases:int = 1024

with open("./in/WORST", "w") as new_file:
    for _ in range(num_cases):
        # S
        new_file.write(f"{random.randint(1, 100)} ")
        # x
        new_file.write(f"{random.randint(0, 10000000)} ")
        # y
        new_file.write(f"{random.randint(0, 10000000)} ")
        # dx
        new_file.write(f"{random.randint(1, 20)} ")
        # dy
        new_file.write(f"{random.randint(1, 20)}\n")
    new_file.write(f"0 0 0 0 0")
