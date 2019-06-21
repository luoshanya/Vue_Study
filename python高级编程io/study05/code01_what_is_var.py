# a = 1
# b = 1
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
del b[1]
print(b)
print(id(a), id(b))
print(a is b)