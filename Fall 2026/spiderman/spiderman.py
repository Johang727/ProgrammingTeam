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
    global moves, success, sum_moves
    """ 
    The recursive "solution" to this problem.  

    :param int current: current height
    :param int next: next move index
    :param int max_height: current maximum height
    :param str final_steps: final output string (eventually)
    :param int remaining_height: how much we can go up before no go down and spiderman dies :c

    :returns None
    """

    if current > sum_moves:
        return None
    if max_height > success[0]:
        return None
    elif current < 0:
        return None #(max_height, "IMPOSSIBLE")
    elif len(moves) == next:
        if current != 0:
            return None #(max_height, final_steps)
        else:
            success = (max_height, final_steps)
            return None
    else:
        """if current+next > max_height:
            max_height = current
            spooder(current+next, next, max_height, final_steps)"""
        if current > max_height:
            max_height = current
        
        spooder(current - moves[next], next+1, max_height, f"{final_steps}D")
        spooder(current + moves[next], next+1, max_height, f"{final_steps}U")



    return None

"""List of distances of each move"""
moves: list[int] = []
for i in range(num_cases):
    moves.clear()
    success: tuple[int, str] = (1000, "IMPOSSIBLE")
    num_distances: int = int(next(it))

    for dists in range(num_distances):
        moves.append(int(next(it)))


    sum_moves = (sum(moves) // 2)

    spooder(
        current=moves[0],
        max_height=max(moves)
        )

    #print(f"\033[31;1;4m{success[1]}\033[0m")
    print(f"{success[1]}")