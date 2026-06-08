from qdrant_client import QdrantClient
from config import MARKDOWN_FILE, CHUNK_SIZE, CHUNK_OVERLAP, Qdrant_URL, collect_name


client = QdrantClient(url=Qdrant_URL)

if client.collection_exists(collection_name=collect_name):
    client.delete_collection(collection_name=collect_name)

