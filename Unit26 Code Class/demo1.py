class FirstClass:
	def setData(self, data):
		self.data=data
	def display(self):
		print(self.data)

x=FirstClass()
y=FirstClass()
x.setData("im x")
y.setData("im y")
x.display()
y.display()