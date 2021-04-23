# ファイル入力

file_path = 'resources/input.csv'
f = open(file_path, mode='r', encoding='utf-8')

line = f.read()  # 中身をすべて読み込む
print(line)

lines = f.readlines()  # 中身を配列で読み込む
print(lines)
for x in lines:
    print(x.rstrip('\n'))

line = f.readline()  # 1行ずつ読み込む
while line:
    print(line.rstrip('\n'))
    line = f.readline()

while (line := f.readline()):  # セイウチ演算子使用
    print(line.rstrip('\n'))

f.close()  # クローズをしないと、メモリを食う。他の処理でファイルを開けない。

with open(file_path, mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
