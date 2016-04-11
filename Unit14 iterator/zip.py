z=zip((1,2,3),(7,8,9))
for x in z:
	print(x)

z=zip((1,2,3),(7,8,9))
for x in list(z):
	print(x)

# 以下代码无输出，个人理解list(是一个迭代)
z=zip((1,2,3),(7,8,9))
list(z)
for x in z:
	print(x)