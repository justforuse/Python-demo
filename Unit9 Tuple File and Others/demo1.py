Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> t=tuple('Allen')
>>> t
('A', 'l', 'l', 'e', 'n')
>>> t.index('a')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t.index('a')
ValueError: tuple.index(x): x not in tuple
>>> t.index('e')
3
>>> t.index('l')
1
>>> t.count('e')
1
>>> t.count('l')
2
>>> 1,2
(1, 2)
>>> x=(10)
>>> x
10
>>> y=(10,)
>>> y
(10,)
>>> T=(1,2,3,2,4,2)
>>> T.index(2,3)
3
>>> T.index(2,4)
5
>>> T.index(2,6)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    T.index(2,6)
ValueError: tuple.index(x): x not in tuple
>>> T.index(2,5)
5
>>> q=(1,[2,3],4)
>>> q[1]='aa'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    q[1]='aa'
TypeError: 'tuple' object does not support item assignment
>>> q[1][0]='aa'
>>> q
(1, ['aa', 3], 4)
>>> t
('A', 'l', 'l', 'e', 'n')
>>> T
(1, 2, 3, 2, 4, 2)
>>> T.index(2)
1
>>> T.index(2,1)
1
>>> myfile=open('test.txt')
>>> myfile.readline()
'first line\n'
>>> myfile.readline()
'second line\n'
>>> myfile.read()
'third line\n4th line\n5th line'
>>> myfile.readline()
''
>>> myfile.seek(0,0)
0
>>> myfile.readlines()
['first line\n', 'second line\n', 'third line\n', '4th line\n', '5th line']
>>> myfile.readline()
''
>>> myfile.seek(1,0)
1
>>> myfile.readlines()
['irst line\n', 'second line\n', 'third line\n', '4th line\n', '5th line']
>>> myfile.write('aaa')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    myfile.write('aaa')
io.UnsupportedOperation: not writable
>>> f=open('multiline.txt','w')
>>> f.write('aaa')
3
>>> f.close()
>>> x,y,z=1,2,3
>>> x
1
>>> y
2
>>> z
3
>>> 
