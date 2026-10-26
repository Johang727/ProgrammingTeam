#!/usr/bin/python

"""
0,0 is black
boundary between two squares then it does not count as landing on the white square
;side_of_square, (start_pos xy), (jump_dis xy)
10 2 3 3 2 
100 49 73 214 38
25 0 0 5 25 - impossible
407 1270 1323 1 1
18 72 6 18 6 - impossible
407 1270 1170 100 114
0 0 0 0 0
"""

import sys, time

inp = sys.stdin.readlines()


def in_black(tile_size:int, x, y) -> bool:
    #print()
    #print((x, y))
    if (x % tile_size) == 0: 
        #print("x is on a border")
        #time.sleep(1)
        return True
    if (y % tile_size) == 0: 
        #print("y is on a border")
        #time.sleep(1)
        return True
    
    if ((x // tile_size) == (y // tile_size)):
        #print("On diagonal blk")
        return True

    if ((x // tile_size) % 2) != 0:
        #print("x is on a white")
        return False
    if ((y // tile_size) % 2) != 0:
        #print("y is on a white")
        return False
    
    #print("No cases, so white ig")
    return False

for line in inp:
    #print("\n\nNew Case!!!")
    line = line.strip() # remove newline escape char
    it = iter(line.split())

    tile_size:int = int(next(it))

    start_x:int = int(next(it))
    start_y:int = int(next(it))

    hop_x:int = int(next(it))
    hop_y:int = int(next(it))


    # end of program
    if tile_size == 0:
        exit(0)


    # start x is effectively 0
    if (start_x % tile_size) == 0:
        # jump x will always land on border
        if (hop_x % tile_size) == 0:
            print("The flea cannot escape from black squares.")
            continue
    # start y is effectively 0
    if (start_y % tile_size) == 0:
        # jump y will always land on border
        if (hop_y % tile_size) == 0:
            print("The flea cannot escape from black squares.")
            continue

    if in_black(tile_size, start_x, start_y):
        if (hop_x % tile_size) == 0:
            if (hop_x // tile_size) % 2 == 0:
                print("The flea cannot escape from black squares.")
                continue
        if (hop_y % tile_size) == 0:
            if (hop_y // tile_size) % 2 == 0:
                print("The flea cannot escape from black squares.")
                continue

    num_hops:int = 0
    while True:
        #print(num_hops)
        if in_black(tile_size, start_x, start_y):
            start_x += hop_x
            start_y += hop_y
            num_hops += 1
        else:
            # we should be in white?
            print(f"After {num_hops} jumps the flea lands at ({start_x}, {start_y}).")
            break