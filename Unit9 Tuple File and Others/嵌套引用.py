l=[1,2,3]
x=l*4
y=[l]*4
print(x)
print(y,'\n')

l[1]=0
print(x)
print(y)

#如果遇到一个复合对象包含指向自身的引用，就称之为循环对象
a=['Allen']
a.append(a)
print(a)