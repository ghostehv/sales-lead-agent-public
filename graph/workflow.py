"""
LangGraph Workflow - Deterministic Sales Pipeline
=================================================
- Vaste volgorde van stappen
- Conditional edges alleen op harde Python-checks
- Voorbereid op human-in-the-loop (interrupt)
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
    approved_messages: List[dict]
    current_step: str
    error: Optional[str]


def find_leads(state: PipelineState) -> PipelineState:
    print("→ Stap 1: Lead Finder werkt...")
    state["current_step"] = "find_leads"
    state["companies"] = []
    return state


def research_companies(state: PipelineState) -> PipelineState:
    print("→ Stap 2: Researcher werkt...")
    state["current_step"] = "research"
    state["research"] = []
    return state


def market_intelligence(state: PipelineState) -> PipelineState:
    print("→ Stap 3: Market Intelligence werkt...")
    state["current_step"] = "market_intel"
    state["market_insights"] = ""
    return state


def qualify_leads(state: PipelineState) -> PipelineState:
    print("→ Stap 4: Qualifier werkt...")
    state["current_step"] = "qualify"
    state["scored_leads"] = []
    return state


def write_messages(state: PipelineState) -> PipelineState:
    print("→ Stap 5: Message Writer werkt (LinkedIn connectienotitie + DM)...")
    state["current_step"] = "write_messages"
    state["messages"] = []
    return state


def human_approval(state: PipelineState) -> PipelineState:
    print("→ Stap 6: Wachten op human approval...")
    state["current_step"] = "human_approval"
    # Hier komt later: interrupt()
    return state


def should_write_messages(state: PipelineState) -> str:
    """Deterministic check: alleen doorgaan bij score >= 70"""
    scored = state.get("scored_leads", [])
    good_leads = [lead for lead in scored if lead.get("score", 0) >= 70]

    if good_leads:
        return "write_messages"
    return "end"


def build_workflow():
    workflow = StateGraph(PipelineState)

    workflow.add_node("find_leads", find_leads)
    workflow.add_node("research", research_companies)
    workflow.add_node("market_intel", market_intelligence)
    workflow.add_node("qualify", qualify_leads)
    workflow.add_node("write_messages", write_messages)
    workflow.add_node("human_approval", human_approval)

    workflow.set_entry_point("find_leads")
    workflow.add_edge("find_leads", "research")
    workflow.add_edge("research", "market_intel")
    workflow.add_edge("market_intel", "qualify")

    workflow.add_conditional_edges(
        "qualify",
        should_write_messages,
        {
            "write_messages": "write_messages",
            "end": END
        }
    )

    workflow.add_edge("write_messages", "human_approval")
    workflow.add_edge("human_approval", END)

    return workflow.compile()
