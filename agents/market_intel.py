from crewai import Agent
from tools.search_tools import web_search

market_intel = Agent(
    role="Market Intelligence Analyst",
    goal="Ontdek wat momenteel wél werkt en wat faalt in LinkedIn outreach binnen de niche.",
    backstory="""
    Je analyseert wat goed werkt bij LinkedIn connectieverzoeken en follow-up DMs.
    Je zoekt naar succesvolle korte notities, goede openingszinnen,
    en fouten die je moet vermijden.
    Je levert korte, concrete inzichten die de Writer direct kan gebruiken.
    """,
    verbose=True,
    tools=[web_search],
    allow_delegation=False,
    llm="groq/llama-3.3-70b-versatile",
    max_iter=3
)
