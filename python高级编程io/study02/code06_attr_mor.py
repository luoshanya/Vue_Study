class D:
    pass

class B(D):
    pass

class C(D):
    pass

class A(B, C):
    pass
# C3算法  菱形继承关系
print(A.__mro__)