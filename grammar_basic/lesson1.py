# if文

"""
偽になる値（None, False, 0, '', 空のリスト, 空の辞書, 空のタプル, 空のセット）
bool()は内部で__bool__メソッドを呼んでいる。
"""


class ClassA():
    def __init__(self, a):
        self.a = a

    def __bool__(self):
        if self.a == 'a':
            return True
        return False


clsA = ClassA('a')
# clsA = ClassA('b')

bool_var = True
var = 0

print('boolの計算結果：{}'.format(bool(bool_var)))
print('boolの計算結果：{}'.format(bool(var)))
print('boolの計算結果：{}'.format(bool(clsA)))

if bool_var:
    print('if文の中の処理：bool_var')

if var:
    print('if文の中の処理：var')

msg = 'blue'
if msg == 'blue':
    print('すすめ')
elif msg == 'red':
    print('止まれ')
else:
    print('それ以外の処理')

age = 10
if age < 20:
    print('20未満です')
elif age <= 40:
    print('20以上40以下です')
elif age >= 60:
    print('60以上です')
else:
    print('それ以外の年齢')

gender = 'man'
age = 10
if gender == 'man' and age < 20:
    print('未成年男性です')

if gender == 'man' or age < 20:
    print('男性もしくは20未満です')

if not gender == 'man':
    print('女性です')

if gender != 'man':
    print('女性です')

# all, any

# all（反復可能オブジェクト（リストやタプル）の値が全て真の場合、True）
if all((10, 20, 30)):
    print('allの中の処理')

if not all((0, 20, 30)):
    print('allの中の処理')

# any（反復可能オブジェクト（リストやタプル）の値が一つでも真の場合、True）
if any((False, False, True)):
    print('anyの中の処理')

if not any((10 < 5, False, 'a' == 'b')):
    print('anyの中の処理')
