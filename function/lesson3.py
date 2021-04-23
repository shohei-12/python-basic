# グローバル変数

def printAnimal():
    # global animal
    animal = 'Cat'
    print(f'関数内animal = {animal}, id = {id(animal)}')


animal = 'Dog'
printAnimal()
print(f'関数外animal = {animal}, id = {id(animal)}')
