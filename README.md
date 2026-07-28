# Sales Lead Agent

Python AI multi-agent system for B2B lead finding, research, scoring and LinkedIn outreach preparation.

## Architecture (max 4 agents)

```
1. Researcher          → Vindt bedrijven + diep onderzoek
2. Market Intelligence → Wat werkt / wat faalt
3. Qualifier           → Strenge scoring (0-100)
4. Writer              → LinkedIn connectienotitie + follow-up DM
```

Daarna: **Human Approval** (jij beslist wat er verstuurd wordt).

### Belangrijke keuzes
- Maximaal 4 agents (voorkomt onderlinge ruis)
- Deterministic LangGraph flow
- Alleen harde Python-checks (`if score >= 70`)
- Geen LLM-supervisor
- Gericht op LinkedIn Connection Route

## Setup

1. Clone de repo
2. Kopieer `.env.example` naar `.env` en vul je keys in
3. Installeer dependencies:
```bash
pip install -r requirements.txt
```
4. Start:
```bash
python main.py
```

## Status
Core pipeline is deterministic en klaar voor verdere uitbouw.
