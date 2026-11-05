import os
from tavily import TavilyClient

# Read API key securely from environment
api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    raise ValueError("Tavily API key not found!")

# Create Tavily client
client = TavilyClient(api_key=api_key)

def search_internet(query):
    response = client.search(
        query=query,
        search_depth="basic",
        max_results=3
    )

    for result in response["results"]:
        print("\nTitle:", result["title"])
        print("URL:", result["url"])
        print("Content:", result["content"][:300])

# Test the function
search_internet("rain forecast in hyderabd today")
