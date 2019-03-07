string = input("Type a string: ")
m_list = list(string.split())
len_str = []
for i in range(len(m_list)):
    len_str.append(len(m_list[i]))
b = len_str.index(min(len_str))
mini_list = list(m_list[b])
len_set = set(mini_list)
m_set = {'a', 'e', 'y', 'u', 'i', 'o'}
a = m_set.intersection(len_set)
print(a)