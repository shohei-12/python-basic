# 例外処理

try:
    b = [10, 20, 30]
    b.appen(40)
    a = b[3]
    a = 10 / 0
except ZeroDivisionError as e:
    # import traceback
    # traceback.print_exc()
    print(e, type(e))
except IndexError as e:
    print(e)
except Exception as e:
    print(e)

print('処理が完了しました！')

try:
    a = 10 / 0
except ZeroDivisionError as e:
    print(e)
else:
    print('エラーが発生しませんでした！！')
finally:
    print('必ず実行される処理です。')

# raise 例外自作


class MyException(Exception):
    pass


def devide(a, b):
    if b == 0:
        raise ZeroDivisionError('0では割り切れません！')
        # raise MyException('0では割り切れません！')
    else:
        return a / b


try:
    c = devide(10, 0)
except Exception as e:
    print(e, type(e))
