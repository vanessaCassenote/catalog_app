from bson.json_util import dumps

def catalog_handler(products, categories):
    catalog = {}
    catalog['catalog'] = [] 
    products_list = list(products)
    
    for cat in categories:  
        prod = []
        for p in products_list:
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



