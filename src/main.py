import os
import yaml
from pyexpat.errors import messages
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic as Chat
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.agent_toolkits.openapi.spec import reduce_openapi_spec
from langchain_community.agent_toolkits.openapi import planner
from langchain_community.utilities import RequestsWrapper

load_dotenv()

CLAUDE_API_KEY = os.environ.get("CLAUDE_API")
WEATHER_API_KEY = os.environ.get("WEATHER_API")

raw_weatherapi_com_spec = ""
with open("weatherapi.com.yaml") as f:
    raw_weatherapi_com_spec = yaml.load(f, Loader=yaml.Loader)
weatherapi_api_spec = reduce_openapi_spec(raw_weatherapi_com_spec)

class APIKeyInParameterRequestWrapper(RequestsWrapper):
    def get(self, url, **kwargs):
        params = kwargs.get('params', {})
        params['key'] = WEATHER_API_KEY
        kwargs['params'] = params
        return super().get(url, **kwargs)

model = Chat(model="claude-3-haiku-20240307", api_key=CLAUDE_API_KEY)
weather_agent = planner.create_openapi_agent(
    weatherapi_api_spec,
    APIKeyInParameterRequestWrapper(),
    llm=model,
    allow_dangerous_requests=True
)

prompt = ChatPromptTemplate.from_messages(
[
    (
        "system",
        "You are a weather agent that have an api about the weather in a given location"
    ),
    (
        "human",
        "{input}"
    )
]
)

chain = prompt | weather_agent
result = chain.invoke({
    "input": "What is the weather in Yangon?"
})

print(result.content)
