import os
from azure.storage.queue import QueueClient

def enqueue_order(order_id: int):
    try:
        connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        if not connection_string:
            print("AZURE_STORAGE_CONNECTION_STRING not set")
            return
        queue_client = QueueClient.from_connection_string(
            conn_str=connection_string,
            queue_name="orders-queue"
        )
        queue_client.send_message(str(order_id))
        print(f"Order {order_id} enqueued successfully")
    except Exception as e:
        print(f"Error enqueuing order: {e}")
