import json
import boto3

# Bedrock client used to interact with APIs around models
bedrock = boto3.client(
  service_name='bedrock', 
  region_name='eu-west-1'
)
  
# Bedrock Runtime client used to invoke and question the models
bedrock_runtime = boto3.client(
  service_name='bedrock-runtime', 
  region_name='eu-west-1'
)

def lambda_handler(event, context):
  
  prompt = "What is the capital of France?"
 
  # The payload to be provided to Bedrock 
  body = json.dumps(
    {
      "inputText": prompt, 
    }
  )
  
  # The actual call to retrieve an answer from the model
  response = bedrock_runtime.invoke_model(
    body=body, 
    modelId="amazon.titan-text-lite-v1", 
    accept="application/json", 
    contentType="application/json"
  )

  response_body = json.loads(response.get('body').read())

  # The response from the model now mapped to the answer
  answer = response_body.get('results')[0].get('outputText')
  
  return {
    'statusCode': 200,
    'headers': {
      'Access-Control-Allow-Headers': '*',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    },
      'body': json.dumps({ "Answer": answer })
    }
