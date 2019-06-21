class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def static(str_data):
        year, month, day = tuple(str_data.split('-'))
        return Date(int(year), int(month), int(day))

    @classmethod
    def cls_method(cls, str_data):
        year, month, day = tuple(str_data.split('-'))
        # cla代表是类名
        return cls(int(year), int(month), int(day))

    # 改变实例变量
    def tomorrow(self):
        self.day += 1

    def __str__(self):
        return '%s/%s/%s' % (self.year, self.month, self.day)

date = Date(2019, 6, 10)
date.tomorrow()
# print(date)
# <scrpt>alter('abc')</script>

data_str = '2019-6-10'
year, month, day = tuple(data_str.split('-'))
date = Date(int(year), int(month), int(day))
# print(date)

# 使用staticmethod完成初始化
date01 = Date.static(data_str)
# print(date01)

# 使用classmethod完成初始化
date02 = Date.cls_method(data_str)
# print(date02)

