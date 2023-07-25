# import l5_function
#
# res = l5_function.calk(3, 6, "sum")
# print(res)
# res = l5_function.calk(6, 3, "div")
# print(res)

# from l5_function import calk, foo1
# from l5_function import *  # import all
# from l5_function import calk
#
# import time
# import random


# start = time.time()
# print(start)
# res = calk(3, 6, "sum")
# print(res)
# s = 0
# for i in range(100000):
#     s += i
# finish = time.time()
# print(finish - start)

# r = random.randint(1, 3)
# print(r)

# import l5_function
#
# print(l5_function.calk(3, 5, "div"))


# MINUS_ONE = -1  # constant (dont changing variable)
#
# a = 6
# b = 2
# print(a)
#
#
# def foo():
#     a = 45  # create local variable, scope -- function
#     global b  # take variable from global scope
#     b = 56
#     foo_a = 56
#     print(locals())
#     print(globals())
#     return a + b  # firstly search local scope
#
#
# def foo1(a, b):
#     b = 34  # create new local variable
#     print(locals())
#     print(globals())
#     return a + b
#
#
# s = foo()
# print(a)
# print(s)
# s = foo1(5, b)
# print(s)


# l = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l)
#
#
# def list_changer(changed_list: list[int], element: int):
#     changed_list = changed_list.copy()
#     changed_list.remove(element)
#     return changed_list
#
#
# new_l = list_changer(l, 5)
# print(new_l, id(new_l))
# print(l, id(l))


a, b, c = [4, 2, 1]
l = [4, 2, 1, 7]
print(a, c, b)
print(l)  # [4, 2, 1, 7]
print(*l)  # 4 2 1 7 unpacking


# def custom_sum(first, second=0, third=0):  # default initialized arguments should gone after uninitialized
#     return first + second + third


# def custom_sum(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
#
#
# print(custom_sum(3, 5, 6, 7, 3))

def famaly(**kwargs):
    print(kwargs)
    print(kwargs.get("mather", "you have not mather"))


famaly(mather="Olga", father="Kolya", brother="Denis")
famaly(me="Dima")
