# print(x,y)
# 相当于
# sys.stdout.write(str(x) + ' ' + str(y) + '\n')

import sys
temp = sys.stdout
sys.stdout = open('log.txt','a')
a='Allen'
print(a)
b='Additional data'
print('add data: ',b)
sys.stdout.close()

sys.stdout = temp

print('Over!') #这会输出在控制台上

