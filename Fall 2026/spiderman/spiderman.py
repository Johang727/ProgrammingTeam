#!/usr/bin/env python3

"""
3 : number of test cases
4 : num distances
20 20 20 20 : distances
6 : num distances
3 2 5 3 1 2 : distances
7 : num distances
3 4 2 1 6 4 5 : distances

"""

import sys

sys.setrecursionlimit(1000000000)

inp: list[str] = sys.stdin.read().split()
it = iter(inp)

num_cases: int = int(next(it))

def spooder(current: int, next: int, max_height: int=0, final_steps: str=""):
    """
    
    """
    if current < 0:
        return (max_height, "IMPOSSIBLE")
    elif not next:
        if current == 0:
            return (max_height, final_steps)
    else:
        if current+next > max_height:
            max_height = current
            spooder(current+next, next, max_height, final_steps)

 