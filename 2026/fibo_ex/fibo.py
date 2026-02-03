# key = idx, value = num
cache:dict[int,int] = {0:0, 1:1}

def fib(idx:int) -> int:
    global cache
    if cache.get(idx, -1) != -1:
        return cache[idx]

    return fib(idx-2) + fib(idx-1)

numbers:int = int(input())

numbers += 1

for idx in range(1, numbers):
    result:int = fib(idx)
    cache[idx] = result
    print(f"F_{idx} = {result}")

    idx += 1



