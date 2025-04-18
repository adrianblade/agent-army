# YouTube Transcript and Resume Agent

This project provides a Python-based agent that utilizes the YouTube Transcript API and Azure OpenAI to fetch YouTube video transcripts and summarize them in Spanish. The agent is designed to interact with users, obtain video captions, and provide concise summaries.

## Features

- **Fetch YouTube Transcripts**: Extract captions from YouTube videos using the `YouTubeTranscriptApi`.
- **Summarization in Spanish**: Summarize the fetched captions in Spanish using Azure OpenAI's GPT-4 model.
- **Tool Integration**: Implements a custom tool for fetching transcripts.
- **Interactive Agent**: The agent can respond to user queries and provide markdown-formatted responses.

## Requirements

- Python 3.8+
- Azure OpenAI API credentials
- YouTube Transcript API
- `dotenv` for environment variable management

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd agent-army/youtube
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your Azure OpenAI credentials:
   ```env
   AZURE_OPENAI_API_KEY=your_api_key
   AZURE_OPENAI_ENDPOINT=your_endpoint
   AZURE_DEPLOYMENT_NAME=your_deployment_name
   ```

## Usage

Run the `transcript_and_resume_agent.py` script to interact with the agent:

```bash
python transcript_and_resume_agent.py
```

The agent will fetch the captions of the specified YouTube video and provide a summary in Spanish.

## Example

Input:
```
Summarize captions of this video https://www.youtube.com/watch?v=Iv9dewmcFbs&t
```

Output:
```
Resumen de los subtítulos del video...
```

## References

- [YouTube Transcript API Documentation](https://github.com/jdepoix/youtube-transcript-api)
- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)

## License

This project is licensed under the MIT License.