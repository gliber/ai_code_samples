import os
from llama_index.core.tools import FunctionTool
from llama_index.agent.openai import OpenAIAgent
from utils import get_llamaindex_client

# define sample Tool
def multiply(a: int, b: int) -> int:
    """Multiple two integers and returns the result integer"""
    return a * b

# initialize llm
llm = get_llamaindex_client()

multiply_tool = FunctionTool.from_defaults(fn=multiply)

# initialize an agent from tools
agent = OpenAIAgent.from_tools([multiply_tool], llm=llm, verbose=True)
response = agent.chat("What is 2123 * 215123? and 34 * 897")

print(response)