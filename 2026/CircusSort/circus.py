import sys
from math import atan2

# parse data
inp:list[str] = sys.stdin.readlines()

num_points:int = int(inp[0])

raw_coords:list[str] = inp[1].strip().split()

points:list[tuple[float, float]] = []

for i in range(1, len(raw_coords), 2):
    points.append(( float(raw_coords[i-1]), float(raw_coords[i]) ))

# seperate x intercepts to find potential start and ends

intercepts:list[tuple[float, float]] = []


for item in points:
    if item[1] == 0.0:
        intercepts.append(item)

for item in intercepts:
    points.remove(item)

circle_count:int = len(intercepts) // 2

points.sort()
intercepts.sort()

#print(intercepts)

# determine end boundaries of each circle

circles:list[list[tuple[float, float]]] = []

inter_i:int = 0

for i in range(circle_count):
    circles.append([])
    circles[i].append(intercepts[inter_i])
    circles[i].append(intercepts[inter_i+1])

    inter_i += 2


# figure out what to do with the points in the middle

for circle in circles:
    # get important points
    x_left:float = circle[0][0]
    x_right:float = circle[1][0]
    x_center:float = (x_left + x_right) / 2


    # append to list the extra points that fall in
    for extra in points:
        if extra[0] > x_left and extra[0] < x_right:
            circle.append(extra)

    # sort clockwise
    circle.sort(key=lambda p: atan2(p[1], p[0] - x_center), reverse=True)


# print final circles

for i, item in enumerate(circles): # type: ignore
    if i != 0:
        print("")

    print(f"Ring {i+1}:", end="")
    for point in item:
        print(f" ({point[0]},{point[1]})", end="") # type: ignore

