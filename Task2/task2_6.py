a = int(input('Type A: '))
b = int(input('Type B: '))
c = int(input('Type C: '))
if a >= b >= c:
    a = a*2
    b = b*2
    c = c*2
    print(a,b,c)
else:
    a,b = b,a
    print(a,b,c)