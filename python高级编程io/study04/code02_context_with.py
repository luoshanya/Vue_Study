import contextlib

@contextlib.contextmanager
def test():
    print('one')
    # 生成器
    yield
    print('three')

with test() as t:
    print('two')