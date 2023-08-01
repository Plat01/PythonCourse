def fib(n: int):
    global counter
    counter += 1
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n - 2) + fib(n - 1)

# TODO: придумать как исправить костыль
# num = 0
try:
    num = int(input("input number of Fibonacci sequence: "))
    # after error we will go to "except" block

    # print(num)
    # fib(num)
except ValueError as e:  # execute if error occurs
    print(e)
finally:  # execute anyway
    # num = num if num else 0
    num = globals().get('num', 0)

print(num)

counter = 0
print(counter, "start counting")

try:
    print(fib(num))
finally:
    print(counter, "finish counting")

# num = int(input("input number of Fibonacci sequence: "))
# print(num)


# sister convert
# dec = int("10")
# print(dec)
#
# binary = int("1001", base=2)
# print(binary)
# print(bin(binary))
#
# octal = int("0o11", base=8)
# print(octal)
# print(oct(octal))
#
# hexadecimal = int("0xAA", base=16)
# print(hexadecimal)
# print(hex(hexadecimal))
