# global关键字用来在函数或其他局部作用域中使用全局变量。但是如果不修改全局变量也可以不使用global关键字。
# num=1
# def fun1():
#     global num    #需要使用golbal关键字声明
#     print(num)
#     num=123
#     print(num)
# fun1()

# nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
def outer():
    num = 10

    def inner():
        nonlocal num
        num = 100
        print(num)

    inner()
    print(num)


outer()

gcount = 0


def global_test():
    print(gcount)


def global_counter():
    global gcount
    gcount += 1
    return gcount


def global_counter_test():
    print(global_counter())
    print(global_counter())
    print(global_counter())


global_counter_test()


def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def make_counter_test():
    mc = make_counter()
    print(mc())
    print(mc())
    print(mc())


make_counter_test()
