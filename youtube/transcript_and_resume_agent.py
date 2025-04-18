import os
from agno.agent import Agent
from agno.team.team import Team
from agno.models.azure import AzureOpenAI
from dotenv import load_dotenv
from agno.tools import tool
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()

azure_openai_api_key = os.environ.get('AZURE_OPENAI_API_KEY')
azure_openai_endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
azure_openai_deployment_name = os.environ.get('AZURE_DEPLOYMENT_NAME')

@tool()
def get_transcript(video_id: str) -> str:
    return "\n".join([seg.text for seg in YouTubeTranscriptApi().fetch(video_id)])


agent = Agent(
    model=AzureOpenAI(
        id="gpt-4o",
        api_version = '2024-08-01-preview',
        api_key = azure_openai_api_key,
        azure_endpoint = azure_openai_endpoint,
        azure_deployment = azure_openai_deployment_name
    ),
    show_tool_calls=True,
    tools=[get_transcript],
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions. The response should be in spanish language.",
)

agent.print_response(
    "Summarize captations of this video https://www.youtube.com/watch?v=Iv9dewmcFbs&t", markdown=True
)

# https://github.com/hassanbadawy/agno-cookbook/blob/5a46e4686c91eaf7849af963851d760f593b2bac/examples/agents/youtube_kb.py#L4