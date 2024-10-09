from azure.core.credentials import AzureKeyCredential 
from azure.search.documents import SearchClient
from azure.search.documents.models import QueryType
from dotenv import load_dotenv
import os
 
# Load environment variables from .env file
load_dotenv()
 
# Set your Azure Cognitive Search details
endpoint = "https://acsr.search.windows.net"
index_name = "code_book_index"
api_key = os.getenv("AZURE_SEARCH_API_KEY")  # Ensure your API key is set in .env file
 
# Create a SearchClient
search_client = SearchClient(
    endpoint=endpoint,
    index_name=index_name,
    credential=AzureKeyCredential(api_key)
)
 
# Sample book data
books = [
    {"bookid": '1', 
    "title": "Palace of Illusions",
    "genre": "Fiction",
    "author": "Chitra Banerjee Divakaruni",
    "description": "The Mahabharata in Draupadi's POV",
    "year": '2008'
    }
    , 
    {"bookid": '2', 
    "title": "Into the Waters",
    "genre": "Murder Mystery",
    "author": "Paula Hawkins",
    "description": "About a woman who goes missing in a water body",
    "year": '2017'
    }
    ,
    {"bookid": '3', 
    "title": "Girl on the train",
    "genre": "Thriller",
    "author": "Paula Hawkins",
    "description": "A woman witnesses a shocking event on a train, uncovering dark secrets.",
    "year":  '2015'

    }
]
 
# Upload documents
upload_result = search_client.upload_documents(documents=books)
if all(doc.succeeded for doc in upload_result):
    print(f"Successfully uploaded {len(upload_result)} document(s).")
else:
    for doc in upload_result:
        if not doc.succeeded:
            print(f"Failed to upload: {doc.error_message}")
 
# Perform a search query
search_results = search_client.search(search_text="*", query_type=QueryType.SIMPLE)
 
# Print search results
print("\nSearch results:")
for result in search_results:
    print(f"bookid: {result['bookid']}, title: {result['title']}, genre: {result['genre']}, "
          f"author: {result['author']}, description: {result['description']}, year: {result['year']}")

