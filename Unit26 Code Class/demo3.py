class FirstClass:
	def setData(self, data):
		self.data=data
	def display(self):
		print(self.data)

class SecondClass(FirstClass):
	def display(self):
		print('second data "%s" ' % self.data)


class ThirdClass(SecondClass):
	def __init__(self, value):
		self.data = value
	def __add__(self, other):
		return ThirdClass(self.data + other)
	def __str__(self):
		return "ThirdClass:%s" % self.data
	def mul(self, other):
		self.data *= other


x=ThirdClass("allen")

x.display()
print(x)

b=x+"haha"
b.display()
b.mul(2)
b.display()