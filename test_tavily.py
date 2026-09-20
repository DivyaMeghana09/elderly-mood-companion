import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

response = client.search(
    "simple safe activities for elderly people to stay engaged",
    search_depth="basic",
    max_results=3
)

print(response)