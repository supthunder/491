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
elif set.count() == 1:
    print ("Found 1 result: Car ID = " + set[0]['_id'])
    car_id = set[0]['_id']
else:
    i = 1
    print ("Found " + str(set.count()) + " results:")
    for i, result in enumerate(set):
        print (str(i+1) + ". ID = " + result['_id'] + "  License # = " + result['license_tag'] )
    
    entry = input("Choose result #: ")
    set.rewind()
    car_id = set[entry-1]['_id']



# get tests:
set = db.test.find({'car_id' : car_id})

print ("\nTests run on " + car_id + ":")
if not set:
    print "None found"
else:
    for result in set:
        print ("Test ID: " + result['_id'])
