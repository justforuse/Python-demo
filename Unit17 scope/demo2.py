x=88
def func():
	global x
	x=99

func()
print(x)

a,b=1,2
def all_global():
	global c
	c=a+b

all_global()
print(c)