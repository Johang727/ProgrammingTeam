#!/usr/bin/python

import random

with open("./in/WORST", "w") as new_file:
    new_file.write("101\n")

    for i in range(101):
        new_file.write("40\n")
        for j in range(40):
            new_file.write(f"{random.randint(0, 25)} ")
        new_file.write("\n")