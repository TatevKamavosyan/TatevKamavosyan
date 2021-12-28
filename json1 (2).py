import json

def SendJsonResponse(resultDict):
    print('convert Python dictonary into json formatted string')
    developer_str=json.dumps(resultDict)
    print(developer_str)

Developer_dict={
        'name':"Jane Doe",
        'salary':9000,
        'skills':['Python','Machin Learning','Web Developer'],
        'email':'jane.doe@py.com'
        }


SendJsonResponse(Developer_dict)

