Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> while True:
	name=input('Enter name:')
	if name == 'stop': break
	age=input('Enter age:')
	print('Hello', name, 'age', int(age)*2)

	
Enter name:allen
Enter age:21
Hello allen age 42
Enter name:qe
Enter age:1
Hello qe age 2
Enter name:stop
>>> 
