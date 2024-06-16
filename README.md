# Langchain Action Model Experiment

> An experiment on executing External Weather API using Claude Haiku LLM

## How does it work?

1. Program connects to Claude using API Key
2. Program queries claude about the weather in Yangon
3. Using OpenAPI Specification, Claude determines the best and most suitable API to call
4. Calls the API and parse the result into a meaningful response.

## Get things running

```python
pip3 install -r requirements.txt
python3 src/main.py
```