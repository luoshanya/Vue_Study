# 列表推导式 判断语句放在后面
list_data = [i for i in range(21) if i % 2 == 1]
print(list_data)

# 生成器表达式
gender_data = (i for i in range(31) if i % 2 == 1)
print(gender_data)
# 生成式需要循环才可以看
for i in gender_data:
    print(i)

# 字典推导式
data  = {'a':1, 'b':3, 'c':4}
dict_data = {value:key for key, value in data.items()}
print(dict_data)

# 集合推导式
set_data = {key for key , value in data.items()}
print(type(set_data))