x='Allen'
while x:
	print(x, end=" ")
	x=x[1:]  #finally x = ''
print("\n")
n=10
while n:
	n=n-1
	if n%2 != 0:
		continue
	print(n, end=" ")

for i in 'abcd':
	print(i, end=" ")

T=[(1,2),(3,4),(5,6)]
for o in T:
	print(o)

a,*b,c=(1,2,3,4,5)
print(a,b,c)