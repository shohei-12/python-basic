# 一行のif、lambda

y = 10
x = 0 if y > 0 else 1
print(x)


def lambda_a(x): return x * x


print(lambda_a(10))


def lambda_b(x, y, z=5): return x * y * z


print(lambda_b(2, 3))
print(lambda_b(2, 3, 4))

# 条件付きlambda


def lambda_c(x, y): return y if x < y else x


print(lambda_c(10, 20))
print(lambda_c(20, 10))
