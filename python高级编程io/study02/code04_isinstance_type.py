class A:
    pass

class B(A):
    pass

b = B()
# 继承类方面最好使用isinstance检测是否存在关系 最好别使用type
print(isinstance(b, B))
# type的用法   is的作用：其实是将b的地址指向B的地址 一样就返回true 不然就false 所以与A类对比关系就会出错
print(type(b) is B)#Ture
print(type(b) is A)#False