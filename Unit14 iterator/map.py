m=map(str.upper, open("data.txt"))
print(list(m))

a=map(abs, (-1,3,0))
next(a) # 从索引1开始
for x in a:
	print(x) # 3 0