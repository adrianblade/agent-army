import os
import asyncio

from agno.agent import Agent
from agno.models.azure import AzureOpenAI
from dotenv import load_dotenv
from agno.tools.mcp import MCPTools
from mcp import StdioServerParameters

load_dotenv()

azure_openai_api_key = os.environ.get('AZURE_OPENAI_API_KEY')
azure_openai_endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
azure_openai_deployment_name = os.environ.get('AZURE_DEPLOYMENT_NAME')


async def run_agent(message: str) -> None:
    """Run the GitHub agent with the given message."""

    time_server_params = StdioServerParameters(
        command="uvx",
        args=["mcp-server-time", "--local-timezone=Europe/London"],
    )

    async with MCPTools(server_params=time_server_params) as time_mcp_tools:
        agent = Agent(
            model=AzureOpenAI(
                id="gpt-4o",
                api_version = '2024-08-01-preview',
                api_key = azure_openai_api_key,
                azure_endpoint = azure_openai_endpoint,
                azure_deployment = azure_openai_deployment_name
            ),
            tools=[time_mcp_tools],
            markdown=True,
            show_tool_calls=True,
        )

        await agent.aprint_response(message, stream=True)



# Example usage
if __name__ == "__main__":
    # Pull request example
    asyncio.run(
        run_agent(
            "What is the current time in Zaragoza? What restaurants are open right now?"
        )
    )