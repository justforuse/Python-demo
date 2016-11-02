a = list(filter((lambda x: x > 0), range(-5, 5)))
print(a)

# like for with if
b = [x for x in range(-5, 5) if x > 0]
print(b)
