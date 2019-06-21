from study02.code07_class_method import Date

# 数据封装和私有化
class Pro_method():
    def __init__(self, birthday):
        # 私有化 在前面加__
        self.__birthday = birthday

    def get_age(self):
        age = 2019 - self.__birthday.year
        return age

pro_method = Pro_method(Date(1996, 10, 13))
#取不到
# print(pro_method.__birthday)
# 但是只是在语言层面加了点小技巧 这样可以获取 换了一个新的名词
print(pro_method._Pro_method__birthday)
print(pro_method.get_age())
