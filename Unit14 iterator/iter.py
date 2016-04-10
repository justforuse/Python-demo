l=[1,2,3]
i=iter(l)
while True:
	try:
		x=next(i)
	except StopIteration:
		break
	print(x**2)

d={"name":"Allen","age":21,"gender":"male"}
for k in d:
	print(k,': ',d[k])