# agno-playground

This directory contains examples and scripts to demonstrate the usage of the `agno` library for building AI agents with tools and models.

## Prerequisites

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up your environment variables by creating a `.env` file with the following keys:
   ```
   AZURE_OPENAI_API_KEY=<your_azure_openai_api_key>
   AZURE_OPENAI_ENDPOINT=<your_azure_openai_endpoint>
   AZURE_DEPLOYMENT_NAME=<your_azure_deployment_name>
   ```

## Example: `tool_use.py`

The `tool_use.py` script demonstrates how to use the `agno` library with Azure OpenAI and DuckDuckGo tools. Below is a brief explanation of the script:

1. **Initialize the Agent**:
   The agent is configured with the Azure OpenAI model and DuckDuckGo tools for web search.

2. **Environment Variables**:
   The script reads API keys and endpoints from the `.env` file.

3. **Run the Agent**:
   The agent is prompted to fetch the latest articles about Java using DuckDuckGo.

### Usage

Run the script with the following command:
```bash
python tool_use.py
```

### Example Output

The agent will fetch and display the latest articles about Java in a markdown-formatted response.

## Additional Information

For more details about the `agno` library and its capabilities, refer to the official documentation.
