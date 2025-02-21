""" test case 1

8
Jepson no no no no nobody never
Ashley why ever not
Marcus no not never nobody
Bazza no never know nobody
Hatty why no nobody
Hatty nobody never know why nobody
Jepson never no nobody
Ashley never never nobody no

"""


numLines = int(input())

names = {}
words = {}
appearanceRate = {}
out = []

for i in range(numLines):
    """
    Check every input and check for new person, put all unique words in a list as the values (Person | [Words])

    Keep a variable for how many people exist. (i can probably get that by length of dictionary)

    Put the unique words in the dictionary and count how many times they appear, if it equals numPeople, add it to the output list
    """

    msg = input().split()

    currentPerson = msg[0]

    #print(currentPerson)
    
    names.setdefault(currentPerson, []) # if they dont exist, set list
    
    #print(names)

    for i, word in enumerate(msg[1:]):
        if not word in names[currentPerson]:
            names.setdefault(currentPerson, []).append(word)
        appearanceRate[word] = appearanceRate.get(word, 0) + 1

for wordList in names.values():
    for word in wordList:
        words[word] = words.get(word, 0) + 1


numPeople = len(names)

#print(f"Amount of people: {len(names)}")

for word, num in words.items():
    if num == numPeople:
        out.append(word)

if len(out) != 0:
    # sort by appearanceRate then alphabetical order
    out.sort(key=lambda word: (-appearanceRate[word], word))

    for i in out:
        print(i)
else:
    print("ALL CLEAR")

"""for i in appearanceRate.items():
    print(i)"""