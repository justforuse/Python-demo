class FirstClass:
	def setData(self, data):
		self.data=data
	def display(self):
		print(self.data)

class SecondClass(FirstClass):
	def display(self):
		print('second data "%s" ' % self.data)

x=SecondClass()
x.setData("allen")
x.display()