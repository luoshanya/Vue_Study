class Test_test():
    # 这个的运行是在创建实例前
    def __new__(cls, *args, **kwargs):
        print('in new')
    #     如果不return super()就不会跑__init__
        return super().__new__(cls)

    # 这个的运行是在创建实例前
    def __init__(self, name):
        print('in init')
        pass

if __name__ == '__main__':
    test = Test_test(name = 'kelin')