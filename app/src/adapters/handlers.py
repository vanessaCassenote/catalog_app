from bson import ObjectId
from src.models.product_model import Product
from src.models.category_model import Category
from bson.json_util import dumps

def id_handler(data):
    try:
        ObjectId(data)
        return True, "Valid id"
    except TypeError:
        return False, "Not a valid ObjectId"


def product_handler(data):
    required_fields = ["title",
                       "description",
                       "price", 
                       "category",
                       "ownerId"]

    for f in required_fields:
        if((f not in data) or (data[f] == "")):
            return False, "", "Required field:{0} not found or empty!".format(f)
    
    Product.title = data['title']
    Product.description = data['description']
    Product.price = data['price']
    Product.category = data['category']
    Product.ownerId = data['ownerId']

    return True, Product, "All fields available!"

def category_handler(data):
    required_fields = ["title",
                       "description",
                       "ownerId"]

    for f in required_fields:
        if((f not in data) or (data[f] == "")):
            return False, "", "Required field:{0} not found or empty!".format(f)
    
    Category.title = data['title']
    Category.description = data['description']
    Category.ownerId = data['ownerId']

    return True, Category, "All fields available!"


def catalog_handler(products, categories):
    catalog = {}
    catalog['catalog'] = [] 
    
    for cat in categories:  
        prod = []
        for p in products:
            if(str(cat['_id']) == str(p['category'])):
                prod.append({'title':p['title'],
                'description':p['description'],
                'price':p['price']})

        catalog['ownerId'] = cat["ownerId"]
        catalog_tmp = {
            "category_title":cat['title'],
            "category_description":cat['description'],
            "items":prod
         }
        catalog['catalog'].append(catalog_tmp)
    return catalog



