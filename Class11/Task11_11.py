import math
figure = int(input("������� ��� ������, ��������� ������� �� ������ ���������: ����������� - 1, ������������� - 2, ������� - 3, �������� - 4, ���������� - 5: "))
operation = int(input("������� ��� ��������, ������� �� ������ ���������: ������� - 1, �������� - 2, ����� - 3: "))
if figure == 1:
    a = int(input("������� ������ ������� ������������: "))
    b = int(input("������� ������ ������� ������������: "))
    c = int(input("������� ������ ������� ������������: "))
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
