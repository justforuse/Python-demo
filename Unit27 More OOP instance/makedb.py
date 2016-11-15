from embed import Person, Manager
bob=Person("Bob Smith")
sue=Person("Sue Jones", "dev", 10000)
allen=Manager("Allen Yuan", 30000)

import shelve
db=shelve.open("persondb")
for object in (bob, sue, allen):
	db[object.name] = object

db.close()