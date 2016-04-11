f=open('data.txt')
print(f.__next__())
f.close()

# 这是读取文件的最佳方式
for line in open('data.txt'):
	print(line.upper(), end="")