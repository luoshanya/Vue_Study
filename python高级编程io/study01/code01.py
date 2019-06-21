def ask(name):
    print('hello')

def jie_ask():
    print('hello1')
    return ask
# 监听器原理
test = jie_ask()
test('bobby')