from crewai import Agent

qualifier = Agent(
    role="Strict Lead Qualifier",
    goal="Beoordeel leads objectief en streng. Alleen écht sterke leads krijgen een hoge score.",
    backstory="""
    Je bent een kritische sales analist met hoge standaarden.
    Scores boven 80 zijn zeldzaam. 70+ betekent serieuze, beldewaardige lead.
    """,
    verbose=True,
    allow_delegation=False,
    llm="groq/llama-3.3-70b-versatile",
    max_iter=2
)
