# カプセル化、setter、getter

"""
カプセル化:クラスの外部から変数が見えないようにすること
"""


class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print('getter nameを呼び出しました')
        return self.__name

    def get_age(self):
        print('getter ageを呼び出しました')
        return self.__age

    def set_name(self, name):
        print('setter nameを呼び出しました')
        self.__name = name

    def set_age(self, age):
        print('setter ageを呼び出しました')
        self.__age = age

    name = property(get_name, set_name)  # nameを指定するとget_name、set_nameが呼び出される
    age = property(get_age, set_age)

    def print_msg(self):
        print(self.name, self.age)  # self.nameとself.ageはゲッターを呼んでいる


human = Human('Taro', 15)
human.name = 'Jiro'  # set_nameメソッドを呼んでいる
human.age = 18  # set_ageメソッドを呼んでいる

human.print_msg()

print(human.name)  # get_nameを呼んでいる
name = human.name  # get_nameを呼んでいる
print(name)
print(human.age)  # get_ageを呼んでいる
age = human.age  # get_ageを呼んでいる
print(age)
