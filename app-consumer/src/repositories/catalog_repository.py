import pymongo
from bson import ObjectId
import json


class CatalogRepository():

    def __init__(self) -> None:
        
        with open('src/config/mongo/mongodb.json', 'r') as file:
            mongodb = json.load(file)
        
        client = pymongo.MongoClient(mongodb['db']['url'])
        db = client[mongodb['db']['name']]
        self.collection_products = db.get_collection("products")
        self.collection_category = db.get_collection("categories")
    
    def get_by_owner(self, ownerId):
        products = self.collection_products.find({"ownerId":ownerId})
        categories = self.collection_category.find({"ownerId":ownerId})
        return (products, categories)
