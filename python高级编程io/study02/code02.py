
class Cat_cat(object):
    def say(self):
        print('i am a cat')

class Dog_dog(object):
    def say(self):
        print('i am a dog')

    def __getitem__(self, item):
        return 'a'

class test():
    def __init__(self, list_data):
        self.list_data = list_data

    def __getitem__(self, item):
        return self.list_data[item]

Test = test(['bhb', 'nhbu'])

class Duck_duck(object):
    def say(self):
        print('i am a duck')

# 多态 鸭子类型
animal_data = [Cat_cat(), Dog_dog(), Duck_duck()]
for animal in animal_data:
    print(animal.say())

dog = Dog_dog()
a = ['bb', 'cc']
a_tuple = ['aa', 'bb']
a_set = set()
a_set.add('dd')
a_set.add('CC')
# 拼接迭代的数列
# a.extend(dog)
print(a)

# 判断是否是子类
class A:
    pass
class B(A):
    pass

b = B()
print(isinstance(b, A))#True