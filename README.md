# AI code samples

These samples are demos from the "AI agents" presentation by Gilad Liber.

## list of samples

| Sample Name       | Description |
|-------------------|-------------|
| chat_completion | New ChatCompletion OepnaI API with system message and chat history |
| retrieval | A simple RAG from local documents in a folder using LlamaIndex|
| tool_multiply | Tool calling (local implementation) using LlamaIndex |
| tool_finance | Pre-defined yahoo_finance tool calling using LlamaIndex |
| workflow_chain | Chain workflow |
| workflow_parallelization | Parallelization workflow |
| workflow_route | Routing workflow |
| workflow_evaluator_optimizer | Evaluator optimizer workflow |


## technical info for all samples

### general

Set your api key and model in the OPENAI_API_KEY/OPENAI_MODEL environment variables. You can also use OpenAI Azure subscription (see "utils.py")

### installation

It is recommended to use python virtual environment (```venv```)  

```shell
pip install -r requirements.txt
```

This will install all libraries needed for all samples.
