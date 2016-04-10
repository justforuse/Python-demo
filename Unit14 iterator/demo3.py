lines=[line.rstrip() for line in open('data.txt') if line[0] == 'f']
print(lines)

a=sum([1,2,3])
print(a)

# 任何的项为真则返回真
b=any(['Allen','',4])
print(b)
# 所有的项为真才返回真
c=all(['Allen','',4])
print(c)

d=max([4,5,6,81,2,4])
print(d)

e=min([2,4,5,6,1,64])
print(e)

f=max(['a','bp','c'])
print(f) # c