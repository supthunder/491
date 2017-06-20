import pymongo
import sys
import copy

try:
	conn = pymongo.MongoClient('localhost:27017')
	db = conn.cmsc491
	# hlc = db.testSet
	# rs = hlc.find()
	# print rs[0]
except pymongo.errors.ConnectionFailure as e:
	print "problem connecting to cmsc491", e
	sys.exit(1)
# for res in rs:
# 	print res


# Create collections
# docs = ["Accounts.txt","Branch.txt","Customers.txt","Loans.txt"]
# colletions = [db.accounts, db.branch, db.customers, db.loans]

# # hlc = db.lab1
# for doc in range(0,len(docs)):
# 	hlc = colletions[doc]
# 	in_str = open(docs[doc]).read()
# 	in_lst = eval(in_str)
# 	for i in range(0, len(in_lst)):
# 		print in_lst[i]
# 		hlc.insert(in_lst[i])


print("Finding smith")
hlc = db.customers
q = {
	"name" : "Smith"
}
print("===============================")
rs = hlc.find(q)

if not rs:
	print "None found"
else:
	print rs
	for res in rs:
		print res
