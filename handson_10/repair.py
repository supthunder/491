import pymongo
import sys
import copy

try:
	conn = pymongo.MongoClient('localhost:27017')
	db = conn.repair
except pymongo.errors.ConnectionFailure as e:
	print "problem connecting to cmsc491", e
	sys.exit(1)

conn.drop_database('repair')

x = raw_input("Load accounts? ")
docs = ["mech.txt","cars.txt","test.txt","test_mech.txt","car_mech.txt"]
collections = [db.mech, db.cars, db.test, db.test_mech, db.car_mech]

for doc in range(0,len(docs)):
	col = collections[doc]
	in_str = open(docs[doc]).read()
	in_lst = eval(in_str)
	for i in range(0, len(in_lst)):
		print in_lst[i]
		col.insert(in_lst[i])

# Composite index to ensure no duplicates in many-to-many tables
db.test_mech.create_index([("test_id", pymongo.ASCENDING), 
                           ("mech_id", pymongo.ASCENDING)], unique=True)

db.car_mech.create_index([("car_id", pymongo.ASCENDING), 
                          ("mech_id", pymongo.ASCENDING)], unique=True)



print("\n\n===============================")
print("Query A: Find customer & display tests run on their car")

name = str(raw_input("Enter customer name (ex. John Doe): "))
car_id = ""

set = db.cars.find({'customer_name' : name})

if not set:
	print "None found"
else:

	for result in set:
		car_id = result['_id']


# get tests:

#get list of all test IDs for a given car
set = db.test.distinct('_id', {'car_id' : car_id})

if not set:
	print "None found"
else:
	for result in set:
            print ("Test ID: " + result)



print("\n\n===============================")
print("Query B: Find mechanics who worked on " + name + "'s car")

q = {
    "test_id":{ "$in": set }
}
p = {
    "mech_id":1
}
set = db.test_mech.find(q,p).distinct("mech_id")

if not set:
	print "None found"
else:
	for result in set:
		print result




print("\n\n===============================")
print("Query C: Find all cars that underwent a certain test type:")
x = str(raw_input("Enter test type(ex. transmission): "))

# Need distinct() since the same car could be output twice if it had multiple
# tests of the same type performed
set = db.test.distinct('car_id', {'test_type' : x})

if not set:
	print "None found"
else:
	for result in set:
		print result
