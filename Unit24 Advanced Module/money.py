def commas(N):
	digits = str(N)
	assert(digits.isdigit())
	result=""
	while digits:
		digits, last3 = digits[:-3], digits[-3:]
		print(digits, last3)
		result = (last3 + "," + result) if result else last3
		print(result)
	return result

def money(N, width=0):
	sign = "-" if N < 0 else ""
	N = abs(N)
	whole = commas(int(N))
	print(whole)
	fract = ("%.2f" % N)[-2:]
	print(fract)
	format = "%s%s.%s" %(sign, whole,fract)
	return "$%*s" % (width, format)
print(money(1234567890.777,2))