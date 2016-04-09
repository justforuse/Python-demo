a,b,c=list(range(5)), list(range(2,6)), list(range(0,10,2))
print(a,b,c, sep="\n")
# [0, 1, 2, 3, 4]
# [2, 3, 4, 5]
# [0, 2, 4, 6, 8]

s='abcdefghijkl'
for c in s[::2]:
	print(c,end=" ")
# a c e g i k