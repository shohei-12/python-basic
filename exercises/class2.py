"""
継承とポリモーフィズムを用いた演習です。

Animalsクラスにspeakという抽象メソッドを定義します。

Dogクラスを作成して:speakメソッドを実行すると「わん」と表示します
Catクラスを作成して:speakメソッドを実行すると「にゃー」と表示します
Sheepクラスを作成して:speakメソッドを実行すると「めー」と表示します
Otherクラスを作成して:speakメソッドを実行すると「そんな動物いない」と表示します

ユーザーから入力を受け付け
1の場合はDogクラスのspeakメソッドを実行し
2の場合はCatクラスのspeakメソッドを実行し
3の場合はSheepクラスのspeakメソッドを実行し
それ以外はOthreクラスのspeakメソッドを実行します。
"""

from abc import ABCMeta, abstractmethod


class Animals(metaclass=ABCMeta):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animals):
    def speak(self):
        print('わん')


class Cat(Animals):
    def speak(self):
        print('にゃー')


class Sheep(Animals):
    def speak(self):
        print('めー')


class Other(Animals):
    def speak(self):
        print('そんな動物いない')


val = input('\n好きな動物はなんですか？\n1. 犬\n2. 猫\n3. 羊\n')
if val == '1':
    animal = Dog()
elif val == '2':
    animal = Cat()
elif val == '3':
    animal = Sheep()
else:
    animal = Other()

animal.speak()
