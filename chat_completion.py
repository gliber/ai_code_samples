# Chat completion example

from utils import get_client, get_model

client = get_client()

# Creating a chat without manually storing all old messages. Just adding the new user message!

response = client.responses.create(
    model=get_model(),
    input="tell me a joke",
)

print(response.output[0].content[0].text)
print(f"first response:\n{response.output[0].content[0].text}")

response = client.responses.create(
    model=get_model(),
    input="tell me another",
    previous_response_id=response.id
)

print(f"\n\nsecond response:\n{response.output[0].content[0].text}")
