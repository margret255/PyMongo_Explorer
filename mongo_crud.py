from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["mytestdb"]
users = db["users"]

def create_user(name, role):
    result = users.insert_one({"name": name, "role": role})
    return result.inserted_id

def read_users():
    return list(users.find())

def update_user(user_id, new_role):
    users.update_one({"_id": ObjectId(user_id)}, {"$set": {"role": new_role}})

def delete_user(user_id):
    users.delete_one({"_id": ObjectId(user_id)})

if __name__ == "__main__":
    uid = create_user("Neo", "Architect")
    print("Inserted:", uid)

    print("All users:")
    for user in read_users():
        print(user)

    update_user(uid, "Chosen One")
    print("Updated user")

    delete_user(uid)
    print("Deleted user")
