# LangChain Agent Example

This module demonstrates how to build an autonomous agent using [LangChain](https://python.langchain.com) for agentic AI tasks. The agent uses a tool-based approach to reason, plan, and execute actions dynamically.

## Key Features
- Tool-using agent architecture (ReAct or Plan-and-Execute)
- Integration with OpenAI/GPT
- Handles planning and execution loops

## Technologies
- LangChain
- OpenAI GPT-4
- Python 3.10+

## Example Use Case
A document question-answering agent that retrieves relevant text from a local vector store and explains it in plain language.

## How to Run

```bash
pip install -r requirements.txt
python langchain_agent.py

