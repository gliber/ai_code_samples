import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.llms.azure_openai import AzureOpenAI
from utils import get_llamaindex_client

# Download a sample pdf into the following folder!
# In this demo we are using the "Attention is all you need" from: https://arxiv.org/pdf/1706.03762
DATA_DIRECTORY = "c:\\temp\\docs"

# initialize llm
llm = get_llamaindex_client()

documents = SimpleDirectoryReader(DATA_DIRECTORY).load_data()
print(f"Number of Documents parsed: {len(documents)}")
print(f"First document:\n{documents[0]}\n")

index = VectorStoreIndex.from_documents(documents, llm=llm, verbose=True)

# By default, data is stored in-memory. To persist to disk (under ./storage):
index.storage_context.persist()
print("RAG documents saved to disk.\n")

# To reload from disk:
# storage_context = StorageContext.from_defaults(persist_dir="./storage")
# index = load_index_from_storage(storage_context)
# print("indexing loaded from disk")

query = "How does the model encode position?"
print(f"Query: {query}")

# as simple query
query_engine = index.as_query_engine(llm = llm)
response = query_engine.query(query)
print(f"Response: {response}")

# as part of a continous chat
# chat_engine = index.as_chat_engine(llm = llm)
# response = chat_engine.chat(query)
# print(f"Response: {response}")