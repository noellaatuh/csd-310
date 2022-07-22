import pymongo
from pymongo import MongoClient

url ="mongodb+srv://agwen:agwen@cluster0.bgnfg.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client["pytech"]

mycol = db["students"]



docs = mycol.find({})
 
print( "-- Displaying Students Documents From find() Query ..")
docs = mycol.find({})
 
for doc in docs:
 print("Student ID:", doc["student_id"])
 print("First Name:", doc["first_name"])
 print("Last Name:", doc["last_name"])
 print(" ")


myins = { "student_id":"1010", "first_name": "John", "last_name":"Doe"}
myins_student_id = mycol.insert_one(myins).inserted_id

doc1 = mycol.find_one({"student_id": "1010"})
print("-- INSERT STATEMENTS -- ")

print("Inserted student record ",doc1["first_name"]," ", doc1["last_name"]," into the students collection with document_id ",myins_student_id)

print( "-- Displaying Student Test Doc ..")

print("Student ID:", doc1["student_id"])
print("First Name:", doc1["first_name"])
print("Last Name:", doc1["last_name"])


mydel ={"student_id":"1010"}
mycol.delete_one(mydel)


print( "-- Displaying Students Documents From find() Query ..")
docs1 = mycol.find({})
 
for doc3 in docs1:
 print("Student ID:", doc3["student_id"])
 print("First Name:", doc3["first_name"])
 print("Last Name:", doc3["last_name"])
 print(" ")



print( "End of program, press any key to exit ....")




