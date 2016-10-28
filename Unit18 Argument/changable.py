def calc(*numbers):
	sum = 0;
	for i in numbers:
		sum+=i
	return sum

print(calc(*[1,2,3]))
print(calc())