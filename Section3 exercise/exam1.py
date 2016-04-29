str=input("请输入字符串")
l=list(str)
o=[]
for i in l:
	print(ord(i))
	o.append(ord(i))

res=0
for i in l:
	res+=ord(i)
print(res)
print(o)


