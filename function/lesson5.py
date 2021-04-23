# ジェネレータ関数

"""
ジェネレータ関数
def func():
    yield ○○

・ジェネレータ関数を宣言して実行すると、yieldの部分で処理がストップし、yieldの○○に記載された値（配列、辞書等オブジェクト）が呼び出し元に返される
・その後、再度ジェネレータ関数を呼び出すと、yieldの部分から処理がスタートし、次のyieldの部分でストップする
・プログラムが終了するまで、何度もジェネレータ関数を呼び出すことができる

メソッド
send()：値を送出
throw()：例外を発生させる
close()：終了させる
"""


def generator(max):
    print('ジェネレータ作成')
    for n in range(max):
        yield n
        print('yield実行')


gen = generator(10)
n = next(gen)
print(f'n = {n}')
n = next(gen)
print(f'n = {n}')

for x in gen:
    print(f'x = {x}')


def generator(max):
    print('ジェネレータ作成')
    for n in range(max):
        try:
            x = yield n
            print(f'x = {x}')
            print('yield実行')
        except ValueError as e:
            print(e)


gen = generator(10)
print(next(gen))
print(next(gen))
print(gen.send(100))
print(gen.throw(ValueError('Invalid Value')))
gen.close()
next(gen)
