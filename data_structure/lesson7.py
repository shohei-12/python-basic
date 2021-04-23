# 文字列型

fruit = 'apple'
print(fruit, type(fruit))

print(fruit * 2)

new_fruit = fruit + ' banana'
print(new_fruit)

fruits = """apple
banana
grape
"""
print(fruits)

fruit = 'banana'
print(fruit[2])
print(fruit[-1])

# encode, decode => bytes[]
byte_fruit = fruit.encode('utf-8')
print(byte_fruit, type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit, type(str_fruit))

# count

msg = 'ABCDEABC'
print(msg.count('ABC'))

# startswith, endswith

print(msg.startswith('ABCD'))
print(msg.endswith('ABCD'))

# strip(両端), rstrip(右端), lstrip(左端)

msg = ' ABC '
print(msg)
print(msg.strip())
msg = 'ABCDEFABC'
print(msg.strip('CBA'))
print(msg.rstrip('CBA'))
print(msg.lstrip('CBA'))

# upper, lower, swapcase, replace, capitalize

msg = 'abcABC'
msg_u = msg.upper()
msg_l = msg.lower()
msg_s = msg.swapcase()  # 大文字小文字入れ替え
print(msg_u)
print(msg_l)
print(msg_s)

msg = 'ABCDEABC'
msg_r = msg.replace('ABC', 'FFF')
msg_r_1 = msg.replace('ABC', 'FFF', 1)  # 左から数えて1個目までを変換
msg_r_2 = msg.replace('ABC', 'FFF', 2)  # 左から数えて2個目までを変換
print(msg_r)
print(msg_r_1)
print(msg_r_2)

msg = 'hello, WoRld!'
print(msg.capitalize())

# 文字列の一部取り出し、islower、isupper

msg = 'hello, my name is taro'
print(msg[:5])
print(msg[5:])
print(msg[1:6])
print(msg[1:10:2])  # 一つ飛ばしで取り出す
print(msg[1:10:3])  # 二つ飛ばしで取り出す

msg = 'apple'
print(msg.islower())
print(msg.isupper())

# find, index, rfind(右端から検索), rindex(右端から検索)

msg = 'ABCDEABC'
print(msg.find('ABC'))
print(msg.rfind('ABC'))
print(msg.index('ABC'))
print(msg.rindex('ABC'))

print(msg.find('ABCE'))  # 見つからなかった時 => -1
print(msg.index('ABCE'))  # 見つからなかった時 => エラー
