from pymongo import MongoClient
import pprint
client=MongoClient()
#print(client)
db=client["rptutorials"]
#db=client.rptutorials
tutorial=db.tutorial

#David_tutorial=tutorial.find_one({"author":"David"})
#pprint.pprint(David_tutorial)
for doc in tutorial.find():
     pprint.pprint(doc)
