# if 5 > 2:
#     print("hello")
#     print("world")

# x = 1
# x = "Sally"
# print(x)
# print(type(x))

# x = y = z = "orange"
# print(x)
# print(y)
# print(z)

# Unpack a Collection
fruits = ["apple", "banana", "orange"]
# x, y, z = fruits
# print(x, y, z)
# print(x + y + z)

# a = 5
# b = 10
# print(a+b)

# if "lemon" in fruits:
#     print("true")
# else:
#     print("false")

newList = []

for x in fruits:
    if "n" in x:
        newList.append(x)

print(newList)

# function


def my_function(input):
    print("hello " + input)


my_function("david")
