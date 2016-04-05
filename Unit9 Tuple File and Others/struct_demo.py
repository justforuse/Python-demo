f=open('s_data.bin','wb')
import struct
s=b'Allen'
data=struct.pack('>i5si',7,s,8)
print(data)
f.write(data)
f.close()

a,b,c=struct.unpack('>i5si',data)
print(a,b,c)
b=b.decode('utf-8')
print(b)
f2=open('b.txt','w')
f2.write(b)
f2.close()