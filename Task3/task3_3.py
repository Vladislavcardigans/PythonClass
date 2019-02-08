my_str = 'Hello!Anthony!Have!A!Good!Day!'
my_list = (my_str.upper()).split('!')
my_list.sort()
l = len(my_list)
for i in range(l):
    print(my_list[i])