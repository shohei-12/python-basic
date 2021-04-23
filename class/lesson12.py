# setter, getter その2

class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):  # getter
        print('getter nameが呼ばれました')
        return self.__name

    @property
    def age(self):
        print('getter ageが呼ばれました')
        return self.__age

    @name.setter
    def name(self, name):  # setter
        print('setter nameが呼ばれました')
        self.__name = name

    @age.setter
    def age(self, age):
        print('setter ageが呼ばれました')
        if age < 0:  # 値を設定する際に値をチェックできる
            print('0以上の値をしてください')
            return
        self.__age = age


human = Human('Taro', 22)
human.name = 'Koichi'  # setterが呼ばれる
print(human.name)  # getterが呼ばれる
human.age = -1
human.age = 24
print(human.age)
