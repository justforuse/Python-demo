class Super:
	def __init__(self, data):
		self.data = data
	def __sub__(self, value):
		return Super(self.data - value)

