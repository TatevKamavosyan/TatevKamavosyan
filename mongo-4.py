from pymongo import MongoClient
import pprint
client=MongoClient()

db=client.rptutorials

tutorial=db.tutorial

David_tutorial=tutorial.find({"author":"David"})
for i in David_tutorial:
   pprint.pprint(i)

