#!/Python27/python

import sys
from pymongo import MongoClient

arguments = sys.argv
client = MongoClient()
db = client.careem
result = db.Transaction.insert_one(
    {
        "ClientID" : arguments[1],
        "src" : arguments[2],
        "dst" : arguments[3],
        "status" : "New",
        "Location" : arguments[2],
        "cost" : arguments[4]
    }
)
