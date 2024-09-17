from flask import jsonify, request
from app import app
import json
from src.config.aws.s3.aws_s3 import S3
from src.services.category_services import CategoryServices
from src.services.product_services import ProductServices
from src.adapters.handlers import id_handler, product_handler, category_handler, catalog_handler

# Refatorar essa parte
cat = CategoryServices()
prod = ProductServices()

@app.route("/catalog", methods=['POST'])
def get_catalog():
    
    data = request.json
    s3_access = S3().access()

    obj = s3_access.get_object(Bucket='bucket-catalog-json-vanessa', Key=data['ownerId']+".json")
    catalog_json = json.loads(obj['Body'].read())
    return catalog_json

@app.route("/prod", methods=['POST'])
def get_product():
    data = request.json
    status, msg = id_handler(data['id'])
    if(status):
        selected_prod = prod.select_product(data['id'])
        return str(selected_prod)
    return msg        

@app.route("/new_prod", methods=['POST'])
def create_product():
    data = request.json
    
    status, product, msg = product_handler(data)
    if(status):
        message = prod.create_product(product)
        return str(message)+":Product updated successfully!"
    return msg.join(message)

@app.route("/up_prod", methods=['POST'])
def update_product():
    data = request.json

    status, product, msg = product_handler(data)
    status2, msg2 = id_handler(data['id'])
    if(status and status2):
        product._id = data['id']
        message = prod.update_product(product)
        return str(message)+":Product updated successfully!"
    return msg.join(msg2)

@app.route("/del_prod", methods=['POST'])
def delete_product():
    data = request.json
    status, msg = id_handler(data['id'])
    if(status):
        message = prod.delete_product(data['id'])
        return str(message)+":Product deleted successfully!"
    return msg 

#------------------------------------------------------------

@app.route("/cat", methods=['POST'])
def get_category():
    data = request.json
    status, msg = id_handler(data['id'])
    if(status):
        selected_cat= cat.select_category(data['id'])
        return str(selected_cat)
    return msg        

@app.route("/new_cat", methods=['POST'])
def create_category():
    data = request.json
    
    status, category, msg = category_handler(data)
    if(status):
        message = cat.create_category(category)
        return str(message)+":Category created successfully!"
    return msg.join(message)

@app.route("/up_cat", methods=['POST'])
def update_category():
    data = request.json

    status, category, msg = category_handler(data)
    status2, msg2 = id_handler(data['id'])
    if(status and status2):
        category._id = data['id']
        message = cat.update_category(category)
        return str(message)+":Category updated successfully!"
    return msg.join(msg2)

@app.route("/del_cat", methods=['POST'])
def delete_category():
    data = request.json
    status, msg = id_handler(data['id'])
    if(status):
        message = cat.delete_category(data['id'])
        return str(message)+":Category deleted successfully!"
    return msg 
