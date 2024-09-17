import pymongo
from bson import ObjectId
from src.models.category_model import Category
from src.repositories.base_repository import BaseRepository

class CategoryRepository():

    def __init__(self) -> None:
        catalog = BaseRepository()
        self.collection = catalog.collection_category

    def select_category(self, id) -> Category:
        return self.collection.find_one({"_id":ObjectId(id)})

    def create_category(self, category) -> int:
        dict = {"title":category.title,
                "description":category.description,
                "ownerId":category.ownerId}
        self.collection.insert_one(dict) 
        return 200

    def update_category(self, category) -> int:
        dict = {"title":category.title,
                "description":category.description,
                "ownerId":category.ownerId}
        self.collection.update_one(
            {"_id":ObjectId(category._id)},
            {'$set':{
            "title":category.title,
            "description":category.description
        }})
        return 200
    
    def delete_category(self, id) -> int:
        obj = self.select_category(id)
        self.collection.delete_one({"_id":ObjectId(id)})
        return 200, obj.ownerId
