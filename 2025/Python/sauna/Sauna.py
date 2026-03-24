"""
Sample Input:
3
70000 70005
70003 70010
65000 80000

Input:

N = number friends

Sample Out:
3 70003

Output:

N = number of temperatures
T = the lowest temperature
"""


import sys

inp:list[str] = sys.stdin.read().split()

it = iter(inp)

friends:int = int(next(it))

min_temp = 0
max_temp = float("inf")

for _ in range(friends):


    curr = int(next(it))
    if min_temp < curr:
        min_temp = curr

    curr = int(next(it))
    if curr < max_temp:
        max_temp = curr

if max_temp - min_temp < 0:
    print("bad news")
else:
    print(f"{max_temp - min_temp +1} {min_temp}")

#print(min_temp, max_temp)

