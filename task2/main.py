from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure


def connect_to_mongo(uri):
    try:
        client = MongoClient(uri)
        return client
    except ConnectionFailure as e:
        print(f"Error: {e}")
        exit(1)


def read_all_records(db, collection_name):
    collection = db[collection_name]
    try:
        for record in collection.find():
            print(record)
    except OperationFailure as e:
        print(f"Error: {e}")


def find_cat_by_name(db, collection_name, name):
    collection = db[collection_name]
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("Cat is not found")
    except OperationFailure as e:
       print(f"Error: {e}")


def update_cat_age(db, collection_name, name, new_age):
    collection = db[collection_name]
    try:
        result = collection.update_one(
            {"name": name}, {"$set": {"age": new_age}})
        if result.modified_count:
            print("Cat age is updated")
        else:
            print("Cat age is not updated")
    except OperationFailure as e:
        print(f"Error: {e}")


def add_feature_to_cat(db, collection_name, name, feature):
    collection = db[collection_name]
    try:
        result = collection.update_one(
            {"name": name}, {"$addToSet": {"features": feature}})
        if result.modified_count:
            print("Feature is added")
        else:
            print("Feature is not added")
    except OperationFailure as e:
        print(f"Error: {e}")


def delete_cat_by_name(db, collection_name, name):
    collection = db[collection_name]
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print("Cat was deleted")
        else:
            print("Cat is not found")
    except OperationFailure as e:
        print(f"Error: {e}")


def delete_all_records(db, collection_name):
    collection = db[collection_name]
    try:
        collection.delete_many({})
        print("All cats are removed")
    except OperationFailure as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    uri = "mongodb://localhost:27017/"
    client = connect_to_mongo(uri)
    db = client['cats_db']
    collection_name = 'cats'

    read_all_records(db, collection_name)

    find_cat_by_name(db, collection_name, "black")

    update_cat_age(db, collection_name, "black", 14)

    add_feature_to_cat(db, collection_name, "black", "vip_feature")

    read_all_records(db, collection_name)

    delete_cat_by_name(db, collection_name, "black")

    delete_all_records(db, collection_name)

    read_all_records(db, collection_name)

    client.close()