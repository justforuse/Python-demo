def commas(N):
	digits = str(N)
	assert(digits.isdigit())
	result=""
	while digits:
		digits, last3 = digits[:-3], digits[-3:]
		result = (last3 + "," + result) if result else last3

	return result

def money(N, width=0):
	sign = "-" if N < 0 else ""
	N = abs(N)
	whole = commas(int(N))
	fract = ("%.2f" % N)[-2:]
	format = "%s%s.%s" %(sign, whole,fract)
	return "$%*s" % (width, format)
print(money(99999999,0))