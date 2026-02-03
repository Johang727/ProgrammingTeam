import sys

max:int = sys.maxsize 


inp:str = sys.stdin.read()

goTime:list[int] = [int(x) for x in inp.splitlines()]

part:int = goTime.pop(0) # the first line contains the number of participants

goTime.sort()

print(part, goTime, max)

"""
First bus leaves at 4, second leaves at 11

Total waiting time is 9

Do we want a greedy algorithm for this?
"""