x = int(input('Type X: '))
y = int(input('Type Y: '))
A = int(input('Type A: '))
D = int(input('Type D: '))
C = int(input('Type C: '))
if A*x*x*x*x+D*x*x+C == 0:
    if A*y*y*y*y+D*y*y+C == 0:
        print("OK")
    else:
        print("Not OK")
else:
    print("Not OK")