from tavily import TavilyClient
from langchain.tools import tool
from config.settings import settings

tavily = TavilyClient(api_key=settings.TAVILY_API_KEY)

@tool
def web_search(query: str) -> str:
    """Zoek actuele informatie over bedrijven en markten."""
    try:
        response = tavily.search(query=query, max_results=5)
        return str(response.get('results', []))
    except Exception as e:
        return f"Search error: {str(e)}"
