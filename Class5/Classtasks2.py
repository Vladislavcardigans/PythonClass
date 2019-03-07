def list_find(a):
    b = set(a)
    i = 0
    while len(a) > 1:
        a = a - b
        i += 1
    return a, i
c = list_find([1,2,3,4,4,4])
print(c)