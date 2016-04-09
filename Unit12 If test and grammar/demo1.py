x='abcd'
if 1:
	print('ok')
	print('continue')
	print('still')

if {}:
	print('true')
else:
	print("false")

a=x if 1 else 'Allen'
print(a) # abcd



b='' or x
print(b) # abcd

c=(('' and x) or 'Allen')
print(c) # Allen