my_list = [int(i) for i in input("Enter numbers through comma: ").split(",")]
a = my_list.count(0)
for i in range(a):
    my_list.remove(0)
    my_list.append(-1)
print(my_list)