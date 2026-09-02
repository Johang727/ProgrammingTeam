"""
Input 0:
1 4 | map_rows map_cols
1100 | len = c chars | map
2 | n = num_queries
1 1 1 4 | row1 col1, row2 col2 = can move between these?
1 1 1 1 | same

Expected Ans: 
neither
decimal

Binary stay in places marked 0
Decimal stay in places marked 1

"""

import sys

sys.setrecursionlimit(214483647)

inp:list[str] = sys.stdin.readlines()

#print(f"input: {inp}")

map_rows, map_cols = [int(x) for x in inp.pop(0).split()]

#print(f"map rows: {map_rows}")

#print(f"map cols: {map_cols}")

# convert to 2D array
map = [[c for c in inp[r].strip()] for r in range(int(map_rows))] 

#print(f"map: {map}")

num_queries:int = int(inp[map_rows])

#print(f"queries: {num_queries}")

"""
[110011]

{0:1, 1:0, 2:1}
[001122]
"""

def mark_map(bd:str, row:int, col:int) -> None:
    global map, r1, r2, c1, c2
    # bd stands for "binary or decimal"
    if row >= 0 and col >= 0 and row < len(map) and col < len(map[row]):
        if map[row][col] == bd:
            map[row][col] = "M"
            if not(row == r2 and col == c2):
                mark_map(bd, row-1, col); mark_map(bd, row, col+1); mark_map(bd, row+1, col); mark_map(bd, row, col-1)
            else:
                return

def check_map() -> str:
    global map, og_map, r1, r2, c1, c2
    map = [row[:] for row in og_map]

    if map[r2][c2] == "0":
        #print(f"\nbin test for: {map}")
        # check for binary
        mark_map("0", r1, c1)

        #print(f"bin test after for: {map}")

        if map[r2][c2] == "M":
            return "binary"


    if map[r2][c2] == "1":

        map = [row[:] for row in og_map]

        #print(f"\ndec test for: {map}")

        # check for decimal
        mark_map("1", r1, c1)

        #print(f"dec test after for: {map}\n")


        if map[r2][c2] == "M":
            return "decimal"
    
    return "neither"


og_map = [row[:] for row in map]

for q in range(num_queries):
    #print(f"\nOn Query {q}")
    r1, c1, r2, c2 = [int(x)-1 for x in inp[int(map_rows)+q+1].split()]

    #print(f"Starting ({r1}, {c1})")
    #print(f"Destination ({r2}, {c2})")


    #print(f"\nmap before {map}")

    print(check_map())

    #print(f"\nmap after {map}")

    map = [row[:] for row in og_map]

    #print(f"\nmap restored? {map}")