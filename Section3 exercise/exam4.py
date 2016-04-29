L=[1,2,4,8,16,32,64]
x=7
i=0
while i<len(L):
	if 2**x == L[i]:
		print("at index: ", i)
		break
	i+=1
else:
	print("not found")
