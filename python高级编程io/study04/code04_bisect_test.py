import bisect
from collections import deque

# 管理可排序序列 建议使用这个方法
list_data = deque()
bisect.insort(list_data, 4)
bisect.insort(list_data, 2)
bisect.insort(list_data, 8)
bisect.insort(list_data, 3)
print(list_data)