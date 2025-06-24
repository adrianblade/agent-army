import json
import boto3
import os

from agno.agent import Agent, RunResponse
from agno.models.aws import AwsBedrock
from agno.tools.duckduckgo import DuckDuckGoTools

bedrock_region = os.environ.get("AWS_REGION", "eu-west-1")
bedrock_client = boto3.client('bedrock-runtime', region_name=bedrock_region)


agent = Agent(
    model=AwsBedrock(
        id="eu.amazon.nova-micro-v1:0",
        client=bedrock_client,
    ),
    tools=[DuckDuckGoTools()],
    instructions="You are a helpful assistant that can use the following tools to answer questions.",
    show_tool_calls=True,
    markdown=True,
)

def lambda_handler(event, context):

    run_response: RunResponse =  agent.run("Whats new about Java?")

    #print(run_response.content)

    return {
    'statusCode': 200,
    'headers': {
      'Access-Control-Allow-Headers': '*',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    },
      'body': json.dumps({ "Answer": run_response.content })
    }
