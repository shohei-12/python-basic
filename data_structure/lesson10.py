# Dictionary

car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015, 1: 100}

print(car['brand'])
# print(car['bran']) # エラー
print(car.get('brand'))
print(car.get('bran'))  # None
print(car.get('bran', "Does'nt exist"))
print(car.get(1))

print(car.keys())
print(car.values())
print(car.items())

for key, v in car.items():
    print(f'key: {key} value: {v}')

if 'brand' in car:
    print('carのブランドは{}です。'.format(car['brand']))

# 辞書型のメソッド

tmp_car = {'country': 'Japan', 'prefecture': 'Aichi', 'model': 'カローラ'}

print(car)
car.update(tmp_car)  # 追加、更新
print(car)

car['city'] = 'Toyota-shi'
car['year'] = 2017
print(car)

value = car.popitem()
print(car)
print(value)

value = car.pop('model')
print(car)
print(value)

car.clear()
print(car)

del car
# print(car)  # エラー
