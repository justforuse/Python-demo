while True:
	reply = input('text:')
	if reply=='stop':break
	try:
		num =int(reply)
	except:
		print('Wrong!!')
	#这个else和try结合
	else:
		print(int(reply) ** 2)
	print('continue')
print('bye')

while True:
	reply = input('text:')
	if reply=='stop':break
	print(int(reply) ** 2)
print('bye')

while True:
	reply =input("enter:")
	if reply=='stop':
		break
	elif not reply.isdigit():
		print('error'*8)
	else:
		print(int(reply) ** 2)
print('Over')