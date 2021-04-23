# セット

set_a = {'a', 'b', 'c', 'd', 'a', 12}
print(set_a)
print('e' in set_a)
print('a' in set_a)
print('a' not in set_a)

print(len(set_a))

# add, remove, discard, pop, clear

set_a.add('A')
print(set_a)

set_a.remove('a')
print(set_a)
# set_a.remove('B')  # エラー
set_a.discard(12)
print(set_a)
set_a.discard(13)  # エラーにならない

val = set_a.pop()
print(val, set_a)

set_a.clear()
print(set_a)

s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

# 和集合
u = s | t  # u = s.union(t)
print(u)

# 積集合
u = s & t  # u = s.intersection(t)
print(u)

# 差集合
u = s - t  # u = s.difference(t)
print(u)

# 対象差
u = s ^ t  # u = s.symmetric_difference(t)
print(u)

# 要素の追加
s |= t
print(s)

# issubset, issuperset, isdisjoint
s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}
u = {'cherry'}

print(s.issubset(t))
print(t.issuperset(s))
print(t.isdisjoint(s))
print(t.isdisjoint(u))
