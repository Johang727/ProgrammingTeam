"""
n:int = seedlings farmer jon bought

takes 1 day for jon to plant 1 tree

t:list[int] = how long index-n tree takes to grow.
"""


"""
# Attempt #1 - Time Limit Exceeded

seedlings:int = int(input())

treeTime:list[int] = sorted([int(x) for x in input().split()], reverse=True)

treePlanted:list[bool] = [False]*seedlings

days:int = 0

while True:
    if treePlanted != [True]*seedlings:
        jonTired = False
        for i in range(seedlings):
            if treePlanted[i]:
                # let it grow
                if treeTime[i] > 0:
                    treeTime[i] -= 1
                # else, it's fully grown
            if not jonTired and not treePlanted[i]:
                # Jon can plant a tree
                treePlanted[i] = True
                jonTired = True # Jon is now tired and cannot do anything else

        days += 1

        if treeTime == [0]*seedlings:
            # All trees are grown
            days += 1 #Jon needs to wait a day after they are all grown
            break
    else:
        # All trees are planted now, Jon can rest
        treeTime.sort(reverse=True)
        days += treeTime[0] + 1
        break

print(days)
# party time :D"""


# get that input from my man Jon
seedlings:int = int(input())
treeTime:list[int] = sorted([int(x) for x in input().split()], reverse=True)

plantingDay:int = 1
maxTime:int = 0

for time in treeTime:
    completion:int = plantingDay + time
    if completion > maxTime:
        maxTime = completion
    plantingDay += 1

days = maxTime + 1 # type: ignore

print(days)