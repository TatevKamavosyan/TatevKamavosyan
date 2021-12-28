from pymongo import MongoClient
client=MongoClient()
db=client.rptutorial
tutorial=db.tutorial
tutorial2={
"title":"Python's Requests Library (Guide)",
"author":"Alex",
"contributors":[
"Aldren",
"Brad",
"Joanna"

],
"url":"https://realpython.com/python-requests/"
}

tutorial3={
"title":"Object-Oriented Programming (oop) in Python3",
"author":"David",
"contributors":[
"Aldren",
"Joanna",
"Jacob"

],
"url":"https://realpython.com/python3-object-oriented-programming/"
}
new_result=tutorial.insert_many([tutorial2,tutorial3])
print(F"Multiplite tutorials: {new_result.inserted_ids}")
