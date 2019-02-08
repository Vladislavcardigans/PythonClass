a = int(input('Type A: '))
b = int(input('Type B: '))
c = int(input('Type C: '))
if a%2 == 0:
    print(max(a,b,c))
elif b%2 == 0:
    print(max(a,b,c))
elif c%2 == 0:
    print(max(a,b,c))
else:
    print(min(a,b,c))