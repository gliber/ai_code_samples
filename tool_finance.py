# https://llamahub.ai/l/tools/llama-index-tools-yahoo-finance
# LlamaIndex supports a lot of pre-defined tools:
# https://docs.llamaindex.ai/en/stable/api_reference/tools/

from llama_index.tools.yahoo_finance import YahooFinanceToolSpec
from utils import get_llamaindex_client

yahoo_finance = YahooFinanceToolSpec()

# initialize llm
llm = get_llamaindex_client()

agent = llm.from_tools(yahoo_finance.to_tool_list())

response = agent.chat("What is the price of Intel stock?")
print(response)
response = agent.chat("What do analysts say about this company?")
print(response)