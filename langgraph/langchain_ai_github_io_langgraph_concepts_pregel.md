[Skip to content](https://langchain-ai.github.io/langgraph/concepts/pregel/#langgraphs-runtime-pregel)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/pregel.md "Edit this page")

# LangGraph's Runtime (Pregel) [¶](https://langchain-ai.github.io/langgraph/concepts/pregel/\#langgraphs-runtime-pregel "Permanent link")

[Pregel](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel) implements LangGraph's runtime, managing the execution of LangGraph applications.

Compiling a [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) or creating an [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) produces a [Pregel](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel) instance that can be invoked with input.

This guide explains the runtime at a high level and provides instructions for directly implementing applications with Pregel.

> **Note:** The [Pregel](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel) runtime is named after [Google's Pregel algorithm](https://research.google/pubs/pub37252/), which describes an efficient method for large-scale parallel computation using graphs.

## Overview [¶](https://langchain-ai.github.io/langgraph/concepts/pregel/\#overview "Permanent link")

In LangGraph, Pregel combines [**actors**](https://en.wikipedia.org/wiki/Actor_model) and **channels** into a single application. **Actors** read data from channels and write data to channels. Pregel organizes the execution of the application into multiple steps, following the **Pregel Algorithm**/ **Bulk Synchronous Parallel** model.

Each step consists of three phases:

- **Plan**: Determine which **actors** to execute in this step. For example, in the first step, select the **actors** that subscribe to the special **input** channels; in subsequent steps, select the **actors** that subscribe to channels updated in the previous step.
- **Execution**: Execute all selected **actors** in parallel, until all complete, or one fails, or a timeout is reached. During this phase, channel updates are invisible to actors until the next step.
- **Update**: Update the channels with the values written by the **actors** in this step.

Repeat until no **actors** are selected for execution, or a maximum number of steps is reached.

## Actors [¶](https://langchain-ai.github.io/langgraph/concepts/pregel/\#actors "Permanent link")

An **actor** is a [PregelNode](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.PregelNode). It subscribes to channels, reads data from them, and writes data to them. It can be thought of as an **actor** in the Pregel algorithm. [PregelNodes](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.PregelNode) implement LangChain's Runnable interface.

## Channels [¶](https://langchain-ai.github.io/langgraph/concepts/pregel/\#channels "Permanent link")

Channels are used to communicate between actors (PregelNodes). Each channel has a value type, an update type, and an update function – which takes a sequence of updates and modifies the stored value. Channels can be used to send data from one chain to another, or to send data from a chain to itself in a future step. LangGraph provides a number of built-in channels:

### Basic channels: LastValue and Topic [¶](https://langchain-ai.github.io/langgraph/concepts/pregel/\#basic-channels-lastvalue-and-topic "Permanent link")

- [LastValue](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue): The default channel, stores the last value sent to the channel, useful for input and output values, or for sending data from one step to the next.
- [Topic](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic): A configurable PubSub Topic, useful for sending multiple values between **actors**, or for accumulating output. Can be configured to deduplicate values or to accumulate values over the course of multiple steps.

### Advanced channels: Context and BinaryOperatorAggregate [¶](https://langchain-ai.github.io/langgraph/concepts/pregel/\#advanced-channels-context-and-binaryoperatoraggregate "Permanent link")

- `Context`: exposes the value of a context manager, managing its lifecycle. Useful for accessing external resources that require setup and/or teardown; e.g., `client = Context(httpx.Client)`.
- [BinaryOperatorAggregate](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate): stores a persistent value, updated by applying a binary operator to the current value and each update sent to the channel, useful for computing aggregates over multiple steps; e.g., `total = BinaryOperatorAggregate(int, operator.add)`

## Examples [¶](https://langchain-ai.github.io/langgraph/concepts/pregel/\#examples "Permanent link")

While most users will interact with Pregel through the [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) API or
the [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) decorator, it is possible to interact with Pregel directly.

Below are a few different examples to give you a sense of the Pregel API.

[Single node](https://langchain-ai.github.io/langgraph/concepts/pregel/#__tabbed_1_1)[Multiple nodes](https://langchain-ai.github.io/langgraph/concepts/pregel/#__tabbed_1_2)[Topic](https://langchain-ai.github.io/langgraph/concepts/pregel/#__tabbed_1_3)[BinaryOperatorAggregate](https://langchain-ai.github.io/langgraph/concepts/pregel/#__tabbed_1_4)[Cycle](https://langchain-ai.github.io/langgraph/concepts/pregel/#__tabbed_1_5)

```md-code__content
from langgraph.channels import EphemeralValue
from langgraph.pregel import Pregel, Channel

node1 = (
    Channel.subscribe_to("a")
    | (lambda x: x + x)
    | Channel.write_to("b")
)

app = Pregel(
    nodes={"node1": node1},
    channels={
        "a": EphemeralValue(str),
        "b": EphemeralValue(str),
    },
    input_channels=["a"],
    output_channels=["b"],
)

app.invoke({"a": "foo"})

```

```md-code__content
{'b': 'foofoo'}

```

```md-code__content
from langgraph.channels import LastValue, EphemeralValue
from langgraph.pregel import Pregel, Channel

node1 = (
    Channel.subscribe_to("a")
    | (lambda x: x + x)
    | Channel.write_to("b")
)

node2 = (
    Channel.subscribe_to("b")
    | (lambda x: x + x)
    | Channel.write_to("c")
)

app = Pregel(
    nodes={"node1": node1, "node2": node2},
    channels={
        "a": EphemeralValue(str),
        "b": LastValue(str),
        "c": EphemeralValue(str),
    },
    input_channels=["a"],
    output_channels=["b", "c"],
)

app.invoke({"a": "foo"})

```

```md-code__content
{'b': 'foofoo', 'c': 'foofoofoofoo'}

```

```md-code__content
from langgraph.channels import EphemeralValue, Topic
from langgraph.pregel import Pregel, Channel

node1 = (
    Channel.subscribe_to("a")
    | (lambda x: x + x)
    | {
        "b": Channel.write_to("b"),
        "c": Channel.write_to("c")
    }
)

node2 = (
    Channel.subscribe_to("b")
    | (lambda x: x + x)
    | {
        "c": Channel.write_to("c"),
    }
)

app = Pregel(
    nodes={"node1": node1, "node2": node2},
    channels={
        "a": EphemeralValue(str),
        "b": EphemeralValue(str),
        "c": Topic(str, accumulate=True),
    },
    input_channels=["a"],
    output_channels=["c"],
)

app.invoke({"a": "foo"})

```

```md-code__content
{'c': ['foofoo', 'foofoofoofoo']}

```

This examples demonstrates how to use the BinaryOperatorAggregate channel to implement a reducer.

```md-code__content
from langgraph.channels import EphemeralValue, BinaryOperatorAggregate
from langgraph.pregel import Pregel, Channel

node1 = (
    Channel.subscribe_to("a")
    | (lambda x: x + x)
    | {
        "b": Channel.write_to("b"),
        "c": Channel.write_to("c")
    }
)

node2 = (
    Channel.subscribe_to("b")
    | (lambda x: x + x)
    | {
        "c": Channel.write_to("c"),
    }
)

def reducer(current, update):
    if current:
        return current + " | " + "update"
    else:
        return update

app = Pregel(
    nodes={"node1": node1, "node2": node2},
    channels={
        "a": EphemeralValue(str),
        "b": EphemeralValue(str),
        "c": BinaryOperatorAggregate(str, operator=reducer),
    },
    input_channels=["a"],
    output_channels=["c"],
)

app.invoke({"a": "foo"})

```

This example demonstrates how to introduce a cycle in the graph, by having
a chain write to a channel it subscribes to. Execution will continue
until a None value is written to the channel.

```md-code__content
from langgraph.channels import EphemeralValue
from langgraph.pregel import Pregel, Channel, ChannelWrite, ChannelWriteEntry

example_node = (
    Channel.subscribe_to("value")
    | (lambda x: x + x if len(x) < 10 else None)
    | ChannelWrite(writes=[ChannelWriteEntry(channel="value", skip_none=True)])
)

app = Pregel(
    nodes={"example_node": example_node},
    channels={
        "value": EphemeralValue(str),
    },
    input_channels=["value"],
    output_channels=["value"],
)

app.invoke({"value": "a"})

```

```md-code__content
{'value': 'aaaaaaaaaaaaaaaa'}

```

## High-level API [¶](https://langchain-ai.github.io/langgraph/concepts/pregel/\#high-level-api "Permanent link")

LangGraph provides two high-level APIs for creating a Pregel application: the [StateGraph (Graph API)](https://langchain-ai.github.io/langgraph/concepts/low_level/) and the [Functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api/).

[StateGraph (Graph API)](https://langchain-ai.github.io/langgraph/concepts/pregel/#__tabbed_2_1)[Functional API](https://langchain-ai.github.io/langgraph/concepts/pregel/#__tabbed_2_2)

The [StateGraph (Graph API)](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) is a higher-level abstraction that simplifies the creation of Pregel applications. It allows you to define a graph of nodes and edges. When you compile the graph, the StateGraph API automatically creates the Pregel application for you.

```md-code__content
from typing import TypedDict, Optional

from langgraph.constants import START
from langgraph.graph import StateGraph

class Essay(TypedDict):
    topic: str
    content: Optional[str]
    score: Optional[float]

def write_essay(essay: Essay):
    return {
        "content": f"Essay about {essay['topic']}",
    }

def score_essay(essay: Essay):
    return {
        "score": 10
    }

builder = StateGraph(Essay)
builder.add_node(write_essay)
builder.add_node(score_essay)
builder.add_edge(START, "write_essay")

# Compile the graph.
# This will return a Pregel instance.
graph = builder.compile()

```

The compiled Pregel instance will be associated with a list of nodes and channels. You can inspect the nodes and channels by printing them.

```md-code__content
print(graph.nodes)

```

You will see something like this:

````md-code__content
{'__start__': <langgraph.pregel.read.PregelNode at 0x7d05e3ba1810>,
 'write_essay': <langgraph.pregel.read.PregelNode at 0x7d05e3ba14d0>,
 'score_essay': <langgraph.pregel.read.PregelNode at 0x7d05e3ba1710>}
 ```

```python
print(graph.channels)

````

You should see something like this

```md-code__content
{'topic': <langgraph.channels.last_value.LastValue at 0x7d05e3294d80>,
'content': <langgraph.channels.last_value.LastValue at 0x7d05e3295040>,
'score': <langgraph.channels.last_value.LastValue at 0x7d05e3295980>,
'__start__': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e3297e00>,
'write_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e32960c0>,
'score_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e2d8ab80>,
'branch:__start__:__self__:write_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e32941c0>,
'branch:__start__:__self__:score_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e2d88800>,
'branch:write_essay:__self__:write_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e3295ec0>,
'branch:write_essay:__self__:score_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e2d8ac00>,
'branch:score_essay:__self__:write_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e2d89700>,
'branch:score_essay:__self__:score_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e2d8b400>,
'start:write_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e2d8b280>}

```

In the [Functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api/), you can use an [`entrypoint`](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) to create
a Pregel application. The `entrypoint` decorator allows you to define a function that takes input and returns output.

```md-code__content
from typing import TypedDict, Optional

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.func import entrypoint

class Essay(TypedDict):
    topic: str
    content: Optional[str]
    score: Optional[float]

checkpointer = InMemorySaver()

@entrypoint(checkpointer=checkpointer)
def write_essay(essay: Essay):
    return {
        "content": f"Essay about {essay['topic']}",
    }

print("Nodes: ")
print(write_essay.nodes)
print("Channels: ")
print(write_essay.channels)

```

```md-code__content
Nodes:
{'write_essay': <langgraph.pregel.read.PregelNode object at 0x7d05e2f9aad0>}
Channels:
{'__start__': <langgraph.channels.ephemeral_value.EphemeralValue object at 0x7d05e2c906c0>, '__end__': <langgraph.channels.last_value.LastValue object at 0x7d05e2c90c40>, '__previous__': <langgraph.channels.last_value.LastValue object at 0x7d05e1007280>}

```

## Comments

giscus

#### 0 reactions

#### 0 comments

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fconcepts%2Fpregel%2F)