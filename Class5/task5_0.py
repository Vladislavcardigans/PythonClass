my_list = [5, 'qwe', 1, 3, 2, 4, 2, 2, 'qwe', 'qwe', 'qwe']
repeat = []
for i in my_list:
    a = my_list.count(i);
    repeat.append(a)
print('Element: ' + str(my_list[repeat.index(max(repeat))]) + '\nNumber of repeat: ' + str(max(repeat)))
