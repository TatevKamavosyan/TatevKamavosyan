from pymongo import MongoClient
import pprint
#client=MongoClient()
#print(client)
#db=client["rptutorials"]
#db=client.rptutorials
#tutorial=db.tutorial

#David_tutorial=tutorial.find_one({"author":"David"})
#pprint.pprint(David_tutorial)
with MongoClient() as client:
    db=client.rptutorials
    for doc in db.tutorial.find():
        pprint.pprint(doc)
        
