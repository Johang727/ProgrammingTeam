import random

with open("5", "w") as randomcase:
    randomcase.write("100000\n")
    for i in range(100000):
        randomcase.write(f"{random.randint(0,1000000000)}\n")