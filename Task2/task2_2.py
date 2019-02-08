a = input(float)
b = input(float)
c = input(float)
if a > b:
    if a > c:
        if b > c:
            print(float(a)+float(c))
        else:
            print(float(a)+float(b))    
    else:
        print(float(b)+float(c))
if b > a:
    if b > c:
        if a > c:
            print(float(c)+float(b))
        else:
            print(float(a)+float(b))
    else:
        print(float(a)+float(c))