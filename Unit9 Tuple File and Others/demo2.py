x,y,z=1,2,3
n='Allen'
d={'a':11,'b':22}
l=[4,5,6]

f=open('data.txt','w')
f.write(n+'\n')
f.write('%s,%s,%s\n' % (x,y,z))
f.write(str(l) + '$' + str(d) + '\n')
f.close

