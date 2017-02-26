#!/Python27/python
import json
import pymongo

client = pymongo.MongoClient()
db = client.careem
data = db.Shipments.find()
fData = []
for i in data:
    i.pop('_id')
    fData.append(i)

print json.JSONEncoder().encode(fData)
