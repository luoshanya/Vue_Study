from datetime import date

class User_date():
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    # 查找属性的魔法函数
    def __getattr__(self, item):
        # item是属性名
        return '找不到属性%s' % item

    # 无论属性存在与否，属性都会进入这个魔法函数 最好别用 用框架的时候才会到
    # def __getattribute__(self, item):
    #     return 'yes'


if __name__ == '__main__':
    user = User_date('lin', date(year=1996, month=10, day=13))
    # 调用函数
    print(user.tes)