import os
import asyncio

from langchain_openai import AzureChatOpenAI
from browser_use import Agent, Browser, BrowserConfig

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

browser = Browser(
	config=BrowserConfig(
		browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	)
)

async def main():
    agent = Agent(
        task="Go to in https://www.linkedin.com/feed/ a and give me a summary of the page",
        llm=llm,
        browser=browser,
    )
    await agent.run()
    await browser.close()
    input('Press Enter to close...')

if __name__ == '__main__':
    asyncio.run(main())