import pymongo
import sys
import copy

try:
	conn = pymongo.MongoClient('localhost:27017')
	db = conn.lab1
except pymongo.errors.ConnectionFailure as e:
	print "problem connecting to cmsc491", e
	sys.exit(1)

conn.drop_database('lab1')


docs = ["Accounts.txt","Branch.txt","Customers.txt","Loans.txt"]
colletions = [db.accounts, db.branch, db.customers, db.loans]

# hlc = db.lab1
for doc in range(0,len(docs)):
	hlc = colletions[doc]
	in_str = open(docs[doc]).read()
	in_lst = eval(in_str)
	for i in range(0, len(in_lst)):
		print in_lst[i]
		hlc.insert(in_lst[i])

print("\n\n===============================")
print("Finding smith")

x = raw_input("continue? ")

hlc = db.customers
q = {
	"name" : "Smith"
}
p = {"_id":0}
rs = hlc.find(q,p)

if not rs:
	print "None found"
else:
	for res in rs:
		print res

print("\n\n===============================")
print("Finding smiths loans/ loan information")
x = raw_input("continue? ")
hlc = db.loans
q = {
	"customers" : "Smith"
}
p = {
	"_id": 0
}
rs = hlc.find(q,p)
if not rs:
	print "None found"
else:
	for res in rs:
		print res

print("\n\n===============================")
print("Branches that manage smiths loans")
x = raw_input("continue? ")
hlc = db.loans
q = {
	"customers":"Smith"
}
p = {
	"branch":1,
	"_id":0
}
rs = hlc.find(q,p)

if not rs:
	print "No joy on q,p"
else:
	for res in rs:
		print res


print("\n\n===============================")
print("Smiths accounts/account info")
x = raw_input("continue? ")
hlc = db.accounts
q = {
	"customers" : "Smith"
}
p = {
	"_id": 0
}
rs = hlc.find(q,p)
if not rs:
	print "None found"
else:
	for res in rs:
		print res
