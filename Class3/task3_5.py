s = input("Type first string: ")
d = input("Type second string: ")
c = s.find(d)
if c > 0:
    print('Coincidence')
else:
    print('No coincidence')