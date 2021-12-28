from pymongo import MongoClient
import pprint
client=MongoClient()

db=client["rptutorials"]

tutorial=db.tutorial

#David_tutorial=tutorial.find_one({"author":"David"})
#pprint.pprint(David_tutorial)
Lucas_tutorial=tutorial.find({"author":"Lucas"})
for i in Lucas_tutorial:
   pprint.pprint(i)
