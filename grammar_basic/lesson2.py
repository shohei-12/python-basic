# for

for i in range(10):
    print(i)

for _ in range(5):
    print('A')

for i in range(2, 20, 3):
    print(i)

sample = ['John', 'Paul', 'George', 'Ringo']
for member in sample:
    print(member)

human = {
    'Name': 'Taro',
    'Age': 20,
    'gender': 'man'
}

for h in human:
    print(h, human.get(h))

# enumerate, zip, while

fruits = ['grape', 'pine', 'apple']
for index, value in enumerate(fruits):
    print(index, value)

classA = ['Taro', 'Hanako', 'Jiro']
classB = ['Katsuo', 'Wakame', 'Tara']
for A, B in zip(classA, classB):
    print(f'classA student: {A}')
    print(f'classB student: {B}')

count = 0
while count < 5:
    print(count)
    count += 1

print('######################')

for i in range(10):
    if i == 3:
        continue
        # break
    print(i)
else:
    print('ループ処理終了')

num = 0
while num < 10:
    if num == 5:
        num += 1
        continue
    # if num == 7:
    #     break
    print(num)
    num += 1
else:
    print(('whileループ終了'))
