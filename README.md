# Langchain Action Model Experiment

> An experiment on executing External Weather API using Claude Haiku LLM and Python Langchain

## How does it work?

1. Program connects to Claude using API Key
2. Program queries claude about the weather in Yangon
<img width="881" alt="image" src="https://github.com/DreamerChaserHAH/langchain-action-model-experiment/assets/109950820/aacd1759-f78b-4ec8-a0a7-fcf2636584fe"/>

3. Using OpenAPI Specification, Claude determines the best and most suitable API to call
4. Calls the API and parse the result into a meaningful response.
<img width="942" alt="image" src="https://github.com/DreamerChaserHAH/langchain-action-model-experiment/assets/109950820/d04e145a-331f-4ddf-b856-1cf18ff87fc9"/>

## Get things running

```python
pip3 install -r requirements.txt
```

create a clone of .env.sample and rename it to .env, and then add the relevant api keys

```python
python src/main.py
```
