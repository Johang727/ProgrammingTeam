n = input()
name = input()

acro = ''.join(i[0] for i in name.split() if i[0].isupper())

print(acro)