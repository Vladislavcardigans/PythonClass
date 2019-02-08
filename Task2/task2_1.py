a = int(input("Enter first operand: "))
b = int(input("Enter second operand: "))
c = input("Enter operator: ")
if type(a) == int and type(b) == int:
    if c == '+':
        print("Result: " + str(int(a)+int(b)))
    elif c =='-':
        print("Result: " + str(int(a)-int(b)))
    elif c =='*':
        print("Result: " + str(int(a)*int(b)))
    elif c =='/':
        print("Result: " + str(int(a)/int(b)))
    else:
        print('Result: Nan')
else:
    print('Result: Nan')