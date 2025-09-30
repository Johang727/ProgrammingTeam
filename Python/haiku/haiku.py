import sys



#numSyl:int = int(input()) # first line contains an integer 1-100

syl1:int = 0; syl2:int = 0; syl3:int = 0; sylcurr:int = 0



inp:str = sys.stdin.read()

listyList:list[str] = inp.splitlines()

num:int = int(listyList[0])

syls:list[str] = listyList[1:num+1]

poem:list[str] = listyList[num+1:]

#print(poem)


def haiku(line:str) -> None:
    global sylcurr

    #print(line, sylcurr)
    
    if not line:
        return
    else:
        sylcurr += 1
        for syl in syls:
            if line.startswith(syl):
                line = line.lstrip(syl)
                haiku(line)





sylcurr = 0
haiku(poem[0])
syl1 = sylcurr
sylcurr = 0
haiku(poem[1])
syl2 = sylcurr
sylcurr = 0
haiku(poem[2])
syl3 = sylcurr

print([syl1, syl2, syl3])


if [syl1, syl2, syl3] == [5, 7, 5]:
    print("haiku")
else:
    print("come back next year")