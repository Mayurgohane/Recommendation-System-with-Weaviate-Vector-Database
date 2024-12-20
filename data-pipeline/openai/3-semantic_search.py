import os
import weaviate
from weaviate.classes.init import AdditionalConfig, Timeout

WEAVIATE_CLUSTER_URL = os.getenv('WEAVIATE_CLUSTER_URL') 
WEAVIATE_API_KEY = os.getenv('WEAVIATE_API_KEY') 
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = weaviate.Client(
    url=WEAVIATE_CLUSTER_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
    additional_headers={"X-OpenAI-Api-Key": OPENAI_API_KEY})

print(client.is_connected())

book_collection = client.collections.get(name="Book")

# Semantic Search

response = book_collection.query.near_text(
    query="biology",
    limit=3
)

print()
for book in response.objects:
    print(book.properties['title'])
    print(book.properties['description'])
    print(book.properties['categories'])
    print('---')
