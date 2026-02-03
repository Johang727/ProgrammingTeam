import math, sys

E, L, R = [int(x) for x in sys.stdin.readlines()]

def isPrime(n:int) -> bool:
    cap:int = int(math.sqrt(n))
    for k in range(2, cap+1):
        if (n % k == 0):
            return False
    return True

rolling_product:int = 1

for i in range(L, R):
    if isPrime(i):
        rolling_product *= (i**E)


print(rolling_product % 1000000007)
