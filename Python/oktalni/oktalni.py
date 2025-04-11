convDict = {"000":'0', "001":'1', "010":'2', "011":'3', "100":'4', "101":'5', "110":'6', "111":'7'}

inp:str = input()

extras:int = len(inp)%3 # this returns how many extras there are.

if extras != 0:
    zeros:int = 3-extras # this is how many zeros need to be appended to the beginning of the string
    for i in range(zeros):
        inp = '0' + inp

octal:str = ""
octalList:list[str] = []

for i in range(0, len(inp), 3):
    octalList.append(inp[i]+inp[i+1]+inp[i+2])

out:str = ""

for item in octalList:
    out += convDict[item]

print(out)