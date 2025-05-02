import os

from agno.agent import Agent
from agno.tools.email import EmailTools
from dotenv import load_dotenv
from agno.models.azure import AzureOpenAI

load_dotenv()

azure_openai_api_key = os.environ.get('AZURE_OPENAI_API_KEY')
azure_openai_endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
azure_openai_deployment_name = os.environ.get('AZURE_DEPLOYMENT_NAME')

receiver_email = os.environ.get('RECEIVER_EMAIL')
sender_email = os.environ.get('SENDER_EMAIL')
sender_name = os.environ.get('SENDER_NAME')
sender_passkey = os.environ.get('SENDER_PASSKEY')

agent = Agent(
    model=AzureOpenAI(
        id="gpt-4o",
        api_version = '2024-08-01-preview',
        api_key = azure_openai_api_key,
        azure_endpoint = azure_openai_endpoint,
        azure_deployment = azure_openai_deployment_name
    ),
    tools=[
        EmailTools(
            receiver_email=receiver_email,
            sender_email=sender_email,
            sender_name=sender_name,
            sender_passkey=sender_passkey,
        )
    ]
)
agent.print_response("Send an email to {receiver_email}.")