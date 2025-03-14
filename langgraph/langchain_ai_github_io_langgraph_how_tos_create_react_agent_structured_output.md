[Skip to content](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#how-to-return-structured-output-from-the-prebuilt-react-agent)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/create-react-agent-structured-output.ipynb "Edit this page")

# How to return structured output from the prebuilt ReAct agent [¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/\#how-to-return-structured-output-from-the-prebuilt-react-agent "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

- [Agent Architectures](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)
- [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)
- [Tools](https://python.langchain.com/docs/concepts/tools/)
- [Structured Output](https://python.langchain.com/docs/concepts/structured_outputs/)

To return structured output from the prebuilt ReAct agent you can provide a `response_format` parameter with the desired output schema to [create\_react\_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent):

```md-code__content
class ResponseFormat(BaseModel):
    """Respond to the user in this format."""
    my_special_output: str

graph = create_react_agent(
    model,
    tools=tools,
    # specify the schema for the structured output using `response_format` parameter
    response_format=ResponseFormat
)

```

Prebuilt ReAct makes an additional LLM call at the end of the ReAct loop to produce a structured output response. Please see [this guide](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output) to learn about other strategies for returning structured outputs from a tool-calling agent.

## Setup [¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/\#setup "Permanent link")

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


## Code [¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/\#code "Permanent link")

```md-code__content
# First we initialize the model we want to use.
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0)

# For this tutorial we will use custom tool that returns pre-defined values for weather in two cities (NYC & SF)

from typing import Literal
from langchain_core.tools import tool

@tool
def get_weather(city: Literal["nyc", "sf"]):
    """Use this to get weather information."""
    if city == "nyc":
        return "It might be cloudy in nyc"
    elif city == "sf":
        return "It's always sunny in sf"
    else:
        raise AssertionError("Unknown city")

tools = [get_weather]

# Define the structured output schema

from pydantic import BaseModel, Field

class WeatherResponse(BaseModel):
    """Respond to the user in this format."""

    conditions: str = Field(description="Weather conditions")

# Define the graph

from langgraph.prebuilt import create_react_agent

graph = create_react_agent(
    model,
    tools=tools,
    # specify the schema for the structured output using `response_format` parameter
    response_format=WeatherResponse,
)

```

API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) \| [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) \| [create\_react\_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

## Usage [¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/\#usage "Permanent link")

Let's now test our agent:

```md-code__content
inputs = {"messages": [("user", "What's the weather in NYC?")]}
response = graph.invoke(inputs)

```

You can see that the agent output contains a `structured_response` key with the structured output conforming to the specified `WeatherResponse` schema, in addition to the message history under `messages` key.

```md-code__content
response["structured_response"]

```

```md-code__content
WeatherResponse(conditions='cloudy')

```

### Customizing prompt [¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/\#customizing-prompt "Permanent link")

You might need to further customize the second LLM call for the structured output generation and provide a system prompt. To do so, you can pass a tuple (prompt, schema):

```md-code__content
graph = create_react_agent(
    model,
    tools=tools,
    # specify both the system prompt and the schema for the structured output
    response_format=("Always return capitalized weather conditions", WeatherResponse),
)

inputs = {"messages": [("user", "What's the weather in NYC?")]}
response = graph.invoke(inputs)

```

You can verify that the structured response now contains a capitalized value:

```md-code__content
response["structured_response"]

```

```md-code__content
WeatherResponse(conditions='Cloudy')

```

## Comments

giscus

#### [0 reactions](https://github.com/langchain-ai/langgraph/discussions/3574)

#### [5 comments](https://github.com/langchain-ai/langgraph/discussions/3574)

#### ·

#### 4 replies

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@Intraraksa](https://avatars.githubusercontent.com/u/38306547?u=1f3e4a0570f9e6b57313c77c786de00d5ef4ed49&v=4)Intraraksa](https://github.com/Intraraksa) [16 days ago](https://github.com/langchain-ai/langgraph/discussions/3574#discussioncomment-12308288)

I got error

create\_react\_agent() got an unexpected keyword argument 'response\_format'

1

3 replies

[![@jma-hdz](https://avatars.githubusercontent.com/u/61924317?u=8bab7723531b9c2468d967ef62b973d1c73a3779&v=4)](https://github.com/jma-hdz)

[jma-hdz](https://github.com/jma-hdz) [16 days ago](https://github.com/langchain-ai/langgraph/discussions/3574#discussioncomment-12310870)

maybe you need to check your langgraph version (pip list, etc), for example, you could try with the 0.2.71 version

[![@sanggi-wjg](https://avatars.githubusercontent.com/u/24692394?u=0084a34d2c102d54cbd33060739afdc8d7e6a90d&v=4)](https://github.com/sanggi-wjg)

[sanggi-wjg](https://github.com/sanggi-wjg) [6 days ago](https://github.com/langchain-ai/langgraph/discussions/3574#discussioncomment-12421496)

use this path

```notranslate
from langgraph.prebuilt import create_react_agent

```

[![@hinthornw](https://avatars.githubusercontent.com/u/13333726?u=82ebf1e0eb0663ebd49ba66f67a43f51bbf11442&v=4)](https://github.com/hinthornw)

[hinthornw](https://github.com/hinthornw) [yesterday](https://github.com/langchain-ai/langgraph/discussions/3574#discussioncomment-12478504)

Contributor

Try upgrading your langgraph-prebiult package

[![@edgarlcs](https://avatars.githubusercontent.com/u/92342090?u=30a178c81ffdcb8c048351341f38922dc274a9da&v=4)edgarlcs](https://github.com/edgarlcs) [13 days ago](https://github.com/langchain-ai/langgraph/discussions/3574#discussioncomment-12357490)

For some reason the agent responds well in the message responses but returns something completely different on the structured output every time. Has anyone encountered this issue?

1

0 replies

[![@limcolin](https://avatars.githubusercontent.com/u/13306549?u=ef0a912b6a8041d727e71bdc47bd092cc56b4cf4&v=4)limcolin](https://github.com/limcolin) [8 days ago](https://github.com/langchain-ai/langgraph/discussions/3574#discussioncomment-12401088)

Is there a JS version to achieve this using 2 LLMs?

Binding output as tool is giving me invalid\_tool\_calls when streaming with streamEvents

1

0 replies

[![@kapis](https://avatars.githubusercontent.com/u/11299397?u=49f7fa9dbb83a4f353049c3a99f997e64f3f6641&v=4)kapis](https://github.com/kapis) [4 days ago](https://github.com/langchain-ai/langgraph/discussions/3574#discussioncomment-12438915)

You guys aware you can have both tools and structured output with OpenAI models? No need to make is a tool.

1

1 reply

[![@hinthornw](https://avatars.githubusercontent.com/u/13333726?u=82ebf1e0eb0663ebd49ba66f67a43f51bbf11442&v=4)](https://github.com/hinthornw)

[hinthornw](https://github.com/hinthornw) [yesterday](https://github.com/langchain-ai/langgraph/discussions/3574#discussioncomment-12478529)

Contributor

Yes. That is why `response_format` uses structured output instead of tools.

[![@sree24lakshmi](https://avatars.githubusercontent.com/u/77089066?v=4)sree24lakshmi](https://github.com/sree24lakshmi) [yesterday](https://github.com/langchain-ai/langgraph/discussions/3574#discussioncomment-12478314)

Can anyone please suggest if there is a way to overcome context window length when working with SQLDatabasetoolkit. The agent runs into error with stop reason=length as the context length exceeding in case of large output returned by database. Appreciate your help thank you

1

0 replies

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fhow-tos%2Fcreate-react-agent-structured-output%2F)