'''
Johang Hernandez - 07 Feb 2025

4 6 8 = 10
10 1 4 = 7

 4 2
1 5 7

Find 4th # with constant difference.
'''

# Variables

numIn = [int(n) for n in input().split()] # all numbers have to be ints

numIn.sort() # easier to work with when sorted

# print(numIn)

# find difference b/w numbers

diff_12 = numIn[1] - numIn[0]
diff_23 = numIn[2] - numIn[1]


if diff_12 == diff_23: # numbers are already in order, find 4th
    print(numIn[2] + diff_23)
else: # numbers aren't in order, find which one is off
    if diff_23 - diff_12 == diff_12: # extra number goes in-between 2 and 3
        print(numIn[1] + diff_12)
    elif diff_12 - diff_23 == diff_23: # extra number goes in-between 1 and 2
        print(numIn[0] + diff_23)
    else:
        print("what")