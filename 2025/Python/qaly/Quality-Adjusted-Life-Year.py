"""
5 # number of periods which qol is constant
1.0 12.0 # quality, years
0.7 5.2
0.9 10.7
0.5 20.4
0.2 30.0

41.470
"""
import sys


inp:list[str] = sys.stdin.read().split()

it = iter(inp)

periods:int = int(next(it))

rolling_sum:float = 0.0

for _ in range(periods):
    rolling_sum += ( float(next(it))*float(next(it)) )


print(f"{rolling_sum:.3f}")