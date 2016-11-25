x = 11
def f():
	print(x)
def g():
	x = 22
	print(x)
class C:
	x= 33
	def m(self):
		x=44
		self.x = 55
a = C()
print(a.x)
a.m()
print(a.x)
f()
g()
