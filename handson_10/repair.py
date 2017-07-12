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
colletions = [db.mech, db.cars, db.test, db.test_mech, db.car_mech]

# hlc = db.lab1
for doc in range(0,len(docs)):
	hlc = colletions[doc]
	in_str = open(docs[doc]).read()
	in_lst = eval(in_str)
	for i in range(0, len(in_lst)):
		print in_lst[i]
		hlc.insert(in_lst[i])

print("\n\n===============================")
print("Finding Customer")

x = str(raw_input("Customer name (John Doe)? "))
car_id = ""

hlc = db.cars
q = {
	"customer_name" : "John Doe"
}
p = {"_id":0}
rs = hlc.find(q,p)

if not rs:
	print "None found"
else:
	for res in rs:
		car_id = res['id']

# get tests:
hlc = db.test
q = {
	"car_id" : car_id
}
p = {"_id":0}
rs = hlc.find(q,p)

if not rs:
	print "None found"
else:
	for res in rs:
		print res['testname']
