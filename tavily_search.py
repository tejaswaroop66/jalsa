import os
from tavily import TavilyClient

def search_internet(query):

    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        return {"error": "Tavily API key missing"}

    client = TavilyClient(api_key=api_key)

    response = client.search(
        query=query,
        search_depth="basic",
        max_results=3
    )

    return [
        {
            "title": item["title"],
            "url": item["url"],
            "content": item["content"][:500]
        }
        for item in response.get("results", [])
    ]