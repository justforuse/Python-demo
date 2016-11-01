def myCount(args):
	if not args:
		return 0
	else:
		return args[0] + myCount(args[1:])

print(myCount([1,2]))