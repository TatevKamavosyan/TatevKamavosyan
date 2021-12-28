from pymongo import MongoClient
client=MongoClient()
#print(client)
db=client["rptutorials"]
#db=client.rptutorials
tutorial1={
    "title": "Working With JSON Data in python",
    "author": "Lucas",
    "contributors": [
        "Aldren",
        "Dan",
        "Joanna"
    ],
    "url": "https://realpython.com/python-json/"
}
tutorial=db.tutorial
#print(tutorial)
result=tutorial.insert_one(tutorial1)
print(result)
