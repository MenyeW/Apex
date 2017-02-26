#!/Python27/python
import pymongo
from bson.objectid import ObjectId
print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

path_matrix = '';
import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)
path_matrix = mc.get("pathMatrix")

def RunScheduler(hub):
    client = pymongo.MongoClient()
    db = client.careem
    transactions = db.Transaction.find({"Location" : hub, "status" : "New"})
    for transaction in transactions:
        post = {"TransactionId" : (str)(transaction["_id"]),
                "CurrentLocation" : transaction["Location"],
                "From" : transaction["Location"],
                "To" : path_matrix[transaction["Location"]][transaction["dst"]][1]}
        db.Shipments.insert_one(post)
        db.Transaction.update_one({"_id" : transaction["_id"]}, {'$set' : {"status" : "Active"}}, upsert=False)
    shipments = db.Shipments.find({"CurrentLocation" : hub})
    for shipment in shipments:
        #print "Dispatching shipment " + str(shipment["_id"]) + " to: " + str(shipment["To"])
        dst = db.Transaction.find({"_id" : ObjectId(shipment["TransactionId"])})
        x = ''
        for i in dst:
            x = i
        nextHop = path_matrix[hub][x["dst"]][1]
        db.Shipments.update_one({"_id" : ObjectId(shipment["_id"])}, {'$set' : {"CurrentLocation" : "Transit", "From" : hub, "To" : nextHop}}, upsert=False)
        db.Transaction.update_one({"_id" : ObjectId(shipment["TransactionId"])}, {'$set' : {"Location" : "Transit"}}, upsert=False)
        #enqueue in Dispatch Queue

if __name__ == "__main__":
    RunScheduler("Delhi")
    RunScheduler("Himachal")
    RunScheduler("Mumbai")
    RunScheduler("Punjab")
    RunScheduler("Kolkata")
    
