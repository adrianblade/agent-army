import os

from agno.agent import Agent
from agno.models.azure import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

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
    markdown=True
)

# Print the response on the terminal
agent.print_response("Share a 2 sentence horror story.")