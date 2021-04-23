# int str 変換

int_num = 12
str_num = str(int_num)
print(str_num, type(str_num))
float_num = -20.5
str_float = str(float_num)
print(str_float, type(str_float))

# str => int, float
msg = '12'
int_msg = int(msg)
float_msg = float(msg)

print(f'value={int_msg}, type={type(int_msg)}')
print(f'value={float_msg}, type={type(float_msg)}')
