# プライベート変数

"""
__variable:プライベート変数はアンダースコアを2つ付けて定義する
"""


class Human:
    __class_val = 'Human'

    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def print_msg(self):
        print(f'name = {self.__name}, age = {self.age}')


human = Human('Taro', 15)
# print(human.__name) # エラーになる
# print(Human.__class_val) # エラーになる
# print(human._Human__name)
human.print_msg()
