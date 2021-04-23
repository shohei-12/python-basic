# リスト内包表記

"""
ループと条件を使って、1行でリストを作成する方法
・リスト内包表記：[x for x in list]
・ジェネレータ：(x for x in list)
・タプル：tuple(x for x in list)
・セット：{x for x in list}
"""

tuple_a = (1, 2, 3, 'a', 4, 'b')

list_a = [x for x in tuple_a]
list_b = [x * 2 for x in tuple_a if type(x) == int]
list_c = [x for x in range(100) if x % 7 == 0]
print(list_a)
print(list_b)
print(list_c)

dict_a = {
    'a': 'Apple',
    'b': 'Banana'
}

list_d = [dict_a.get(x) for x in tuple_a if type(x) == str]
print(list_d)

gen_a = (x for x in range(10))
print(type(gen_a))

set_a = {x for x in range(10)}
print(set_a)

tuple_b = tuple(x for x in range(10))
print(tuple_b)


def func(n):
    for x in range(2, n):
        if n % x == 0:
            return True
        return False


list_a = [x for x in range(100) if func(x) is False]
list_b = [func(x) for x in range(100) if func(x) is False]
print(list_a)
print(list_b)
