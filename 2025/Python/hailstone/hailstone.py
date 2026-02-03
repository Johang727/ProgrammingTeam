
def h(n:int) -> int:
    """
    if n is even, the sequence is composed of n followed by sequence h(n/2)
    if n is odd, the sequence is composed of n followed by sequence h(3n+1)
    if n == 1: composed of 1


    find the sum in the end
    """
    global hailstonesToWatchFor
    #print(n)
    hailstonesToWatchFor += n
    if n == 1:
        # end
        pass
    else:
        if n % 2 == 0:
            # is even
            h(n//2)
        else:
            # is odd
            h(3*n + 1)

    return hailstonesToWatchFor


hailstonesToWatchFor:int = 0

num:int = int(input())

print(h(num))