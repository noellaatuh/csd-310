import pymongo
 
from pymongo import MongoClient





url ="mongodb+srv://admin:Agwen1234@cluster0.bgnfg.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)


db = client.pytech

print(db.list_collection_names)







 






