from pymongo import MongoClient
import pandas as pd

client = MongoClient()
db = client['DBName']
collection = db['CollectionName']

'''
If you have data in MongoDb like this:

[
    {
        "name": "Adam",
        "age": 27,
        "address":{
            "number": 4,
            "street": "Main Road",
            "city": "Oxford"
        }
     },
     {
        "name": "Steve",
        "age": 32,
        "address":{
            "number": 78,
            "street": "High Street",
            "city": "Cambridge"
        }
     }
]

You can put the data straight into a dataframe like this:
'''
df = pd.DataFrame(list(db.collection.find({}))

'''
And you will get this output:

df.head()

|    | name    | age  | address                                                   |
|----|---------|------|-----------------------------------------------------------|
| 1  | "Steve" | 27   | {"number": 4, "street": "Main Road", "city": "Oxford"}    |
| 2  | "Adam"  | 32   | {"number": 78, "street": "High St", "city": "Cambridge"}  |

However the subdocuments will just appear as JSON inside the subdocument cell. If you want to flatten objects so that subdocument properties are shown as individual cells you can use json_normalize without any parameters.
'''

datapoints = list(db.collection.find({})

df = json_normalize(datapoints)

'''
This will give the dataframe in this format:

|    | name   | age  | address.number | address.street | address.city |
|----|--------|------|----------------|----------------|--------------|
| 1  | Thomas | 27   |     4          | "Main Road"    | "Oxford"     |
| 2  | Mary   | 32   |     78         | "High St"      | "Cambridge"  |
'''
