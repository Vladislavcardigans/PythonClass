my_list = list(input())
for i in range(len(my_list)):
    if my_list[i] in range(chr(65), chr(90)):
        print("Not OK")