# 上下文管理器协议
class Test():
    def __enter__(self):
        # 开始
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 结束
        print('exit')

    def with_test(self):
        # 过程
        print('do something!')

with Test() as test:
    test.with_test()