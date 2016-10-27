class tester:
	def __init__(self, start):
		self.state = start
	def nested(self, label):
		print(label, self.state)
		self.state += 1

	# 直接调用
	def __call__(self, label):
		print(label, self.state)
		self.state += 1

F = tester(0)
F("allen")
F("bob")