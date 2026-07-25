# Sales Lead Agent (Public)

Python AI multi-agent system for B2B lead finding, research, scoring and personalized outreach.

## Current Focus
- Deterministic LangGraph pipeline (no LLM deciding the flow)
- Strong research + scoring agents
- Human-in-the-loop before any outreach action
- Moving from cold email → LinkedIn Connection Route (safer & higher response)

## Architecture

```
Lead Finder → Researcher → Market Intelligence → Qualifier → Message Writer → Human Approval
```

- Hard Python checks (e.g. score >= 70)
- Prepared for LangGraph `interrupt()` before sending anything
- Tools: Tavily for search

## Agents
1. **Lead Finder** – Finds relevant companies
2. **Researcher** – Deep company research
3. **Market Intelligence** – What works / what fails in outreach
4. **Qualifier** – Scores leads 0-100 (strict)
5. **Writer** – Creates personalized connection notes + follow-up DMs
6. **Supervisor / Human Approval** – Final quality + reality check

## Tech Stack
- LangGraph (main orchestration)
- CrewAI agents
- Groq LLM
- Tavily Search
- Pydantic + SQLAlchemy

## Setup

1. Clone the repo
2. Copy `.env.example` to `.env` and add your keys:
   - GROQ_API_KEY
   - TAVILY_API_KEY
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python main.py
   ```

## Important Notes
- This version focuses on **preparation** of high-quality outreach (especially LinkedIn Connection Route).
- No automatic sending yet (by design – human approval required).
- LinkedIn automation is intentionally cautious due to high ban risk.

## Status
Work in progress. Core pipeline is deterministic and ready for further development.
