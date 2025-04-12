from langchain.chat_models import ChatOpenAI
from langchain.agents import tool
from langgraph.graph import END, StateGraph
from typing import TypedDict

llm = ChatOpenAI(model="gpt-4", temperature=0)

@tool
def research_tool(input: str) -> str:
    return f"Retrieved research info about: {input}"

@tool
def analysis_tool(info: str) -> str:
    return f"Key insights extracted from: {info}"

@tool
def writing_tool(insights: str) -> str:
    return f"Final report: {insights}"

class GraphState(TypedDict):
    query: str
    research: str
    analysis: str
    output: str

def research_step(state: GraphState) -> GraphState:
    query = state["query"]
    research = research_tool.run(query)
    return {**state, "research": research}

def analysis_step(state: GraphState) -> GraphState:
    research = state["research"]
    insights = analysis_tool.run(research)
    return {**state, "analysis": insights}

def writing_step(state: GraphState) -> GraphState:
    insights = state["analysis"]
    final_output = writing_tool.run(insights)
    return {**state, "output": final_output}

workflow = StateGraph(GraphState)
workflow.add_node("research", research_step)
workflow.add_node("analysis", analysis_step)
workflow.add_node("writing", writing_step)

workflow.set_entry_point("research")
workflow.add_edge("research", "analysis")
workflow.add_edge("analysis", "writing")
workflow.add_edge("writing", END)

app = workflow.compile()

result = app.invoke({"query": "autonomous drone coordination"})
print(result["output"])

