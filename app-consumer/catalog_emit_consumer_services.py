from src.config.rabbitmq.rabbitmq import RabbitMQ
import sys
import json
from src.config.aws.s3.aws_s3 import S3
from src.repositories.catalog_repository import CatalogRepository
from src.handlers import catalog_handler

def callback(ch, method, properties, body):
    print(f"Received message: {body}")
    ownerId = body.decode("utf-8")

    # get all results from database
    catalog = CatalogRepository()
    products, categories = catalog.get_by_owner(ownerId)
    catalog_json = catalog_handler(products, categories)

    # save on s3
    s3_access = S3().access()
    
    s3_access.put_object(
        Bucket='bucket-catalog-json-vanessa', 
        Key=ownerId+".json",
        Body=json.dumps(catalog_json)
    )
    print("Saved on S3")

def consumer_catalog_message():
    rabbitmq = RabbitMQ()
    try:
        print("Connection to RabbitMQ established successfully.")
        rabbitmq.consume(queue_name='catalog_emit_queue', callback=callback)

    except Exception as e:
        print(f"Failed to establish connection to RabbitMQ: {e}")
        sys.exit(1)
    finally:
        rabbitmq.close()

if __name__ == "__main__":
    consumer_catalog_message()