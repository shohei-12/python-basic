# デフォルト値、可変長引数、複数の返り値

def sample(arg1, arg2=100):
    print(arg1, arg2)


sample(200)
sample(200, 300)


def spam(arg1, *arg2):  # 可変長タプル
    print(f'arg1 = {arg1}, arg2 = {arg2}')
    print(type(arg2))


spam(1, 2, 3, 4, 5)


def spam_2(arg1, **arg2):  # 可変長辞書
    print(f'arg1 = {arg1}, arg2 = {arg2}')
    print(type(arg2))


spam_2(3, name='Taro', age=20)


def spam_3(arg1, *arg2, **arg3):
    print(f'arg1 = {arg1}, arg2 = {arg2}, arg3 = {arg3}')


spam_3(1, 2, 3, 4, 5, name='Taro', age=20)


def sample_2():
    return 1, 2, 3


print(sample_2())
a, b, c = sample_2()
print(a, b, c)
