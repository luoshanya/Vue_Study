class test(object):
    def __init__(self, list_data):
        self.list_data = list_data

    # def __str__(self):
    #     return ','.join(self.list_data)
    #
    # def __repr__(self):
    #     return ','.join(self.list_data)

    def __len__(self):
        return len(self.list_data)

Test = test(['a', 'b' ,'c'])
print(len(Test))
