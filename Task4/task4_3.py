string = input("Type a string: ")
m_list = list(string.split())
len_str = []
for i in range(len(m_list)):
    len_str.append(len(m_list[i]))
b = len_str.index(max(len_str))
for i in range(len(len_str)):
    c = len_str.index(max(len_str))
    if c == b:
        print(c)
