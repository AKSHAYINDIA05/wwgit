from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import QueryType
from dotenv import load_dotenv
import os
 
# Load environment variables from .env file
load_dotenv()
 
# Set your Azure Cognitive Search details
endpoint = "https://acsr.search.windows.net"
index_name = "resumeindex"
api_key =os.getenv("AZURE_SEARCH_API_KEY")  # Ensure your API key is set in .env file
  
# Create a SearchClient
search_client = SearchClient(
    endpoint=endpoint,
    index_name=index_name,
    credential=AzureKeyCredential(api_key)
)
 
# 1. Full-text Search on the Content Field
def full_text_search(search_text):
    search_results = search_client.search(search_text=search_text, query_type=QueryType.SIMPLE)
    print("\nFull-text Search Results:\n")
    for result in search_results:
        print(result)
 
# 2. Fuzzy Search for Handling Misspelled Queries
def fuzzy_search(search_text):
    search_results = search_client.search(search_text=search_text + "~", query_type=QueryType.SIMPLE)
    print("\nFuzzy Search Results:\n")
    for result in search_results:
        print(result)
 
#3. Filtering Based on Specific Fields
def filtered_search(title):
    try:
        search_results = search_client.search(
            search_text="*",
            filter=f"title eq '{title}'",  # Filter by title
            query_type=QueryType.SIMPLE
        )
        print(f"\nFiltered Search Results for title '{title}':\n")
        for result in search_results:
            print(result)
    except Exception as e:
        print(f"Error occurred: {str(e)}")
 
 
# Sample Queries
full_text_search("CDA")
fuzzy_search("TabLeAU")  # Intentional misspelling
filtered_search("Allen.pdf")