import numbers

class IntFiled():
    # 数据描述符
    def __get__(self, instance, owner):
        # 返回值
        return self.age

    def __set__(self, instance, value):
        # 判断字符的类型时， 首先进入这里
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        elif value <= 0:
            raise ValueError('value must greater than zero')
        # 返回value值 判断
        self.age = value

    def __delete__(self, instance):
        pass

class User:
    age = IntFiled()

if __name__ == '__main__':
    user = User()
    user.age = 3
    print(user.age)
