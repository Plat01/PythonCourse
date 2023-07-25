def foo():
    print("Hello world")
    if "sunny":
        print("Have a nice day")


def foo1(name):
    print("Have a nice day", end=" ")
    if name:
        print(name)


def calk(a: int, b: int, operation='') -> int:  # def func_name(arg: arg_type...) -> return_type:
    """
    This function implement calculator with wierd interface
    :param a: first argument
    :param b: second argument
    :param operation: operation name
    :return: result
    """
    print(globals())
    # print(a + b)
    # return a + b
    if operation == "sum":
        return a + b
    elif operation == "mult":
        return a * b
    elif operation == "div":
        return a / b
    return 0


# res = calk(4, 6, "mult")
# print(res)
# res = calk(4, 6, "div")
# print(res)
# res = calk(3, 6)
# print(res)
# res = calk(b=5, a=3, operation="div")
# print(res)


if __name__ == '__main__':
    foo()
    res = calk(4, 6, "sum")
    print(res)
    # a = foo1("Dima")
    # print(a)
    # foo1("Roma")
    # print(globals())
    # print("Note from l5_function file")
    # calk("a", 3, "sum")

# if banan == "banana":
#     print("Banana")
