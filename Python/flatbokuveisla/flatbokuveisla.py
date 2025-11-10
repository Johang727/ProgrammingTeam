import sys

num_slices, people = [int(x.strip("\n")) for x in sys.stdin.readlines()]

#print(num_slices, people)

# everyone gets equal num slices

communism:int = num_slices // people

leftovers:int = num_slices - (communism*people)

print(leftovers)