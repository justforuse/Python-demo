def unpack(a,b,c,d):
	print(a,b,c,d,sep="&")

unpack(1,2,3,4)

unpack(*['a','b','c','d'])

x=(1,2)
y=(3,4)

a=list(zip(x,y))
print(a)

m,n=zip(*zip(x,y))
print(m)
print(n)