my_list = input().split()
numb = int(input())
for i in range(len(my_list)):
    my_list[i] = int(my_list[i])
quanty = my_list.count(numb)
print(quanty)