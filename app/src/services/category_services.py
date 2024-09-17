from src.repositories import category_repository
from src.services.catalog_emit_producer_services import publish_catalog_message

class CategoryServices():

    def __init__(self):
        self.category = category_repository.CategoryRepository()

    def select_category(self, id):
        try:
            select_output =  self.category.select_category(id)
            publish_catalog_message(select_output.ownerId)
            return select_output
        except Exception as e:
            return "Erro selecting: ".join(str(e))
    def create_category(self, category):
        try:
            create_output = self.category.create_category(category)
            publish_catalog_message(category.ownerId)
            return create_output
        except Exception as e:
            return "Erro creating: ".join(str(e))

    def update_category(self, category):
        try:
            update_output = self.category.update_category(category)
            publish_catalog_message(category.ownerId)
            return update_output
        except Exception as e:
            return "Erro updating: ".join(str(e))

    def delete_category(self, id):
        try:
            delete_output, ownerId = self.category.delete_category(id)
            publish_catalog_message(ownerId)
            return delete_output
        except Exception as e:
            return "Erro deleting: ".join(str(e))