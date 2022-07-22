import pymongo
from pymongo import MongoClient

url ="mongodb+srv://agwen:agwen@cluster0.bgnfg.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client["pytech"]

mycol = db["students"]

myins = { "student_id":"1007", "first_name": "Thorin", "last_name":"Oakenshield"}
myins1 =  { "student_id":"1008", "first_name": "Bilbo", "last_name":"Baggins"}
myins2 =  { "student_id":"1009", "first_name": "Frodo", "last_name":"Baggins"}


myins_student_id = mycol.insert_one(myins).inserted_id
myins1_student_id = mycol.insert_one(myins1).inserted_id
myins2_student_id = mycol.insert_one(myins2).inserted_id

doc1 = mycol.find_one({"student_id": "1007"})
doc2 = mycol.find_one({"student_id": "1008"})
doc3 = mycol.find_one({"student_id": "1009"})

print("-- INSERT STATEMENTS -- ")

print("Inserted student record ",doc1["first_name"]," ", doc1["last_name"]," into the students collection with document_id ",myins_student_id)

print("Inserted student record ",doc2["first_name"]," ",doc2["last_name"]," into the students collection with document_id ",myins1_student_id)

print("Inserted student record ",doc3["first_name"]," ", doc3["last_name"]," into the students collection with document_id ",myins2_student_id)

print( "End of program, press any key to exit ....")