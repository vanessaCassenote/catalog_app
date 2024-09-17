from src.repositories import product_repository
from src.services.catalog_emit_producer_services import publish_catalog_message

class ProductServices():

    def __init__(self):
        try:
            self.product = product_repository.ProductRepository()
            print("mongo connection done!")
        except Exception:
            print("Error on mongodb connection!")

    def select_product(self, id):
        try:
            select_output = self.product.select_product(id)
            publish_catalog_message(select_output.ownerId)
            return select_output
        except Exception as e:
            return "Erro selecting: ".join(str(e))
    def create_product(self, product):
        try:
            create_output = self.product.create_product(product)
            publish_catalog_message(product.ownerId)
            return create_output
        except Exception as e:
            return "Erro creating: ".join(str(e))

    def update_product(self, product):
        try:
            update_output = self.product.update_product(product)
            publish_catalog_message(product.ownerId)
            return update_output
        except Exception as e:
            return "Erro updating: ".join(str(e))

    def delete_product(self, id):
        try:
            delete_output, ownerId = self.product.delete_product(id)
            publish_catalog_message(ownerId)
            return delete_output
        except Exception as e:
            return "Erro deleting: ".join(str(e))