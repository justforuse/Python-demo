keys=["name", "age", "gender"]
values=["Allen", 21, "male"]
d={}
for (k,v) in zip(keys, values):
	d[k]=v
print(d)

# python 2.2+
d2=dict(zip(keys,values))
print(d2)