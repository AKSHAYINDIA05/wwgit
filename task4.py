import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
load_dotenv()
client = AzureOpenAI(
    azure_endpoint="https://wwdstraining.openai.azure.com/",
    api_version="2024-05-01-preview",
    api_key="bb51630b53244471c8599b853799af9da"
)
 
search_service_endpoint = "https://acsr.search.windows.net"
search_index_name = "code_book_index"
search_api_key = "6oRambevEUx1NmYcfEXkXw9XxofANmxtgEe7bhKZX1AzSeCvUscV"
search_client = SearchClient(endpoint=search_service_endpoint, index_name=search_index_name, credential=AzureKeyCredential(search_api_key))
 
user_query = "place of illusion"
openai_prompt = f"check the spelling errors and correct the following : '{user_query}'"
response = client.chat.completions.create(
    model="langtest",
    messages=[{"role": "user", "content": openai_prompt+user_query}],
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
)
 
query=response.choices[0].message.content
print(query)
 
search_results = search_client.search(search_text=query, search_fields=["title"])
 
# Step 3: Print results
for result in search_results:
    print(result)
 
 