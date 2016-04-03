l=list(zip(['name','age','gender'],['Ellen',21,'male']))
d=dict(zip(['name','age','gender'],['Ellen',21,'male']))
print(l)
print(d)

s={a:b for (a,b) in zip(['name','age','gender'],['Ellen',21,'male'])}
print(s)

d={x.lower():x + '!' for x in 'ABCD'}
print(d)
a=dict.fromkeys(['a','b','c'],1)
print(a)

#
for x in d.keys():
	print(x)

	