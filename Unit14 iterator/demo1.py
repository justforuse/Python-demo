f=open('data.txt')
print(f.__next__())
f.close()

for line in open('data.txt'):
	print(line.upper(), end="")