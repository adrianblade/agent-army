import os
import asyncio

from langchain_openai import AzureChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv

load_dotenv()

# Retrieve Azure-specific environment variables
azure_openai_api_key = os.environ.get('AZURE_OPENAI_API_KEY')
azure_openai_endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
azure_openai_deployment_name = os.environ.get('AZURE_DEPLOYMENT_NAME')

# Initialize the Azure OpenAI client
llm = AzureChatOpenAI(
    model_name='gpt-4o', 
    openai_api_key=azure_openai_api_key,
    azure_endpoint=azure_openai_endpoint,  # Corrected to use azure_endpoint instead of openai_api_base
    deployment_name=azure_openai_deployment_name,  # Use deployment_name for Azure models
    api_version='2024-08-01-preview'  # Explicitly set the API version here
)

async def main():
    agent = Agent(
        task="Finds in https://shop.mango.com/es/es a white dresses and returns the price and urls",
        llm=llm,
    )
    await agent.run()

asyncio.run(main())