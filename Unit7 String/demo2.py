import sys
data = dict(platform=sys.platform, name ='Ellen')
res = 'My pc named {name:<3} runs {platform:>9}'.format(**data)
print(res)
#
res = '{0:,d}'.format(12345678)
print(res)
#
res = '{0:b}'.format((2**3)-1)
print(res)


for x in [1,2,3]:
	print(x, end=',')