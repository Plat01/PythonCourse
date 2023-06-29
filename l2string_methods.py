# s = input("Input string: ")
s = "abcdefg"
print(s[-1])
print(s[3], s[-4])
print(s[2:4])  # output simbols from 2nd index to 4th index (excluded)


# these sequences have indexes to
# t = (5, 6, 4)  # tuple
# l = [6, 8, 2]  # list

print(s[1:5:2])
print(s[::2])
print(s[::-1])
print(s[:3:-1])

print(s, id(s))  # id function return place of object in memory
s = s[::-1]  # turn "abcdefg" into "gfedcba"
print(s, id(s))
# s[3] = "q"  # string is immutable object
# print(s, id(s))

# for i in s:  # move "i" trow whole "s" sequence (str)
#     print(i)


# when we change string, we take new object with new location in memory
print(s.index('ba'))
print(s, id(s))
s = s.capitalize()
print(s, id(s))

s_lower = s.lower()
print(s_lower, id(s_lower))
s_upper = s.upper()
print(s_upper, id(s_upper))
print(s_lower == s_upper)
print(s_lower is s.lower())
# print('s' is 's')

s = "Mother wash window"
list_s = s.split(maxsplit=1)
print(list_s)
srt_back = " ".join(list_s)
print(srt_back)

num_s = "23"
print(num_s.isdigit())
# print(s_upper," is string in upper case --",  s_upper.isupper())
# print(s_upper + " is string in uppercase -- " + str(s_upper.isupper()))
print(f"{s_upper} is string in uppercase -- {s_upper.isupper()}")
