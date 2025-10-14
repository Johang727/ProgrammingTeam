import sys



#numSyl:int = int(input()) # first line contains an integer 1-100

syl1:bool = False; syl2:bool = False; syl3:bool = False



inp:str = sys.stdin.read()

listyList:list[str] = inp.splitlines()

num:int = int(listyList[0])

syls:list[str] = listyList[1:num+1]

poem:list[str] = listyList[num+1:]

#print(poem)


def haiku(line:str, num:int):

    if(not line and num == 0):
        return True
    if(line and num == 0):
        return False
    for s in syls:
        if line.startswith(s):
            if(haiku(line[len(s):].strip(), num - 1)):
                return True
    return False





syl1 = haiku(poem[0], 5)

if syl1:
    syl2 = haiku(poem[1], 7)

if syl2 or syl1:
    syl3 = haiku(poem[2], 5)

#print([syl1, syl2, syl3])


if [syl1, syl2, syl3] == [True]*3:
    print("haiku")
else:
    print("come back next year")