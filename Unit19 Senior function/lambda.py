# simple-demo
f = lambda a, b, c: a+b+c
print(f(1, 2, 3))

# default value
g = lambda a="aa", b="bb", c="cc": a+b+c
print(g("d"))

# jump table
L = [
    lambda x:x**2,
    lambda x:x**3,
    lambda x:x**4,
]
for f in L:
    print(f(2))

print(L[1](3))
