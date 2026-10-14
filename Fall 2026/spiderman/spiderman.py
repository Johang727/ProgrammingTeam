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

def spooder(current: int, next: int=1, max_height: int=0, final_steps: str="U") -> None:
    global moves, successes
    """
    The recursive "solution" to this problem.  

    :param int current: current height
    :param int next: next move index
    :param int max_height: current maximum height
    :param str final_steps: final output string (eventually)

    :returns tuple[0]: max height reached
    :returns tuple[1]: the final string of steps to take
    """
    if max_height > 1000:
        return None
    if current < 0:
        return None #(max_height, "IMPOSSIBLE")
    elif len(moves) == next:
        if current != 0:
            return None #(max_height, final_steps)
        else:
            successes.append( (max_height, final_steps) )
            return None
    else:
        """if current+next > max_height:
            max_height = current
            spooder(current+next, next, max_height, final_steps)"""
        if current > max_height:
            max_height = current
        spooder(current + moves[next], next+1, max_height, f"{final_steps}U")
        spooder(current - moves[next], next+1, max_height, f"{final_steps}D")


    return None

moves: list[int] = []
successes: list[tuple[int, str]] = []
for i in range(num_cases):
    print(f"Case {i+1}")
    moves.clear()
    successes.clear()
    num_distances: int = int(next(it))

    for dists in range(num_distances):
        moves.append(int(next(it)))

    spooder(
        current=moves[0],
        max_height=max(moves)
        )

    successes.sort()
    if successes:
        print(successes[0][1])
    else:
        print("IMPOSSIBLE")