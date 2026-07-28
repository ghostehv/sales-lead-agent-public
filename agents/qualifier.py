from crewai import Agent
from pydantic import BaseModel, Field

class LeadScore(BaseModel):
    score: float = Field(..., description="Score van 0 tot 100")
    reasoning: str = Field(..., description="Korte motivatie")
    recommended_contact: str = Field(..., description="Beste functie om te benaderen")

qualifier = Agent(
    role="Strict Lead Qualifier",
    goal="Beoordeel leads objectief en streng. Alleen écht sterke leads krijgen een hoge score.",
    backstory="""
    Je bent een kritische sales analist met hoge standaarden.
    Scores boven 80 zijn zeldzaam.
    Een score van 70+ betekent dat dit een serieuze lead is.
    Je laat je niet beïnvloeden door optimistische aannames.
    """,
    verbose=True,
    allow_delegation=False,
    llm="groq/llama-3.3-70b-versatile",
    max_iter=2
)
