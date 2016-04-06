a,b,c='abc'
print(a,b,c,sep='..') #a..b..c
print(a,b,c,end='.over.\n') #a b c.over.
#直接输出到文件中控制台不输出
print(a,b,c,sep=',',end='/over\n',file=open('print.txt','a'))

import sys
sys.stdout.write('hello world')