[Skip to content](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#rebuild-graph-at-runtime)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/deployment/graph_rebuild.md "Edit this page")

# Rebuild Graph at Runtime [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/\#rebuild-graph-at-runtime "Permanent link")

You might need to rebuild your graph with a different configuration for a new run. For example, you might need to use a different graph state or graph structure depending on the config. This guide shows how you can do this.

Note

In most cases, customizing behavior based on the config should be handled by a single graph where each node can read a config and change its behavior based on it

## Prerequisites [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/\#prerequisites "Permanent link")

Make sure to check out [this how-to guide](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/) on setting up your app for deployment first.

## Define graphs [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/\#define-graphs "Permanent link")

Let's say you have an app with a simple graph that calls an LLM and returns the response to the user. The app file directory looks like the following:

```md-code__content
my-app/
|-- requirements.txt
|-- .env
|-- openai_agent.py     # code for your graph

```

where the graph is defined in `openai_agent.py`.

### No rebuild [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/\#no-rebuild "Permanent link")

In the standard LangGraph API configuration, the server uses the compiled graph instance that's defined at the top level of `openai_agent.py`, which looks like the following:

```md-code__content
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, MessageGraph

model = ChatOpenAI(temperature=0)

graph_workflow = MessageGraph()

graph_workflow.add_node("agent", model)
graph_workflow.add_edge("agent", END)
graph_workflow.add_edge(START, "agent")

agent = graph_workflow.compile()

```

API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) \| [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) \| [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

To make the server aware of your graph, you need to specify a path to the variable that contains the `CompiledStateGraph` instance in your LangGraph API configuration ( `langgraph.json`), e.g.:

```md-code__content
{
    "dependencies": ["."],
    "graphs": {
        "openai_agent": "./openai_agent.py:agent",
    },
    "env": "./.env"
}

```

### Rebuild [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/\#rebuild "Permanent link")

To make your graph rebuild on each new run with custom configuration, you need to rewrite `openai_agent.py` to instead provide a _function_ that takes a config and returns a graph (or compiled graph) instance. Let's say we want to return our existing graph for user ID '1', and a tool-calling agent for other users. We can modify `openai_agent.py` as follows:

```md-code__content
from typing import Annotated
from typing_extensions import TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, MessageGraph
from langgraph.graph.state import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
from langchain_core.runnables import RunnableConfig

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

model = ChatOpenAI(temperature=0)

def make_default_graph():
    """Make a simple LLM agent"""
    graph_workflow = StateGraph(State)
    def call_model(state):
        return {"messages": [model.invoke(state["messages"])]}

    graph_workflow.add_node("agent", call_model)
    graph_workflow.add_edge("agent", END)
    graph_workflow.add_edge(START, "agent")

    agent = graph_workflow.compile()
    return agent

def make_alternative_graph():
    """Make a tool-calling agent"""

    @tool
    def add(a: float, b: float):
        """Adds two numbers."""
        return a + b

    tool_node = ToolNode([add])
    model_with_tools = model.bind_tools([add])
    def call_model(state):
        return {"messages": [model_with_tools.invoke(state["messages"])]}

    def should_continue(state: State):
        if state["messages"][-1].tool_calls:
            return "tools"
        else:
            return END

    graph_workflow = StateGraph(State)

    graph_workflow.add_node("agent", call_model)
    graph_workflow.add_node("tools", tool_node)
    graph_workflow.add_edge("tools", "agent")
    graph_workflow.add_edge(START, "agent")
    graph_workflow.add_conditional_edges("agent", should_continue)

    agent = graph_workflow.compile()
    return agent

# this is the graph making function that will decide which graph to
# build based on the provided config
def make_graph(config: RunnableConfig):
    user_id = config.get("configurable", {}).get("user_id")
    # route to different graph state / structure based on the user ID
    if user_id == "1":
        return make_default_graph()
    else:
        return make_alternative_graph()

```

API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) \| [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) \| [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) \| [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) \| [add\_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages) \| [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode) \| [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) \| [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) \| [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html)

Finally, you need to specify the path to your graph-making function ( `make_graph`) in `langgraph.json`:

```md-code__content
{
    "dependencies": ["."],
    "graphs": {
        "openai_agent": "./openai_agent.py:make_graph",
    },
    "env": "./.env"
}

```

See more info on LangGraph API configuration file [here](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file)

## Comments

giscus

#### [0 reactions](https://github.com/langchain-ai/langgraph/discussions/3331)

#### [1 comment](https://github.com/langchain-ai/langgraph/discussions/3331)

#### ·

#### 1 reply

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@jasontjahjono](https://avatars.githubusercontent.com/u/67953053?u=1b5e8c13d09f56e7193f7a238731656420edc39a&v=4)jasontjahjono](https://github.com/jasontjahjono) [Feb 6](https://github.com/langchain-ai/langgraph/discussions/3331#discussioncomment-12078432)

do we have a javascript version of this?

1

1 reply

[![@jasontjahjono](https://avatars.githubusercontent.com/u/67953053?u=1b5e8c13d09f56e7193f7a238731656420edc39a&v=4)](https://github.com/jasontjahjono)

[jasontjahjono](https://github.com/jasontjahjono) [Feb 6](https://github.com/langchain-ai/langgraph/discussions/3331#discussioncomment-12078565)

what is the type for `def make_graph(config: RunnableConfig):` in typescript?

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fdeployment%2Fgraph_rebuild%2F)