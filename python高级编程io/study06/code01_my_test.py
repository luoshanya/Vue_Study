from datetime import datetime

class User_date():
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = None

    def get_date(self):
        return datetime.now().year - self.birthday.year

    @property#可以使函数变成属性调用
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter#动态属性设置
    def age(self, value):
        # 不用return
        self._age = value


if __name__ == '__main__':
    user = User_date('lin', datetime(year=1996, month=10, day=13))
    # 调用函数
    print(user.get_date())
    user.age = 18
    # 调用属性值
    print(user._age)
    #调用属性
    print(user.age)
