# map(f, iterable)
# 基本上等于：
# [f(x) for x in iterable]

func = lambda x : list(map(print, x))

print(func(['a','b','c']))

a = (lambda x:(lambda y: x+y))(100)(1)
print(a)