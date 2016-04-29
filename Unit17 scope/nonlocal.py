def tester(start):
	state = start
	def nested(label):
		nonlocal state
		print(label, state)
		state += 1
	return nested
f=tester(0)
f('allen')
f('alice')