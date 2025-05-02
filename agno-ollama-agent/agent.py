from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Ollama(id="llama3.2:3b"),
    tools=[DuckDuckGoTools()],
    markdown=True
)
agent.print_response("What's happening in New York?", stream=True)