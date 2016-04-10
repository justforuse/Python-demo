l=[1,2,3,4,5]
l=[x+10 for x in l]
print(l)

a={i: line for (i, line) in enumerate(open('data.txt'))}
print(a) #{0: 's="Allen"\n', 1: 'for (offset, item) in enumerate(s):\n', 2: "\tprint(item,'at',offset)"}