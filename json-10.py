import json


developerInfo = """{
    "id": 23,
    "name": "jane doe",
    'skills': 9000,
    "email": "JaneDoe@pynative.com",
    "experience": {"python": 5, "data Science": 2},
    "projectinfo": [{"id": 100, "name": "Intelect analiz Data"}]
}
"""

print("Started reading nested JSON array")
developerDict=json.loads(developerInfo)

print("Project name: ", developerDict["projectinfo"][0]["name"])
print("Experience: ", developerDict["experience"]["python"])

print("Done reading nested JSON Array")
