import json
sampleDict={
    'colorlist':['red','green','blue'],
    'carTuple':('BMW','Audi','range rover'),
    'samplesString':'pynative.com',
    'sampleFloat':225.48,
    'booleantrue':True
    }
resultJSON=json.dumps(sampleDict)
print('done converting python primitive types into JSON')
print(resultJSON)
      
