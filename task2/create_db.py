from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure


def connect_to_mongo(uri):
    try:
        client = MongoClient(uri)
        return client
    except ConnectionFailure as e:
        print(f"Error: {e}")
        exit(1)


def create_cat(db, collection_name, cat_data):
    try:
        collection = db[collection_name]
        collection.insert_one(cat_data)
    except OperationFailure as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    uri = "mongodb://localhost:27017/"
    client = connect_to_mongo(uri)
    db = client['cats_db']
    collection_name = 'cats'

    cat_data = {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"]
    }

    create_cat(db, collection_name, cat_data)

    cat_data = {
        "name": "black",
        "age": 5,
        "features": ["black"]
    }

    create_cat(db, collection_name, cat_data)

    client.close()