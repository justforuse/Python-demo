def makeActions():
	acts = []
	for i in range(5):
		acts.append(lambda x: i ** x)
	return acts

acts = makeActions()
print(acts[0](2))