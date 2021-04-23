# クラスの定義

class Car:
    """車クラス
    """

    # プロパティ
    country = 'Japan'
    year = 2019
    name = 'Prius'

    # メソッド
    def print_name(self):
        print(self.name)


my_car = Car()  # インスタンス化
print(my_car.year)
my_car.print_name()

list_a = ['apple', 'banana', Car]
second_car = list_a[2]()
second_car.print_name()

help(Car)
