numLines = int(input())

t9 = {'a':'2','b':'22','c':'222'}

for i in range(numLines):
    oldWord = input()
    newWord = ''
    for i in range(len(oldWord)):
        if i == 0: # first letter
            newWord += t9.get(oldWord[0])
        else: # the rest of the letters
            currentNum = t9.get(oldWord[i])[:1]
            if currentNum == lastNum:
                newWord += ' ' + t9.get(oldWord[i])
        lastNum = t9.get(oldWord[i])[:1]
    print(newWord)
