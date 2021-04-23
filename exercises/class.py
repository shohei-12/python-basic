"""
キャラクターを作成して戦わせます。

Characterクラスを作成し、インスタンス変数として
name(名前), hp(ヒットポイント), offence(攻撃), defence(守備)を持たせます。

attackメソッドを実行すると、敵インスタンスのHPが自分のoffence - 敵のdefence分減ります。
(自分のoffence - 敵のdefenceがマイナスの場合は1)

critical_hitメソッドを実行すると、attackメソッドの倍のダメージを与えます。

HPが0になると死んでしまい、攻撃ができなくなります。

AllCharactersクラスを作成します。クラス変数が3個存在します。

all_characters:現在作成されているすべてのキャラクターの配列
alive_characters:現在生きているすべてのキャラクターの配列
dead_characters:現在死んでいるすべてのキャラクターの配列

もし同じ名前のキャラクターを登録した場合は、CharacterAlreadyExistExceptionを作成して返してください。
"""


class CharacterAlreadyExistException(Exception):
    pass


class Character:
    def __init__(self, name, hp, offence, defence):
        self.name = name
        self.hp = hp
        self.offence = offence
        self.defence = defence

    def attack(self, enemy):
        if self.hp == 0:
            return print('hpが0のため攻撃ができません')
        elif enemy.hp == 0:
            return print('相手はすでに瀕死です')

        damage = self.offence - enemy.defence
        if damage < 0:
            enemy.hp -= 1
        else:
            enemy.hp -= damage
            if enemy.hp < 0:
                enemy.hp = 0

    def critical_hit(self, enemy):
        if self.hp == 0:
            return print('hpが0のため攻撃ができません')
        self.attack(enemy)
        self.attack(enemy)


a = Character('a', 50, 30, 5)
b = Character('b', 50, 10, 10)
a.critical_hit(b)
a.critical_hit(b)
b.critical_hit(a)
print(b.hp)


class AllCharacters:
    all_characters = []
    alive_characters = []
    dead_characters = []

    @classmethod
    def add_characters(cls, characters):
        cls.alive_characters.clear()
        cls.dead_characters.clear()
        for character in characters:
            if character.name not in cls.all_characters:
                cls.all_characters.append(character.name)
            if character.hp > 0 and character.name not in cls.alive_characters:
                cls.alive_characters.append(character.name)
            if character.hp == 0 and character.name not in cls.dead_characters:
                cls.dead_characters.append(character.name)

    @classmethod
    def add_all_characters(cls, characters):
        for character in characters:
            if character in cls.all_characters:
                raise CharacterAlreadyExistException('同じ名前のキャラクターがすでに存在します')
            cls.all_characters.append(character)

    @classmethod
    def add_alive_characters(cls, characters):
        for character in characters:
            if character in cls.alive_characters:
                raise CharacterAlreadyExistException('同じ名前のキャラクターがすでに存在します')
            cls.alive_characters.append(character)

    @classmethod
    def add_dead_characters(cls, characters):
        for character in characters:
            if character in cls.dead_characters:
                raise CharacterAlreadyExistException('同じ名前のキャラクターがすでに存在します')
            cls.dead_characters.append(character)


# AllCharacters.add_all_characters([a.name, b.name])
# AllCharacters.add_alive_characters(a.name)
# AllCharacters.add_dead_characters(b.name)

AllCharacters.add_characters([a, b])
print(AllCharacters.all_characters)
print(AllCharacters.alive_characters)
print(AllCharacters.dead_characters)

a.hp = 0
b.hp = 1
AllCharacters.add_characters([a, b])

print(AllCharacters.all_characters)
print(AllCharacters.alive_characters)
print(AllCharacters.dead_characters)
