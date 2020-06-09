from pymongo import MongoClient
print("Hello from docker container")

# Setup a connection, by default the port that will be used = 27017
client = MongoClient("mongodb://172.18.0.1:27017/")     # When both Mongo and This application is running on Docker and we are using Docker Compose
#client = MongoClient("mongodb://localhost:27017/")   # When only Mongo DB is running on Docker.
# client = MongoClient("mongodb://mymongo:27017/")     # When both Mongo and This application is running on Docker and we are using Docker Compose
print(client)
print(client.server_info())

# Choose the database
db = client['IshmeetDB']
print(db)
# Choose the document, create a database cursor
people = db['people']

# people.insert_one({"name":"Ishmeet"})
# Querying in the document
cursor = people.find()

for data in cursor:
    print(data)

print("Finished")

