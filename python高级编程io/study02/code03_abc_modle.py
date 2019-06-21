# 如何模拟一个抽象基类
class test():
    def get(self, data):
        raise NotImplementedError
    def post(self, data, key):
        raise NotImplementedError


class test01(test):
    # 继承必须要抽象基类就必须使用上面规定好的方法，不然会报错
    def get(self, data):
        pass
    def post(self, data, key):
        pass
# 这个错误是在使用对象后才报错的
Test = test01()
Test.get('a')

# 一下是在造对象的时候就报错了
import abc

class Test_jl(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, data):
        raise NotImplementedError

    @abc.abstractmethod
    def post(self, data):
        raise NotImplementedError

class test_jl(Test_jl):
    def get(self, data):
        pass

    def post(self, data):
        pass

test = test_jl()
