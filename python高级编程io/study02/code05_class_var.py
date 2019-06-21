class A:
    # 类变量
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(2, 3)
# 实例的变量
a.aa = 11
# 类变量 两种不同的变量
A.aa = 100
print(a.aa, a.x, a.y)
b = A(2, 3)
# b.aa = 12
print(b.aa)
print(A.aa)

