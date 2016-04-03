Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l=dict.fromkeys(['a','b','c'],[1,2,3])
>>> l
{'c': [1, 2, 3], 'a': [1, 2, 3], 'b': [1, 2, 3]}
>>> l=dict(['a','b','c'],[1,2,3])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    l=dict(['a','b','c'],[1,2,3])
TypeError: dict expected at most 1 arguments, got 2
>>> l=dict([('a','b','c'),(1,2,3)])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    l=dict([('a','b','c'),(1,2,3)])
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> l=dict([('a',1),('b',2),('c',3)])
>>> l
{'c': 3, 'a': 1, 'b': 2}
>>> k=l.keys()
>>> k
dict_keys(['c', 'a', 'b'])
>>> k.sort()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    k.sort()
AttributeError: 'dict_keys' object has no attribute 'sort'
>>> k=list(k)
>>> k
['c', 'a', 'b']
>>> k.sort()
>>> k
['a', 'b', 'c']
>>> for x in k:
	print(x,l[x])

	
a 1
b 2
c 3
>>> l
{'c': 3, 'a': 1, 'b': 2}
>>> k
['a', 'b', 'c']
>>> k=l.keys()
>>> k
dict_keys(['c', 'a', 'b'])
>>> for x in sorted(k):
	print(x,l[x])

	
a 1
b 2
c 3
>>> m=sorted(l)
>>> m
['a', 'b', 'c']
>>> for x in m:
	print(x,l[x])

	
a 1
b 2
c 3
>>> r=dict.fromkeys(['a','b'],0)
>>> r
{'a': 0, 'b': 0}
>>> [0]*5
[0, 0, 0, 0, 0]
>>> 
