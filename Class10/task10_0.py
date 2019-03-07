import time
def my_dec1(f):
    start_time = time.time()
    def wrap():
        f()
        print(str(time.time() - start_time) + 'Second')
    return wrap
def my_dec2(f):
    start_time = time.time()
    def wrap():
        f()
        with open('func_info.txt', 'w') as f1:
            func_time = time.time() - start_time
            f1.write(str(func_time) + "\n" + str(f.name))
    return wrap
@my_dec2
@my_dec1
def my_func():
    print(1234)
    return 3
my_func()