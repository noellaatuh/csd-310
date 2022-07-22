import pymongo

myclient = pymongo.MongoClient("mongodb+srv://agwen:agwen@cluster0.bgnfg.mongodb.net/?retryWrites=true&w=majority")

db= myclient.test
mytable = db.student
x= mytable.find_one()
print(x)
