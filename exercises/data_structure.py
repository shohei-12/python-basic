# 1. numという変数に数値の10を入れてください
# 2. numの型を標準出力してください
# 3. 2のnumを文字列に変換して、num_strという変数に入れてください
# 4. リストnum_listにnum_strと'20', '30'を入れてください
# 5. num_listに新たな要素'40'を入れてください
# 6. num_listをタプルに変換してnum_tupleに格納してください
# 7. 標準入力を受け付けて、num_tupleに受け付けた標準入力を追加してください
# 8. セットnum_setを作成します。中身は'40', '50', '60'としてください
# 9. num_tupleとnum_setのユニオン（和集合）を表示してください（タプルをセット化するにはset（変数名）とします）
# 10. 辞書型num_dictをキーnum_tuple、値num_strとして作成してください
# 11. リストnum_listの長さを表示してください
# 12. num_dictからキー'MyKey'を取り出して見つからない場合は'Does not exist'を返すようにして標準出力してください
# 13. リストnum_listに新たに'50', '60'を一行で追加してください
# 14. 標準入力を受け付け、is_under_50という論理型変数に標準入力が50より小さいかどうかを入れてください
# 15. num_str = {num_strの値}として標準出力してください
# 16. num_dictが持っているメソッドを標準出力してください


# 1
num = 10

# 2
print(type(num))

# 3
num_str = str(num)

# 4
num_list = [num_str, '20', '30']
print(f'num_list:{num_list}')

# 5
num_list.append('40')
print(f'num_list:{num_list}')

# 6
num_tuple = tuple(num_list)

# 7
num_tuple += (input('50を入力してください'),)
print(f'num_tuple:{num_tuple}')

# 8
num_set = {'40', '50', '60'}
print(f'num_set:{num_set}')

# 9
print(set(num_tuple) | num_set)

# 10
num_dict = {num_tuple: num_str}
print(num_dict)

# 11
print(len(num_list))

# 12
print(num_dict.get('MyKey', 'Does not exist'))

# 13
num_list.extend(['50', '60'])
print(f'num_list:{num_list}')

# 14
val = input('数字を入力してください')
is_under_50 = int(val) < 50
print(f'is_under_50:{is_under_50}')

# 15
print('num_str = {}'.format(num_str))

# 16
print(dir(num_dict))
