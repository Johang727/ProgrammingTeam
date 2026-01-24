import math

def isPrime(n:int) -> bool:
    cap:int = int(math.sqrt(n))
    for k in range(2, cap+1):
        if (n % k == 0):
            return False
    return True

prime_dict:dict[int, set] = {}

prime_set:set[int] = set()


with open("pn", "w") as prime_nums:
    for i in range(1000, 1001000, 1000):
        curr_set = set()
        for j in range(i-1000, i):
            if isPrime(j):
                curr_set.add(j)

        prime_dict[i-1000] = curr_set

    prime_nums.write(str(prime_dict))