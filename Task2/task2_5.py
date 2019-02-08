a = int(input('Type A: '))
b = int(input('Type B: '))
if a > b:
    a,b = 2*a*b,(a+b)/2
    print(a,b)
else:
    a,b = (a+b)/2, 2*a*b
    print('A =' + str(a) + ' B = ' + str(b))