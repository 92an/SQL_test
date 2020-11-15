import os
import pymongo
from pymongo import MongoClient


if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celeberty"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFaliure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

# inserting example
""" new_docs = [{
    "first": "Terry",
    "last": "Pratchet",
    "dob": "28/04/1948",
    "gender": "M",
    "hair_color": "Not much",
    "occupation": "Writer",
    "nationality": "Brittish "
}, {
    "first": "George",
    "last": "RR Martin",
    "dob": "20/09/1948",
    "gender": "M",
    "hair_color": "White",
    "occupation": "Writer",
    "nationality": "American"
    }]

coll.insert_many(new_docs) """

documents = coll.find()

for doc in documents:
    print(doc)
