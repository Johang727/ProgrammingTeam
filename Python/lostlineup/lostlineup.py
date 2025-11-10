numPeople:int = int(input())

if numPeople == 1:
    print(1)
else:
    listPeople:list[int] = [int(x) for x in input().split()]

    # print(numPeople, listPeople)

    output:str = "1"

    for i in range(numPeople-1):
        output = f"{output} {listPeople.index(i)+2}"

    print(output)