import pymongo
import sys
import copy

try:
	conn = pymongo.MongoClient('localhost:27017')
	db = conn.lab2
except pymongo.errors.ConnectionFailure as e:
	print "problem connecting to cmsc491", e
	sys.exit(1)

conn.drop_database('lab2')


docs = ["Cars.txt","Mechanics.txt","Tests.txt","Car_Mechanic.txt", "Test_Mechanic.txt"]
colletions = [db.cars, db.mechanics, db.tests, db.car_mechanic, db.test_mechanic]

# hlc = db.lab1
for doc in range(0,len(docs)):
	hlc = colletions[doc]
	in_str = open(docs[doc]).read()
	in_lst = eval(in_str)
	for i in range(0, len(in_lst)):
		print in_lst[i]
		hlc.insert(in_lst[i])
