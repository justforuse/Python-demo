import struct
f=open('s_data.bin','rb')
data=f.read()
print(data)
a,b,c=struct.unpack('>i5si',data)
print(a,b,c)