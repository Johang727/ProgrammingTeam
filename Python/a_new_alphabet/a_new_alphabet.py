adict = {'a':'@','b':'8','c':'(','d':'|)','e':'3','f':'#',
         'g':'6','h':'[-]','i':'|','j':'_|',
         'k':'|<','l':'1','m':'[]\/[]','n':'[]\[]','o':'0',
         'p':'|D','q':'(,)','r':'|Z','s':'$','t':"']['",
         'u':'|_|','v':'\/','w':'\/\/','x':'}{','y':'`/','z':'2'}

''' TJ's and my answer
theLine = input().lower()

betterLine = ''
for ch in theLine:
    if ch in adict:
        betterLine += adict[ch]
    else:
        betterLine += ch

print(betterLine)
'''

print(''.join([adict.get(c,c) for c in input().lower()])) # meysenburger output