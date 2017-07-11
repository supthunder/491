import pymongo
import sys
import copy

try:
	conn = pymongo.MongoClient('localhost:27017')
	db = conn.repair
except pymongo.errors.ConnectionFailure as e:
	print "problem connecting to cmsc491", e
	sys.exit(1)

# conn.drop_database('repair')

x = raw_input("Load accounts? ")
docs = ["mech.txt","cars.txt","test.txt"]
colletions = [db.mech, db.cars, db.test]

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

x = str(raw_input("Customer name? "))

hlc = db.customers
q = {
	"name" : x
}
p = {"_id":0}
rs = hlc.find(q,p)

if not rs:
	print "None found"
else:
	for res in rs:
		print res

# print("\n\n===============================")
# print("Finding smiths loans/ loan information")
# x = raw_input("continue? ")
# hlc = db.loans
# q = {
# 	"customers" : "Smith"
# }
# p = {
# 	"_id": 0
# }
# rs = hlc.find(q,p)
# if not rs:
# 	print "None found"
# else:
# 	for res in rs:
# 		print res

# print("\n\n===============================")
# print("Branches that manage smiths loans")
# x = raw_input("continue? ")
# hlc = db.loans
# q = {
# 	"customers":"Smith"
# }
# p = {
# 	"branch":1,
# 	"_id":0
# }
# rs = hlc.find(q,p)

# if not rs:
# 	print "No joy on q,p"
# else:
# 	for res in rs:
# 		print res


# print("\n\n===============================")
# print("Smiths accounts/account info")
# x = raw_input("continue? ")
# hlc = db.accounts
# q = {
# 	"customers" : "Smith"
# }
# p = {
# 	"_id": 0
# }
# rs = hlc.find(q,p)
# if not rs:
# 	print "None found"
# else:
# 	for res in rs:
# 		print res
