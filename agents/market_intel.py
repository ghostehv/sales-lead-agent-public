from crewai import Agent
from tools.search_tools import web_search

market_intel = Agent(
    role="Market Intelligence Analyst",
    goal="Ontdek wat momenteel wél werkt en wat faalt in outreach binnen de niche.",
    backstory="""
    Je analyseert wat goed werkt in LinkedIn connection requests en follow-up DMs,
    en welke benaderingen falen of als spam worden gezien.
    Je levert korte, bruikbare inzichten.
    """,
    verbose=True,
    tools=[web_search],
    allow_delegation=False,
    llm="groq/llama-3.3-70b-versatile",
    max_iter=3
)
