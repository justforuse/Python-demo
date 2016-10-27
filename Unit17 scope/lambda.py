def func():
	x = 3
	action = lambda n, x=x:n**x
	return action

f = func()
print(f(3))