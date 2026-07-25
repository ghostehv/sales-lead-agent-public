"""
Sales Lead Agent - Main Entry Point
===================================
Deterministic LangGraph pipeline.
"""

from dotenv import load_dotenv
load_dotenv()

from graph.workflow import build_workflow

SEARCH_CRITERIA = """
Nederlandse SaaS bedrijven tussen 10 en 50 medewerkers
die actief zijn in marketing automation of sales tools.
"""

def main():
    print("=" * 60)
    print("Sales Lead Agent (LangGraph) wordt gestart...")
    print("=" * 60)
    print(f"\nZoekcriteria:\n{SEARCH_CRITERIA.strip()}\n")

    print("→ LangGraph workflow wordt opgebouwd...")
    app = build_workflow()

    initial_state = {
        "criteria": SEARCH_CRITERIA,
        "companies": [],
        "research": [],
        "market_insights": "",
        "scored_leads": [],
        "messages": [],
        "approved_messages": [],
        "current_step": "start",
        "error": None
    }

    print("→ Pipeline start...\n")
    print("-" * 60)

    result = app.invoke(initial_state)

    print("-" * 60)
    print("\nPipeline afgerond.")
    print(f"Laatste stap: {result.get('current_step')}")

    return result


if __name__ == "__main__":
    main()
