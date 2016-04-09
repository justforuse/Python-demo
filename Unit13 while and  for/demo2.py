s1='spam'
s2='scam'
res=[]
for x in s1:
	if x in s2:
		res.append(x)
print(res)

file = open('break.py')
print(file.read(1)) #read(1):读取一个字符