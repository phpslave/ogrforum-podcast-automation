from qdrant_client import QdrantClient

def preprocess_data(data):
    """
    Placeholder function to preprocess data.
    """
    # Example preprocessing: convert to lowercase and split into chunks
    processed_data = data.lower().split('.')
    return [chunk.strip() for chunk in processed_data if chunk]

def store_data(data):
    """
    Store data in Qdrant vector database.
    """
    client = QdrantClient()
    processed_data = preprocess_data(data)
    client.insert(processed_data)
