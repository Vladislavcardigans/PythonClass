s = input("Type a letter: ")
a = s.find('Mr')
b = s.find('Mrs')
c = s.find('Miss')
d = s.find('Ms')
if a > 0:
    print('Male')
if b > 0:
    print('Male')
if c > 0:
    print('Female')
if d > 0:
    print('Female')