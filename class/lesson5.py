# 特殊メソッド

class Human:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return self.name + ',' + str(self.age) + ',' + self.phone_number

    def __eq__(self, other):
        return (
            self.name == other.name
        ) and (self.phone_number == other.phone_number)

    def __hash__(self):
        return hash(self.name + self.phone_number)

    def __bool__(self):
        return True if self.age >= 20 else False

    def __len__(self):
        return len(self.name)


man = Human('Taro', 20, '08011111111')
man2 = Human('Taro', 18, '08011111111')
man3 = Human('Jirokichi', 18, '09011111111')
print(man)  # 内部で__str__を実行

print(man == man2)  # 内部で__eq__を実行
print(hash('Taro'))
print(hash('Taro'))
print(hash('Jiro'))

set_man = {man, man2, man3}  # 内部で__hash__を実行
for x in set_man:
    print(x)

if man:  # 内部で__bool_を実行
    print('manはTrue')

if man2:  # 内部で__bool__を実行
    print('man2はTrue')

print(len(man))  # 内部で__len__を実行
print(len(man3))  # 内部で__len__を実行
