"""

seed times simulation run

in:
4 1000 
22 2000
25 1000

out:
9 1 0 0 0 0 0 0 0 0
7 1 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 0 0 0
1 2 0 0 0 0 1 1 0 0
"""
import sys

class r:
    def __init__(self, seed:int) -> None:
        self.seed = seed
    def new_number(self) -> int:
        self.seed = ((self.seed*5171)+13297) % 50021
        return self.seed
    



def check_connection(tree_a:int, tree_b:int, trees:dict) -> int:
    global paths

    trees[tree_a] = 2


    if tree_b in paths.get(tree_a, set()):
        return 1
    if tree_a == tree_b:
        paths.setdefault(tree_a, set()).add(tree_b)
        paths.setdefault(tree_b, set()).add(tree_a)
        return 1

    if trees.get(tree_a + 100, 0) == 1:
        #print("tree right")
        if check_connection(tree_a + 100, tree_b, trees) == 1:
            paths.setdefault(tree_a + 100, set()).add(tree_b)
            paths.setdefault(tree_b, set()).add(tree_a + 100)
            return 1
    if trees.get(tree_a - 100, 0) == 1:

        #print("tree left")
        if check_connection(tree_a - 100, tree_b, trees) == 1:
            paths.setdefault(tree_a - 100, set()).add(tree_b)
            paths.setdefault(tree_b, set()).add(tree_a - 100)
            return 1


    if tree_a % 100 != 99:
        if trees.get(tree_a + 1, 0) == 1:
            #print("tree up")
            if check_connection(tree_a + 1, tree_b, trees) == 1:
                paths.setdefault(tree_a + 1, set()).add(tree_b)
                paths.setdefault(tree_b, set()).add(tree_a + 1)
                return 1

    if tree_a % 100 != 0:
        if trees.get(tree_a - 1, 0) == 1:
            #print("tree down")
            if check_connection(tree_a - 1, tree_b, trees) == 1:
                paths.setdefault(tree_a - 1, set()).add(tree_b)
                paths.setdefault(tree_b, set()).add(tree_a - 1)
                return 1

    
    return 0



sys.setrecursionlimit(1000000000)

inp:list[str] = sys.stdin.read().strip().split()

it = iter(inp)

n = lambda: int(next(it))

num_cases:int = len(inp) // 2


for _ in range(num_cases):

    paths:dict[int, set[int]] = {}

    tree_grid:dict[int, int] = {}

    #print(tree_grid)

    rand:int = n()

    rng = r(rand)

    queries:int = n()

    num_fires:int = 0

    fire_list:list[int] = []

    tree_locations:list[int] = []



    for i in range(queries):

        while True:
            tree_plant_pos:int = rng.new_number() % 10000

            #print(tree_plant_pos)

            if tree_grid.get(tree_plant_pos, 0) == 0:
                tree_grid[tree_plant_pos] = 1
                tree_locations.append(tree_plant_pos)
                break
        
        a:int = rng.new_number() % (i+1)
        b:int = rng.new_number() % (i+1)

        tree_a:int = tree_locations[a]
        tree_b:int = tree_locations[b]


        new_trees = tree_grid.copy()

        #print(i)
        
        num_fires += check_connection(tree_a, tree_b, new_trees)

    
        if (i + 1) % 100 == 0:
            fire_list.append(num_fires)
            num_fires = 0


    print(*fire_list)
