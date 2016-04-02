#
import sys
print('hello {1[name]}, your pc runs {0.platform}'.format(sys,{'age':21,'name':'Ellen'}))
#
l=list('abcd')
print('l: %s'%l)
parts=l[0],l[-1],l[1:3]
res = 'first={0}, last={1}, other={2}'.format(*parts)
print(res)
#
print('{0:.{1}f}'.format(1/3.0, 5))
#
res2='%.*f'%(4, 1/3.0)
print(res2)

#
template='%s, %s,%s'
res = template%('a','b','c')
print(res)