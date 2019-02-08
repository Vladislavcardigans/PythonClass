def calc(a,b, *args):
    sum2 = 1
    for i in args:
        sum2 *= i 
    if min(args) == 0:
        sum3 = 0
    else:
        sum3 = a + b + sum2/min(args)
    return sum3
v = calc(1,2,3,4,5,6,7,-5)
print(v)