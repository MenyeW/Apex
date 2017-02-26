#!/Python27/python
import pymongo
import sys
from bson.objectid import ObjectId

arguments = sys.argv
transactionId = arguments[1]
location = arguments[2]

client = pymongo.MongoClient()
data = client.careem.Transaction.find({'_id':ObjectId(transactionId)})
record = '';
for i in data:
    record = i;
trans = client.careem.Transaction
ship = client.careem.Shipments
if(record['dst'] == location):
    trans.update_one({'_id':ObjectId(transactionId)},{'$set':{'status':'Completed','Location':location}})
    ship.delete_one({'TransactionId':transactionId})
else:
    trans.update_one({'_id':ObjectId(transactionId)},{'$set':{'Location':location}})
    ship.update_one({'TransactionId':transactionId} ,{'$set':{'CurrentLocation':location,'From':'-','To':'-'}})
