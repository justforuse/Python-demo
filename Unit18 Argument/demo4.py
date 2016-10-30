def func(a, *b, c=6, **d):
	print(a, b, c, d)

func(1,2,3,4,c=5,x=6,y=7)