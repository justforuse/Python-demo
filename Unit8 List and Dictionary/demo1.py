m = [[1,2,3],
	 [4,5,6],
	 [7,8,9]]
print(m)
print(m[1][1])

l = [1,2,3,4]
l[1:2] = []
print(l)

l = []
import random
x=0
while(x<7):
	l.append(random.randint(0,10))
	x=x+1


print(l)
print(x)

s=['a','b','c','d','e']
s.sort(reverse=True)
print(s)