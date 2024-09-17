import pymongo
from src.models.product_model import Product
from bson import ObjectId
from src.repositories.base_repository import BaseRepository

class ProductRepository():

    def __init__(self) -> None:
        catalog = BaseRepository()
        self.collection = catalog.collection_products
    
    def select_product(self, id) -> Product:
        return self.collection.find_one({"_id":ObjectId(id)})
    
    def create_product(self, product) -> int:
        dict = {"title":product.title,
                "description":product.description,
                "price":product.price,
                "category":product.category,
                "ownerId":product.ownerId}
        
        self.collection.insert_one(dict)   
        return 200
    
    def update_product(self, product) -> int:
        new_values = {"$set": {"title":product.title, 
                                "description":product.description,
                                "price":product.price,
                                "category": product.category,
                                "owner_id":product.ownerId}}
        prod = self.collection.update_one({"_id":ObjectId(product._id)}, new_values)  
        return 200

    def delete_product(self, id) -> int:
        obj = self.select_product(id)
        self.collection.delete_one({"_id":ObjectId(id)})
        return 200, obj.ownerId

