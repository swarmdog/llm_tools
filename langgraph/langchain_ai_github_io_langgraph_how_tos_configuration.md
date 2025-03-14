[Skip to content](https://langchain-ai.github.io/langgraph/how-tos/configuration/#how-to-add-runtime-configuration-to-your-graph)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/configuration.ipynb "Edit this page")

# How to add runtime configuration to your graph [¶](https://langchain-ai.github.io/langgraph/how-tos/configuration/\#how-to-add-runtime-configuration-to-your-graph "Permanent link")

Sometimes you want to be able to configure your agent when calling it.
Examples of this include configuring which LLM to use.
Below we walk through an example of doing so.

Prerequisites

This guide assumes familiarity with the following:


- [LangGraph State](https://langchain-ai.github.io/langgraph/concepts/low_level/#state)
- [Chat Models](https://python.langchain.com/docs/concepts/#chat-models/)

## Setup [¶](https://langchain-ai.github.io/langgraph/how-tos/configuration/\#setup "Permanent link")

First, let's install the required packages and set our API keys

```md-code__content
%%capture --no-stderr
%pip install -U langgraph langchain_anthropic

```

```md-code__content
import getpass
import os

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("ANTHROPIC_API_KEY")

```

Set up [LangSmith](https://smith.langchain.com/) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com/).


## Define graph [¶](https://langchain-ai.github.io/langgraph/how-tos/configuration/\#define-graph "Permanent link")

First, let's create a very simple graph

```md-code__content
import operator
from typing import Annotated, Sequence
from typing_extensions import TypedDict

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import BaseMessage, HumanMessage

from langgraph.graph import END, StateGraph, START

model = ChatAnthropic(model_name="claude-2.1")

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

def _call_model(state):
    state["messages"]
    response = model.invoke(state["messages"])
    return {"messages": [response]}

# Define a new graph
builder = StateGraph(AgentState)
builder.add_node("model", _call_model)
builder.add_edge(START, "model")
builder.add_edge("model", END)

graph = builder.compile()

```

API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) \| [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) \| [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) \| [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) \| [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) \| [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

## Configure the graph [¶](https://langchain-ai.github.io/langgraph/how-tos/configuration/\#configure-the-graph "Permanent link")

Great! Now let's suppose that we want to extend this example so the user is able to choose from multiple llms.
We can easily do that by passing in a config. Any configuration information needs to be passed inside `configurable` key as shown below.
This config is meant to contain things are not part of the input (and therefore that we don't want to track as part of the state).

```md-code__content
from langchain_openai import ChatOpenAI
from typing import Optional
from langchain_core.runnables.config import RunnableConfig

openai_model = ChatOpenAI()

models = {
    "anthropic": model,
    "openai": openai_model,
}

def _call_model(state: AgentState, config: RunnableConfig):
    # Access the config through the configurable key
    model_name = config["configurable"].get("model", "anthropic")
    model = models[model_name]
    response = model.invoke(state["messages"])
    return {"messages": [response]}

# Define a new graph
builder = StateGraph(AgentState)
builder.add_node("model", _call_model)
builder.add_edge(START, "model")
builder.add_edge("model", END)

graph = builder.compile()

```

API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) \| [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html)

If we call it with no configuration, it will use the default as we defined it (Anthropic).

```md-code__content
graph.invoke({"messages": [HumanMessage(content="hi")]})

```

```md-code__content
{'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}),\
  AIMessage(content='Hello!', additional_kwargs={}, response_metadata={'id': 'msg_01WFXkfgK8AvSckLvYYrHshi', 'model': 'claude-2.1', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 10, 'output_tokens': 6}}, id='run-ece54b16-f8fc-4201-8405-b97122edf8d8-0', usage_metadata={'input_tokens': 10, 'output_tokens': 6, 'total_tokens': 16})]}

```

We can also call it with a config to get it to use a different model.

```md-code__content
config = {"configurable": {"model": "openai"}}
graph.invoke({"messages": [HumanMessage(content="hi")]}, config=config)

```

```md-code__content
{'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}),\
  AIMessage(content='Hello! How can I assist you today?', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 8, 'total_tokens': 17, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-f8331964-d811-4b44-afb8-56c30ade7c15-0', usage_metadata={'input_tokens': 8, 'output_tokens': 9, 'total_tokens': 17})]}

```

We can also adapt our graph to take in more configuration! Like a system message for example.

```md-code__content
from langchain_core.messages import SystemMessage

# We can define a config schema to specify the configuration options for the graph
# A config schema is useful for indicating which fields are available in the configurable dict inside the config
class ConfigSchema(TypedDict):
    model: Optional[str]
    system_message: Optional[str]

def _call_model(state: AgentState, config: RunnableConfig):
    # Access the config through the configurable key
    model_name = config["configurable"].get("model", "anthropic")
    model = models[model_name]
    messages = state["messages"]
    if "system_message" in config["configurable"]:
        messages = [\
            SystemMessage(content=config["configurable"]["system_message"])\
        ] + messages
    response = model.invoke(messages)
    return {"messages": [response]}

# Define a new graph - note that we pass in the configuration schema here, but it is not necessary
workflow = StateGraph(AgentState, ConfigSchema)
workflow.add_node("model", _call_model)
workflow.add_edge(START, "model")
workflow.add_edge("model", END)

graph = workflow.compile()

```

API Reference: [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html)

```md-code__content
graph.invoke({"messages": [HumanMessage(content="hi")]})

```

```md-code__content
{'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}),\
  AIMessage(content='Hello!', additional_kwargs={}, response_metadata={'id': 'msg_01VgCANVHr14PsHJSXyKkLVh', 'model': 'claude-2.1', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 10, 'output_tokens': 6}}, id='run-f8c5f18c-be58-4e44-9a4e-d43692d7eed1-0', usage_metadata={'input_tokens': 10, 'output_tokens': 6, 'total_tokens': 16})]}

```

```md-code__content
config = {"configurable": {"system_message": "respond in italian"}}
graph.invoke({"messages": [HumanMessage(content="hi")]}, config=config)

```

```md-code__content
{'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}),\
  AIMessage(content='Ciao!', additional_kwargs={}, response_metadata={'id': 'msg_011YuCYQk1Rzc8PEhVCpQGr6', 'model': 'claude-2.1', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 14, 'output_tokens': 7}}, id='run-a583341e-5868-4e8c-a536-881338f21252-0', usage_metadata={'input_tokens': 14, 'output_tokens': 7, 'total_tokens': 21})]}

```

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Please help us improve this page by adding to the discussion below.


## Comments

[iframe](https://giscus.app/en/widget?origin=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fhow-tos%2Fconfiguration%2F&session=&theme=preferred_color_scheme&reactionsEnabled=1&emitMetadata=0&inputPosition=bottom&repo=langchain-ai%2Flanggraph&repoId=R_kgDOKFU0lQ&category=Discussions&categoryId=DIC_kwDOKFU0lc4CfZgA&strict=0&description=Build+language+agents+as+graphs&backLink=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fhow-tos%2Fconfiguration%2F&term=langgraph%2Fhow-tos%2Fconfiguration%2F)

Back to top