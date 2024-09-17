import pymongo
from bson import ObjectId
import json

class BaseRepository():

    def __init__(self, database=None, host=None) -> None:
        with open('src/config/mongo/mongodb.json', 'r') as file:
            mongodb = json.load(file)

        client = pymongo.MongoClient(mongodb['db']['url'])
        db = client[mongodb['db']['name']]
        self.collection_products = db.get_collection("products")
        self.collection_category = db.get_collection("categories")