# LangGraph Multi-Agent Orchestration

This use case demonstrates a modular agentic pipeline using [LangGraph](https://python.langchain.com/docs/langgraph/) to simulate collaboration between multiple agents.

## Agents:
- **Research Agent**: retrieves external knowledge
- **Analysis Agent**: summarizes and interprets findings
- **Writer Agent**: creates structured output from insights

## Key Features:
- Directed graph execution of agents
- Modular and composable architecture
- Enables goal-based collaboration

## How to Run

```bash
pip install -r ../../requirements.txt
python langgraph_orchestration.py


