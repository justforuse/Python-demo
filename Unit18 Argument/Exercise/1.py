def func1(a, b=4, c=5):
	print(a, b, c)
func1(1,2)

def func2(a, b,c=5):
	print(a,b,c)

func2(1, c=3,b=2)

def func3(a, *pargs):
	print(a, pargs)

func3(1,2,3)

def func4(a, **kargs):
	print(a, kargs)

func4(a=1, c=3, b=2)

def func5(a,b,c=3,d=4):
	print(a, b,c,d)

func5(1, *(5,6))

# 1 2 5
# 1 2 3
# 1 (2, 3)
# 1 {'b': 2, 'c': 3}
# 1 5 6 4