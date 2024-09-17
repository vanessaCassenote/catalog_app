from src.config.rabbitmq.rabbitmq import RabbitMQ

def publish_catalog_message(ownerId):
    
    print("Trying to connect to rabbitmq")
    try:
        rabbitmq = RabbitMQ()
        rabbitmq.publish(queue_name='catalog_emit_queue', message=str(ownerId))
        print("Test message published successfully.")
    except Exception as e:
        print(f"Failed to publish test message: {e}")
    finally:
        rabbitmq.close()

#if __name__ == "__main__":
#    publish_catalog_message()