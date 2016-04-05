file=open('data.txt')
try:
	for line in file:
		print(line)

finally:
	file.close()