P = float(input("Enter a P, 0 < P < 25: "))
sum = 1000
if 0 > P or P > 25:
    print('Invalid P')
i = 0
while sum < 1100:
    sum *= 1+P/100
    i += 1
print("Number a mount: " + str(i) + "\nMoney: " + (str(sum)))