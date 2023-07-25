import time

L = [2, 5, 7, 1, 9]

# range()
# r1 = tuple(range(10))
# print(r1)
#
# r2 = list(range(3, 8))
# print(r2)
#
# r3 = tuple(range(6, 20, 3))
# print(r3)
#
# for i in range(6, 20, 3):
#     print(i)
#
# r4 = tuple(range(20, 11, -1))
# print(r4)

# reversed()
# r5 = tuple(reversed(range(6, 20, 3)))
# print(r5)
#
# for i in reversed(range(10)):
#     time.sleep(0.1)
#     print(i)
# else:
#     print("BOOM")

# sum()
# s1 = sum(range(100))
# print(s1)
#
# l1 = list(range(6, 20, 3))
# l11 = [i for i in range(6, 20, 3) if not i % 12 == 0]  # [<body of cycle> for i in ... if <condition>]
# # list comprecation
# print(l1, l11)

# s = 0
# start = time.time()
# for i in range(10000000):
#     s += i
# print(time.time() - start, s)
# time = 1.0062880516052246

# start = time.time()
# s = sum(range(10000000), )
# print(time.time() - start, s)
# s2 = sum(L, 50)
# print(s2)


# max()
# m1 = max(L)
# print(m1)
# m2 = max([], default=51)
# print(m2)
#
#
# def foo(x: int):
#     """
#
#     :param x:
#     :return: remainder of 4
#     """
#     return x % 4
#
#
# m3 = max(L, key=foo)  # max element in ring of 3
# print(m3)

# sorted()
sort_l = sorted(L)  # return new list
print(sort_l)
sort_l1 = L.sort()  # return nothing
print(sort_l1)
t = tuple(L)
print(t)
sort_t = sorted(t)
print(sort_t)

# enumerate()
