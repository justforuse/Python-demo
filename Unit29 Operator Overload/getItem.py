class Test:
	data = [5,6,7,8,9]
	def __getitem__(self, index):
		print("index: ", index)
		print(self.data[index])

x = Test()
x[1]
x[1:3]
x[:4]
x[2:]
x[::2]