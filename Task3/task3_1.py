my_list = [3,5,7,4,5,6,9,4,3]
maxnum = my_list.index(max(my_list))
my_list = my_list[0:maxnum] + my_list[maxnum + 1:10]
print(my_list)