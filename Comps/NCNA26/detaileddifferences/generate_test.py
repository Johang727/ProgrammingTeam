#!/usr/bin/python
import random
import string


num_cases:int = 500

with open("./in/gen_1", "w") as new_file:
    new_file.write("3\n")
    new_file.write(f'{"A"*50}\n')
    new_file.write(f'{"B"*50}\n')
    new_file.write(f'{"B"*50}\n')
    new_file.write(f'{"B"*50}\n')

with open("./in/gen_2", "w") as new_file:
    new_file.write(f"{num_cases}\n")
    for _ in range(num_cases//2):
        # word1
        for _ in range(50):
            new_file.write(random.choice(string.ascii_letters))
        new_file.write("\n")
        # word2
        for _ in range(50):
            new_file.write(random.choice(string.ascii_letters))
        new_file.write("\n")
        # word3
        for _ in range(50):
            new_file.write(str(random.randint(0, 9)))
        new_file.write("\n")

        for _ in range(50):
            new_file.write(str(random.randint(0, 9)))
        new_file.write("\n")




