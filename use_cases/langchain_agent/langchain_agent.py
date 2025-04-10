from langchain.agents import initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

llm = ChatOpenAI(temperature=0, model_name="gpt-4")

tools = load_tools(["llm-math", "serpapi"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

agent.run("What's the product of 17 and 42, and tell me a fun fact about the result.")

