def maker(x):
	def action(y):
		print(x**y) 
	return action
f=maker(2)
f(3)