from qdrant_client import QdrantClient

def store_data(data):
    """
    Store data in Qdrant vector database.
    """
    client = QdrantClient()
    processed_data = preprocess_data(data)
    client.insert(processed_data)
