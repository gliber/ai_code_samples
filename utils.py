import os
import re
import openai
import llama_index.llms.azure_openai as llama_azure_openai
import llama_index.agent.openai as llama_openai

USE_OPEN_AI_AZRUE = False


def get_client():    
    """ relies on API key and endpoint in env vars """
    if USE_OPEN_AI_AZRUE:
        client = openai.AzureOpenAI(
            azure_endpoint=os.getenv("AZ_OPENAI_API_BASE"),
            api_key=os.getenv("AZ_OPENAI_API_KEY"),
            api_version=os.getenv("AZ_OPENAI_API_VERSION"),
        )
    else:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return client

def get_model():
    if USE_OPEN_AI_AZRUE:
        print(f" ====== {os.getenv("AZ_OPENAI_LLM") }"   )
        return os.getenv("AZ_OPENAI_LLM")    
    else:
        return os.getenv("OPENAI_MODEL")

def get_llamaindex_client():
    if USE_OPEN_AI_AZRUE:    
        return llama_azure_openai.AzureOpenAI(
            deployment_name=os.getenv("AZ_OPENAI_LLM"),
            api_key=os.getenv("AZ_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZ_OPENAI_API_BASE"),
            api_version=os.getenv("AZ_OPENAI_API_VERSION"))
    else:
        return llama_openai.OpenAI(model=os.getenv("OPENAI_MODEL"))

def llm_call(prompt: str, system_prompt: str = "You are an assitant", model="claude-3-5-sonnet-20241022") -> str:
    """
    Calls the model with the given prompt and returns the response.

    Args:
        prompt (str): The user prompt to send to the model.
        system_prompt (str, optional): The system prompt to send to the model. Defaults to "".
        model (str, optional): The model to use for the call. Defaults to "claude-3-5-sonnet-20241022".

    Returns:
        str: The response from the language model.
    """
    client = get_client()
    messages = [{"role": "system", "content" : system_prompt},{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=os.getenv("AZ_OPENAI_LLM"),
        max_tokens=4096,
        messages=messages,
        temperature=0.1,
    )
    return response.choices[0].message.content
    
def extract_xml(text: str, tag: str) -> str:
    """
    Extracts the content of the specified XML tag from the given text. Used for parsing structured responses 

    Args:
        text (str): The text containing the XML.
        tag (str): The XML tag to extract content from.

    Returns:
        str: The content of the specified XML tag, or an empty string if the tag is not found.
    """
    match = re.search(f'<{tag}>(.*?)</{tag}>', text, re.DOTALL)
    return match.group(1) if match else ""