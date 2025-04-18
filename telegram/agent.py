import os

from agno.agent import Agent
from agno.tools.telegram import TelegramTools
from dotenv import load_dotenv
from agno.models.azure import AzureOpenAI

load_dotenv()

azure_openai_api_key = os.environ.get('AZURE_OPENAI_API_KEY')
azure_openai_endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
azure_openai_deployment_name = os.environ.get('AZURE_DEPLOYMENT_NAME')

telegram_token = os.environ.get('TELEGRAM_TOKEN')
chat_id = os.environ.get('TELEGRAM_CHAT_ID')

agent = Agent(
    name="telegram",
    model=AzureOpenAI(
        id="gpt-4o",
        api_version = '2024-08-01-preview',
        api_key = azure_openai_api_key,
        azure_endpoint = azure_openai_endpoint,
        azure_deployment = azure_openai_deployment_name
    ),
    tools=[TelegramTools(token=telegram_token, chat_id=chat_id)],
)

agent.print_response("Send message to telegram chat a paragraph about the moon")