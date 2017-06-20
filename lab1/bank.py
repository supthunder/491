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

print("\n\n===============================")
print("Finding smith")
hlc = db.customers
q = {
	"name" : "Smith"
}
rs = hlc.find(q)

if not rs:
	print "None found"
else:
	for res in rs:
		print res

print("\n\n===============================")
print("Finding smiths loans/ loan information")
rs.rewind()
for res in rs:
	loanInfo = res.get('loans')
	print(loanInfo)


branches = []

hlc = db.loans
for loan in loanInfo:
	loan = {"loanNo":loan}
	rs = hlc.find(loan)
	if not rs:
		print "None found"
	else:
		for res in rs:
			print res
			branches.append(res['branch'])

print("\n\n===============================")
print("Finding smiths loans/ loan information V2")
hlc = db.loans
q = {
	"customers" : "Jones"
}
rs = hlc.find(q)

if not rs:
	print "None found"
else:
	for res in rs:
		print res
