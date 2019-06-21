class Test_code(object):
    def __init__(self, list_data):
        self.test = list_data

    # 魔法函数 可以使类变成对象 直接使用
    def __getitem__(self, item):
        return self.test[item]

# 对象实例化，可以进行for循环
test_code = Test_code(['a', 'b', 'c'])
# print(Test_code.__bases__)
for i in test_code:
    print(i)