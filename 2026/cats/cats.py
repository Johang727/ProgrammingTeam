"""
Info:

- The cats demand 1 mL of milk
- Aunt has a limited amount of milk
- Cats are social distanced
- You have drunken large amounts of hard liquor (-1 mL milk per meter walked)
- Extra milk can be left to cats as they won't drink more than 1 mL

In:
T - number of cases
M - amount of milk in the fridge in milimeters
C - number of cats

C*(C-1) / 2 lines

i - cat #i
j - cat #j
Dij - Distance between i and j in meters

The fridge is at cat #0

Sample:

1
20 5
0 1 4
0 2 3
0 3 10
0 4 15
1 2 7
1 3 3
1 4 5
2 3 4
2 4 3
3 4 8

returns "yes"



Out:
yes/no: is it possible to feed every cat at least 1 mL of milk?

Time Limit: 6 seconds
    - Might be able to simulate? 20 cases with 2000 cats will take too long; first can pass with simulation. Might still be worth to get a start.

    - Some sort of node search? Need to account for leaving milk with the cats tho

    - Cat 0 will automatically take 1 mL, but can be left with more.
"""

import sys

inp = sys.stdin.read().split()

it = iter(inp)

cases:int = int(next(it))

for _ in range(cases):

    milk:int = int(next(it))
    cats:int = int(next(it))


    #print(milk, cats)

    cat_matrix = [[0] * cats for _ in range(cats)]

    combinations:int = ( cats * (cats - 1) ) // 2

    for _ in range(combinations):
        cat_i:int = int(next(it))
        cat_j:int = int(next(it))
        milk_cost:int = int(next(it))

        cat_matrix[cat_i][cat_j] = cat_matrix[cat_j][cat_i] = milk_cost

    min_distance:list[float] = [float('inf')] * cats
    visited:list[bool] = [False] * cats
    min_distance[0] = 0
    total_cost:int = 0
    
    for _ in range(cats):
        cat:int = -1
        current_min:float = float('inf')
        for i in range(cats):
            if not visited[i] and min_distance[i] < current_min:
                current_min = min_distance[i]
                cat = i
        
        visited[cat] = True
        total_cost += current_min # type: ignore
        

        row:list[int] = cat_matrix[cat]
        for next_cat in range(cats):
            if not visited[next_cat]:
                new_cost = row[next_cat]
                if new_cost < min_distance[next_cat]:
                    min_distance[next_cat] = new_cost
    
    print("yes" if (total_cost + cats <= milk) else "no")