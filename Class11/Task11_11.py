import math
figure = int(input("¬ведите код фигуры, параметры которой вы хотите посчитать: треугольник - 1, пр€моугольник - 2, квадрат - 3, трапеци€ - 4, окружность - 5: "))
operation = int(input("¬ведите код операции, которую вы хотите выполнить: площадь - 1, периметр - 2, объем - 3: "))
if figure == 1:
    a = int(input("¬ведите первую сторону треугольника: "))
    b = int(input("¬ведите вторую сторону треугольника: "))
    c = int(input("¬ведите третью сторону треугольника: "))
    try:
        if operation == 1:
            p = (1/2)*(a+b+c)
            s = math.sqrt(p*(p-a)*(p-b)*(p-c))
            print(str(s))
        elif operation == 2:
            p = a+b+c
            print(str(p))
    except:
        print("Not OK")
        
elif figure == 2:
    pass
