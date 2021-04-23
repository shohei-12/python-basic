# inner関数, ノンローカル変数

"""
inner関数の用途
・外の関数の外からアクセスできないような関数を作成する -> 関数の処理を隠すことができる
・関数の中で同じ処理が何度も発生する場合に、一つにまとめる
・デコレータ関数を作成する

ノンローカル変数 -> 外側の関数の変数を参照できるようになる
"""


def outer():
    outer_value = '外側の変数'

    def inner():
        nonlocal outer_value
        outer_value = '内側の変数'
        print(f'inner:outer_value = {outer_value}, id = {id(outer_value)}')
    inner()
    print(f'outer:outer_value = {outer_value}, id = {id(outer_value)}')


outer()
# inner()  # エラーが発生する
