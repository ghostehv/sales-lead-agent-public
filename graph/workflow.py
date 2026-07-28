"""
LangGraph Workflow - Max 4 agents + deterministic
=================================================
1. Researcher
2. Market Intelligence
3. Qualifier
4. Writer

Alleen harde Python-checks, geen LLM-supervisor.
"""

from typing import TypedDict, List, Optional
from langgraph.graph import StateGraph, END


class PipelineState(TypedDict):
    criteria: str
    companies: List[dict]
    research: List[dict]
    market_insights: str
    scored_leads: List[dict]
    messages: List[dict]
    current_step: str
    error: Optional[str]


# ============================================
# NODES
# ============================================

def researcher_node(state: PipelineState) -> PipelineState:
    """Stap 1: Vindt bedrijven + doet diep onderzoek"""
    print("→ Stap 1: Researcher werkt...")
    state["current_step"] = "researcher"
    # TODO: echte agent call
    state["companies"] = []
    state["research"] = []
    return state


def market_intel_node(state: PipelineState) -> PipelineState:
    """Stap 2: Wat werkt en wat faalt"""
    print("→ Stap 2: Market Intelligence werkt...")
    state["current_step"] = "market_intel"
    state["market_insights"] = ""
    return state


def qualifier_node(state: PipelineState) -> PipelineState:
    """Stap 3: Strenge scoring"""
    print("→ Stap 3: Qualifier werkt...")
    state["current_step"] = "qualifier"
    state["scored_leads"] = []
    return state


def writer_node(state: PipelineState) -> PipelineState:
    """Stap 4: Schrijft LinkedIn connectienotitie + DM"""
    print("→ Stap 4: Writer werkt...")
    state["current_step"] = "writer"
    state["messages"] = []
    return state


# ============================================
# HARD PYTHON CHECK
# ============================================

def should_write(state: PipelineState) -> str:
    """
    Alleen doorgaan naar Writer als er leads zijn met score >= 70.
    Geen LLM-oordeel.
    """
    scored = state.get("scored_leads", [])
    good_leads = [lead for lead in scored if lead.get("score", 0) >= 70]

    if good_leads:
        return "writer"
    return "end"


# ============================================
# GRAPH
# ============================================

def build_workflow():
    workflow = StateGraph(PipelineState)

    workflow.add_node("researcher", researcher_node)
    workflow.add_node("market_intel", market_intel_node)
    workflow.add_node("qualifier", qualifier_node)
    workflow.add_node("writer", writer_node)

    workflow.set_entry_point("researcher")
    workflow.add_edge("researcher", "market_intel")
    workflow.add_edge("market_intel", "qualifier")

    # Harde check
    workflow.add_conditional_edges(
        "qualifier",
        should_write,
        {
            "writer": "writer",
            "end": END
        }
    )

    workflow.add_edge("writer", END)

    return workflow.compile()
