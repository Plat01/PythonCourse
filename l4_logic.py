t = True
f = False
# print(t, type(t))
#
# t1 = 5 > 2
# print(t1)
# f1 = 2 * 2 == 5
# print(f1)
# print(t1 == f1)
# # and and do only for boolean values
# print(True and False)
# print(True or False)

# print(1 in [1, 5, "addfa"], "1" in "1234")
# print(1 is 1, [1, 2, 3] is [1, 2, 3])
# print(1 == 1, [1, 2, 3] == [1, 2, 3])

bool_list = [True, False, True, False, True]
print(sum(bool_list))
print(int(t), int(f))  # 1 0
print(bool(1), bool(0))  # True False
print(bool("Hello"), bool(""))  # True False
print(bool([3, 5, 6]), bool([]))  # True False
print(bool((4, 6, 7)), bool(tuple()))  # True False
print(bool(None), type(None))
print("qwerty" and [])
print({4, 6, 7} or 0)




