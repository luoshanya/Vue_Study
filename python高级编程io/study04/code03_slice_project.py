import numbers

class Test_prpject():
    def __init__(self, name, project_name, pro_list):
        self.name = name
        self.project_name = project_name
        self.pro_list = pro_list

    # 翻转的魔法函数
    def __reversed__(self):
        # 翻转的方法
        return self.pro_list.reverse()

    # 最重要的魔法函数
    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(name=self.name, project_name=self.project_name, pro_list=self.pro_list[item])
        elif isinstance(item, numbers.Integral):
            return cls(name=self.name, project_name=self.project_name, pro_list=[self.pro_list[item]])

    # 返回长度
    def __len__(self):
        return len(self.pro_list)

    # 迭代器魔法函数
    def __iter__(self):
        # 迭代
        return iter(self.pro_list)

    # if in 的魔法函数
    def __contains__(self, item):
        if item in self.pro_list:
            return True
        else:
            return False



pro_list = ['a', 'b', 'c']
test = Test_prpject(name='猪', project_name='猪猪', pro_list=pro_list)
# debug 翻转  调用魔法函数__reversed__
reversed(test)
if 'a' in test[0:3]:
    print('yes')

