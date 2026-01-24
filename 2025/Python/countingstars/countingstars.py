import sys

sys.setrecursionlimit(1000000)

inp:list[str] = sys.stdin.readlines(); idx:int = 0; case:int = 0

def markStar(row:int, col:int, map:list[list[str]]):
    # check if row and col are valid
    if row >= 0 and col >= 0 and row < len(map) and col < len(map[row]):
        if map[row][col] == "-":
            map[row][col] = "S"
            markStar(row-1, col, map); markStar(row, col+1, map); markStar(row+1, col, map); markStar(row, col-1, map)

def countStars(map:list[list[str]]) -> int:
    num = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == "-":
                num += 1
                markStar(row, col, map)
    return num

while idx < len(inp):
    num_r, num_c = [int(x) for x in inp[idx].split()]
    idx += 1

    img = [[c for c in inp[idx + r].strip()] for r in range(num_r)]
    idx += num_r


    stars = countStars(img)
    print(f"Case {case+1}: {stars}")
    case += 1


"""
Mark stars, changing - to something else
check NESW and when you reach no more dashes, you're done.
Falls back to loop looking for dashes again, won't mark that star since it's a different char now.
"""

