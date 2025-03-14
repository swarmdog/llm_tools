[Skip to content](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#how-to-add-human-in-the-loop-processes-to-the-prebuilt-react-agent)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/create-react-agent-hitl.ipynb "Edit this page")

# How to add human-in-the-loop processes to the prebuilt ReAct agent [¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/\#how-to-add-human-in-the-loop-processes-to-the-prebuilt-react-agent "Permanent link")

Prerequisites

This guide assumes familiarity with the following:


- [Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
- [Agent Architectures](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)
- [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)
- [Tools](https://python.langchain.com/docs/concepts/tools/)

This guide will show how to add human-in-the-loop processes to the prebuilt ReAct agent. Please see [this tutorial](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent) for how to get started with the prebuilt ReAct agent

You can add a a breakpoint before tools are called by passing `interrupt_before=["tools"]` to `create_react_agent`. Note that you need to be using a checkpointer for this to work.

## Setup [¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/\#setup "Permanent link")

First, let's install the required packages and set our API keys

```md-code__content
%%capture --no-stderr
%pip install -U langgraph langchain-openai

```

```md-code__content
import getpass
import os

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("OPENAI_API_KEY")

```

Set up [LangSmith](https://smith.langchain.com/) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com/).


## Code [¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/\#code "Permanent link")

```md-code__content
# First we initialize the model we want to use.
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0)

# For this tutorial we will use custom tool that returns pre-defined values for weather in two cities (NYC & SF)
from typing import Literal

from langchain_core.tools import tool

@tool
def get_weather(location: str):
    """Use this to get weather information from a given location."""
    if location.lower() in ["nyc", "new york"]:
        return "It might be cloudy in nyc"
    elif location.lower() in ["sf", "san francisco"]:
        return "It's always sunny in sf"
    else:
        raise AssertionError("Unknown Location")

tools = [get_weather]

# We need a checkpointer to enable human-in-the-loop patterns
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

# Define the graph

from langgraph.prebuilt import create_react_agent

graph = create_react_agent(
    model, tools=tools, interrupt_before=["tools"], checkpointer=memory
)

```

API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) \| [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) \| [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) \| [create\_react\_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

## Usage [¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/\#usage "Permanent link")

```md-code__content
def print_stream(stream):
    """A utility to pretty print the stream."""
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

```

```md-code__content
from langchain_core.messages import HumanMessage

config = {"configurable": {"thread_id": "42"}}
inputs = {"messages": [("user", "what is the weather in SF, CA?")]}

print_stream(graph.stream(inputs, config, stream_mode="values"))

```

API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html)

```md-code__content
================================[1m Human Message [0m=================================\
\
what is the weather in SF, CA?\
==================================[1m Ai Message [0m==================================\
Tool Calls:\
  get_weather (call_YjOKDkgMGgUZUpKIasYk1AdK)\
 Call ID: call_YjOKDkgMGgUZUpKIasYk1AdK\
  Args:\
    location: SF, CA\
\
```\
\
We can verify that our graph stopped at the right place:\
\
```md-code__content\
snapshot = graph.get_state(config)\
print("Next step: ", snapshot.next)\
\
```\
\
```md-code__content\
Next step:  ('tools',)\
\
```\
\
Now we can either approve or edit the tool call before proceeding to the next node. If we wanted to approve the tool call, we would simply continue streaming the graph with `None` input. If we wanted to edit the tool call we need to update the state to have the correct tool call, and then after the update has been applied we can continue.\
\
We can try resuming and we will see an error arise:\
\
```md-code__content\
print_stream(graph.stream(None, config, stream_mode="values"))\
\
```\
\
```md-code__content\
==================================[1m Ai Message [0m==================================\
Tool Calls:\
  get_weather (call_YjOKDkgMGgUZUpKIasYk1AdK)\
 Call ID: call_YjOKDkgMGgUZUpKIasYk1AdK\
  Args:\
    location: SF, CA\
=================================[1m Tool Message [0m=================================\
Name: get_weather\
\
Error: AssertionError('Unknown Location')\
 Please fix your mistakes.\
==================================[1m Ai Message [0m==================================\
Tool Calls:\
  get_weather (call_CLu9ofeBhtWF2oheBspxXkfE)\
 Call ID: call_CLu9ofeBhtWF2oheBspxXkfE\
  Args:\
    location: San Francisco, CA\
\
```\
\
This error arose because our tool argument of "San Francisco, CA" is not a location our tool recognizes.\
\
Let's show how we would edit the tool call to search for "San Francisco" instead of "San Francisco, CA" - since our tool as written treats "San Francisco, CA" as an unknown location. We will update the state and then resume streaming the graph and should see no errors arise:\
\
```md-code__content\
state = graph.get_state(config)\
\
last_message = state.values["messages"][-1]\
last_message.tool_calls[0]["args"] = {"location": "San Francisco"}\
\
graph.update_state(config, {"messages": [last_message]})\
\
```\
\
```md-code__content\
{'configurable': {'thread_id': '42',\
  'checkpoint_ns': '',\
  'checkpoint_id': '1ef801d1-5b93-6bb9-8004-a088af1f9cec'}}\
\
```\
\
```md-code__content\
print_stream(graph.stream(None, config, stream_mode="values"))\
\
```\
\
```md-code__content\
==================================[1m Ai Message [0m==================================\
Tool Calls:\
  get_weather (call_CLu9ofeBhtWF2oheBspxXkfE)\
 Call ID: call_CLu9ofeBhtWF2oheBspxXkfE\
  Args:\
    location: San Francisco\
=================================[1m Tool Message [0m=================================\
Name: get_weather\
\
It's always sunny in sf\
==================================[1m Ai Message [0m==================================\
\
The weather in San Francisco is currently sunny.\
\
```\
\
Fantastic! Our graph updated properly to query the weather in San Francisco and got the correct "It's always sunny in sf" response from the tool, and then responded to the user accordingly.\
\
## Comments\
\
giscus\
\
#### 0 reactions\
\
#### 0 comments\
\
WritePreview\
\
[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")\
\
[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fhow-tos%2Fcreate-react-agent-hitl%2F)