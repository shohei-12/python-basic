"""
数値を1~100までループさせて

数値が3の倍数の場合は
数値：Fizz

数値が5の倍数の場合は
数値：Buzz

数値が3かつ5の倍数の場合は
数値：Fizz Buzz

それ以外は数値のみ表示

と表示する処理を作成してください
"""

for i in range(100):
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i}：Fizz Buzz')
    elif i % 3 == 0:
        print(f'{i}：Fizz')
    elif i % 5 == 0:
        print(f'{i}：Buzz')
    else:
        print(i)

# range(1, 101)も可
