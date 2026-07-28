from crewai import Agent
from pydantic import BaseModel, Field

class LeadScore(BaseModel):
    score: float = Field(..., description="Score van 0 tot 100")
    reasoning: str = Field(..., description="Korte, duidelijke motivatie")
    recommended_contact: str = Field(..., description="Beste functie om te benaderen")

qualifier = Agent(
    role="Strict Lead Qualifier",
    goal="Beoordeel leads objectief en streng. Alleen écht sterke leads krijgen een hoge score.",
    backstory="""
    Je bent een kritische sales analist die bekend staat om zijn hoge standaarden.
    Je geeft zelden scores boven de 80. Je kijkt naar fit, timing, pijnpunten en bereikbaarheid.
    Je bent eerlijk, direct en laat je niet beïnvloeden door optimistische aannames.
    Een score van 70+ betekent dat dit een serieuze, beldewaardige lead is.
    """,
    verbose=True,
    allow_delegation=False,
    llm="groq/llama-3.3-70b-versatile",
    max_iter=2
)
