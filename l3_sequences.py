# # list
# list_example = [3, "text", 9.7]
# other_list = list('qwerty')
# other_empty_list = list()
# empty_list = []
# print(other_list)
# print(list_example, type(list_example), id(list_example))
# new_list = list_example + [3]  # list concatenation, result is new list
# print(new_list, type(new_list), id(new_list), list_example == new_list,
#       list_example is new_list)
# single_item_list = [56]
# list_example.append(3)  # add element to the end of list
# print(list_example, type(list_example), id(list_example), list_example == new_list,
#       list_example is new_list)
# list_example.insert(2, "word")
# print(list_example)
# print(list_example[0], list_example[4], len(list_example))
# print(list_example[:3:2])
# copy_list = list_example.copy()
# print(copy_list, list_example, copy_list == list_example,
#       copy_list is list_example)

# # tuple
# tuple_example = tuple()
# print(tuple_example, type(tuple_example), id(tuple_example))
# other_tuple = (3,)  # (3) is just an integer
# print(other_tuple, type(other_tuple), len(other_tuple))
# tuple_example = (3, 6, 9, "world", 3)
# print(tuple_example.index(3), tuple_example.count(3), id(tuple_example))
# tuple_example = tuple_example + other_tuple
# print(tuple_example, id(tuple_example))
# list_from_tuple = list(tuple_example)
# print(list_from_tuple)
# t =  (3, 6, "dima", (3, 6, "dima"))
# print(t, type(t))

# for i in [4, 8, 9, "Dima"]:  # for loop takes any iterable object
#       print(i)


# #  dictionary
# dictionary = dict()
# print(dictionary, type(dictionary))
# d1 = {1: 'a', 2: 'b', 'third': 5, 9.9: "float", 'a': str, 1: "One"}  # dictionary -- is data type
#                                                                     # that have key and value
# print(d1, type(d1), id(d1))
# print(d1[2], d1['third'])
# d1["new_val"] = 56
# print(d1, type(d1), id(d1))
# d1['a'] = "Any value"
# print(d1, type(d1), id(d1))
# for i in d1:
#     print(f'key = {i} val = {d1[i]}')
#
# a, b = (1, 8)
# print(a, b)
# unzip_d1 = d1.items()
# print(unzip_d1)
# for k, v in d1.items():
#     print(k, v)
# print(d1.get(9), d1.get(9.9), d1.get(2))
# v = d1.pop(2)
# print(v)
# print(d1, type(d1), id(d1))
# print(d1.keys())  # get all keys
# print(d1.values())  # get all values
# d2 = d1.fromkeys((4, 6, 2), "value")
# print(d2, type(d2))
# d1[(4, 6)] = (4, 6)
# print(d1, type(d1), id(d1))
# # d1[[4, 7]] = [4, 7]  # key can be only immutable value
# # print(d1, type(d1), id(d1))
# d1["immutable"] = [4, 7]
# print(d1, type(d1), id(d1))
# d1[876] = d1
# print(d1, type(d1), id(d1))
# print(d1[876])


# set
set_example = set('змееед')  # mutable unordered object
print(set_example)
set1 = set()  # {} creates dict
print(set1, type(set1))
# print(set_example[3])  # no indexes in set ( set is unordered)
last = set_example.pop()
print(set_example)
set_example.remove('е')
print(set_example)
set1.add(6)
new_set = set_example.union(set1)
print(new_set, type(new_set))

