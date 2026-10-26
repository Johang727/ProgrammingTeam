#!/usr/bin/python

import random

num_cases:int = 101
moves_per_case:int = 40

lower_limit:int = 1
upper_limit:int = 25

with open("./in/WORST", "w") as new_file:
    new_file.write(f"{num_cases}\n")

    for i in range(num_cases):
        new_file.write(f"{moves_per_case}\n")
        for j in range(moves_per_case):
            new_file.write(f"{random.randint(lower_limit, upper_limit)} ")
        new_file.write("\n")