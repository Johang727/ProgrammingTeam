"""
Input 1 
5 3 ; init_seats num_events
1 1 ; the events: 1: visitor wants to sit at i
1 3
1 3

Ledig ; avaliable
Ledig
Upptagen ; not avaliable

"""

import sys

inp = sys.stdin.read().split()
it = iter(inp)
next_int = lambda: int(next(it))

init_seats:int = next_int()
num_events:int = next_int()

"""int: seat number, bool: if occupied"""
seats:dict[int, bool] = {}

for _ in range(num_events):
    switch:int = next_int()
    if switch == 1:
        seat:int = next_int()
        if not seats.get(seat, False):
            seats[seat] = True
            print("Ledig")
        else:
            print("Upptagen")

    if switch == 2:
        curr_seat:int = next_int()
        desired_seat:int = next_int()

        if not seats.get(desired_seat, False):
            """Desired seat is open"""
            seats[curr_seat] = False
            seats[desired_seat] = True
            print("Ledig")
        else:
            print("Upptagen")
