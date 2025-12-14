from pymongo import MongoClient

# Connect to MongoDB running in Docker
client = MongoClient("mongodb://localhost:27017/")

# Create or use a database
db = client['mytestdb']

# Create or use a collection
collection = db['users']

# Insert a sample document
collection.insert_one({"name": "Suspense", "role": "Explorer"})

# Retrieve documents
for doc in collection.find():
    print(doc)
