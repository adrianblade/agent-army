import os

from agno.models.azure import AzureOpenAI
from agno.agent import Agent
from agno.tools.crawl4ai import Crawl4aiTools
from dotenv import load_dotenv

load_dotenv()

# Retrieve Azure-specific environment variables
azure_openai_api_key = os.environ.get('AZURE_OPENAI_API_KEY')
azure_openai_endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
azure_openai_deployment_name = os.environ.get('AZURE_DEPLOYMENT_NAME')


agent = Agent(
    model=AzureOpenAI(
        id="gpt-4o",
        api_version = '2024-08-01-preview',
        api_key = azure_openai_api_key,
        azure_endpoint = azure_openai_endpoint,
        azure_deployment = azure_openai_deployment_name
    ),
    tools=[Crawl4aiTools(max_length=None)],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Tell me about https://www.nike.com/es/hombre")