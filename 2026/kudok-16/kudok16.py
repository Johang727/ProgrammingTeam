"""
Sample In:
2
   33 35 38 30
16 ? ? ? 8
42 14 12 13 ?
39 ? 15 4 9
39 6 ? ? ?
   30 26 27 43
34 ? ? ? 8
39 ? ? 14 ? 
28 ? 4 ? ?
35 5 ? ? ?

Sample Out:
   33 35 38 30
16 2 1 5 8
42 14 12 13 3
39 11 15 4 9
39 6 7 16 10

   30 26 27 43
34 15 1 10 8
39 3 9 14 13 
28 7 4 11 6
35 5 12 2 16
"""

import sys

inp:list[str] = sys.stdin.read().strip().split()

it = iter(inp)

n = lambda: int(next(it))

cases:int = n()

col1:int = n()
col2:int = n()
col3:int = n()
col4:int = n()

