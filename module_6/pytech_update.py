import pymongo
from pymongo import MongoClient

url ="mongodb+srv://agwen:agwen@cluster0.bgnfg.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client["pytech"]

mycol = db["students"]


print( "-- Displaying Students Documents From find() Query ..")
docs = mycol.find({})
 
for doc in docs:
 print("Student ID:", doc["student_id"])
 print("First Name:", doc["first_name"])
 print("Last Name:", doc["last_name"])
 print(" ")


result = mycol.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

print( "-- Displaying Student Document 1007 ")

doc1  = mycol.find_one({"student_id": "1007"})
 

print("Student ID:", doc1["student_id"])
print("First Name:", doc1["first_name"])
print("Last Name:", doc1["last_name"])

print( "End of program, press any key to exit ....")




