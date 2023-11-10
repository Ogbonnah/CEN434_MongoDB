import pymongo

# Creating the database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["students"]

# Adding to the database
mydict = [{ "_id": 1,"name": "Mmesoma", "Hall": "Dorcas", "Room":"D307", "Matric-number": "20CJ027466" },
           { "_id": 2, "name": "Ena", "Hall": "Esther", "Room":"F201", "Matric-number": "20CJ027444" },
            { "_id": 3, "name": "Ella", "Hall": "Deborah", "Room":"B408", "Matric-number": "20CJ027457" }, 
            { "_id": 4, "name": "Reigner", "Hall": "Dorcas", "Room":"E204", "Matric-number": "20CJ027439" },
            { "_id": 5, "name": "Paula", "Hall": "Mary", "Room":"F107", "Matric-number": "20CJ027421" }        
            ]

# x = mycol.insert_many(mydict)

# Deleting from the database
myquery = { "name": "Ella" }
mycol.delete_one(myquery)

# Adding a new record to the database
def add_new_record(mycol, record):

  result = mycol.insert_one(record)
  return result.inserted_id

  
# Prompt the user for the student's name.
name = input("Enter the student's name: ")

# Prompt the user for the student's hall.
hall = input("Enter the student's hall: ")

# Prompt the user for the student's room.
room = input("Enter the student's room: ")

# Prompt the user for the student's matric number.
matric_number = input("Enter the student's matric number: ")

# Create a new record dictionary.
new_record = {
  "name": name,
  "hall": hall,
  "room": room,
  "matric-number": matric_number
}
# Add the new record to the database.
new_record_id = add_new_record(mycol, new_record)

# Print a confirmation message.
print("New record added successfully!")
