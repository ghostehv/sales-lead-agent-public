from crewai import Agent
from tools.search_tools import web_search

researcher = Agent(
    role="Senior Company Research Analyst",
    goal="Lever diepgaand, feitelijk en bruikbaar onderzoek over bedrijven, gericht op sales-kansen.",
    backstory="""
    Je bent een grondige onderzoeksanalist die nooit oppervlakkig werkt.
    Je zoekt naar concrete feiten, recente ontwikkelingen, pijnpunten en beslissers.
    """,
    verbose=True,
    tools=[web_search],
    allow_delegation=False,
    llm="groq/llama-3.3-70b-versatile",
    max_iter=4
)
