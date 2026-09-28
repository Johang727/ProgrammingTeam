 #!/usr/bin/env python3

"""
Input:
arrive, leave, other_approach

Out: yes/no if yield right of way


Sample In 1
    South West East
Sample Out 1
    Yes

Sample In 2
    South North North
Sample Out 2
    No
    
"""

import sys

inp:list[str] = sys.stdin.read().split()

directions:dict[str, int] = {
    "North":0,
    "East":1,
    "South":2,
    "West":3
}

# the input to work with 
dirs:list[int] = []

for direction in inp:
    dirs.append(directions[direction])

#print(dirs)

"""print("Negative" if (dirs[1] - dirs[0]) < 0 else "Positive")

print(dirs[1] - dirs[0])

print("Other Straight" if abs(dirs[0] - dirs[2]) == 2 else "")

print("Other Right" if abs(dirs[0] - dirs[2]) == 1 else "")

print(dirs[1] - dirs[0] > 0)

print((dirs[1] - dirs[0]) % 2)

print(dirs[1] - dirs[0] % 2 == 1)

print()

print(((dirs[1] - dirs[0]) > 0) and ((dirs[1] - dirs[0] % 2) == 1))
"""


"""
going_straight:bool = abs(dirs[0] - dirs[1]) == 2
going_left:bool = dirs[1] == (dirs[0] + 1) % 4

other_approach_right:bool = dirs[0] == (dirs[2] + 1) % 4
other_approach_straight:bool = abs(dirs[0] - dirs[2]) == 2
"""


going_straight:bool = abs(dirs[0] - dirs[1]) == 2
going_left:bool = dirs[1] == (dirs[0] + 1) % 4 #((dirs[1] - dirs[0]) > 0 and (dirs[1] - dirs[0]) % 2 == 1)

other_approach_right:bool = dirs[0] == (dirs[2] + 1) % 4 #abs(dirs[0] - dirs[2]) % 2 == 1
other_approach_straight:bool = abs(dirs[0] - dirs[2]) == 2


"""if going_straight:
    print("Going Straight")
if going_left:
    print("Going Left")"""

# If going straight and other from the right
if going_straight and other_approach_right:
    print("Yes")
elif (going_left and (other_approach_straight or other_approach_right)):
    print("Yes")
else:
    print("No")