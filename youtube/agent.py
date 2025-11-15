import os

from agno.agent import Agent
from agno.models.azure import AzureOpenAI
from agno.tools.youtube import YouTubeTools
from agno.tools.reasoning import ReasoningTools
from dotenv import load_dotenv

load_dotenv()

# Configuración de Azure
azure_openai_api_key = os.environ.get('AZURE_OPENAI_API_KEY')
azure_openai_endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
azure_openai_deployment_name = os.environ.get('AZURE_DEPLOYMENT_NAME')

youtube_agent = Agent(
    model=AzureOpenAI(
        id="gpt-4o",
        api_version='2024-08-01-preview',
        api_key=azure_openai_api_key,
        azure_endpoint=azure_openai_endpoint,
        azure_deployment=azure_openai_deployment_name
    ),
    tools=[YouTubeTools(), ReasoningTools(),],
    description="You are a YouTube agent that has the special skill of understanding YouTube videos and summarize them.",
    markdown=True,
)

if __name__ == "__main__":
    youtube_agent.print_response(
        "Analyze this video: https://www.youtube.com/watch?v=mZzAuFq5C6Q and return the resume in spanish", stream=True
)
