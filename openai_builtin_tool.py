# OpenAI built-in tool example (web_search)

import json
from utils import get_client, get_model

client = get_client()

# Calling a built-in OpenAI tool

response = client.responses.create(
    model=get_model(),
    input="What are the latest news about Intel?",
    tools=[
        {
            "type": "web_search"
        }
    ]
)

# This request will trigger a web search.
# The response output includes several output fields (including annotations to network articles) 

print(json.dumps(response.output, default=lambda o: o.__dict__, indent=2))
