[Skip to content](https://langchain-ai.github.io/langgraph/concepts/low_level/#langgraph-glossary)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/low_level.md "Edit this page")

# LangGraph Glossary [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#langgraph-glossary "Permanent link")

## Graphs [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#graphs "Permanent link")

At its core, LangGraph models agent workflows as graphs. You define the behavior of your agents using three key components:

1. [`State`](https://langchain-ai.github.io/langgraph/concepts/low_level/#state): A shared data structure that represents the current snapshot of your application. It can be any Python type, but is typically a `TypedDict` or Pydantic `BaseModel`.

2. [`Nodes`](https://langchain-ai.github.io/langgraph/concepts/low_level/#nodes): Python functions that encode the logic of your agents. They receive the current `State` as input, perform some computation or side-effect, and return an updated `State`.

3. [`Edges`](https://langchain-ai.github.io/langgraph/concepts/low_level/#edges): Python functions that determine which `Node` to execute next based on the current `State`. They can be conditional branches or fixed transitions.


By composing `Nodes` and `Edges`, you can create complex, looping workflows that evolve the `State` over time. The real power, though, comes from how LangGraph manages that `State`. To emphasize: `Nodes` and `Edges` are nothing more than Python functions - they can contain an LLM or just good ol' Python code.

In short: _nodes do the work. edges tell what to do next_.

LangGraph's underlying graph algorithm uses [message passing](https://en.wikipedia.org/wiki/Message_passing) to define a general program. When a Node completes its operation, it sends messages along one or more edges to other node(s). These recipient nodes then execute their functions, pass the resulting messages to the next set of nodes, and the process continues. Inspired by Google's [Pregel](https://research.google/pubs/pregel-a-system-for-large-scale-graph-processing/) system, the program proceeds in discrete "super-steps."

A super-step can be considered a single iteration over the graph nodes. Nodes that run in parallel are part of the same super-step, while nodes that run sequentially belong to separate super-steps. At the start of graph execution, all nodes begin in an `inactive` state. A node becomes `active` when it receives a new message (state) on any of its incoming edges (or "channels"). The active node then runs its function and responds with updates. At the end of each super-step, nodes with no incoming messages vote to `halt` by marking themselves as `inactive`. The graph execution terminates when all nodes are `inactive` and no messages are in transit.

### StateGraph [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#stategraph "Permanent link")

The `StateGraph` class is the main graph class to use. This is parameterized by a user defined `State` object.

### Compiling your graph [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#compiling-your-graph "Permanent link")

To build your graph, you first define the [state](https://langchain-ai.github.io/langgraph/concepts/low_level/#state), you then add [nodes](https://langchain-ai.github.io/langgraph/concepts/low_level/#nodes) and [edges](https://langchain-ai.github.io/langgraph/concepts/low_level/#edges), and then you compile it. What exactly is compiling your graph and why is it needed?

Compiling is a pretty simple step. It provides a few basic checks on the structure of your graph (no orphaned nodes, etc). It is also where you can specify runtime args like [checkpointers](https://langchain-ai.github.io/langgraph/concepts/persistence/) and [breakpoints](https://langchain-ai.github.io/langgraph/concepts/low_level/#breakpoints). You compile your graph by just calling the `.compile` method:

```md-code__content
graph = graph_builder.compile(...)

```

You **MUST** compile your graph before you can use it.

## State [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#state "Permanent link")

The first thing you do when you define a graph is define the `State` of the graph. The `State` consists of the [schema of the graph](https://langchain-ai.github.io/langgraph/concepts/low_level/#schema) as well as [`reducer` functions](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers) which specify how to apply updates to the state. The schema of the `State` will be the input schema to all `Nodes` and `Edges` in the graph, and can be either a `TypedDict` or a `Pydantic` model. All `Nodes` will emit updates to the `State` which are then applied using the specified `reducer` function.

### Schema [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#schema "Permanent link")

The main documented way to specify the schema of a graph is by using `TypedDict`. However, we also support [using a Pydantic BaseModel](https://langchain-ai.github.io/langgraph/how-tos/state-model/) as your graph state to add **default values** and additional data validation.

By default, the graph will have the same input and output schemas. If you want to change this, you can also specify explicit input and output schemas directly. This is useful when you have a lot of keys, and some are explicitly for input and others for output. See the [notebook here](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/) for how to use.

#### Multiple schemas [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#multiple-schemas "Permanent link")

Typically, all graph nodes communicate with a single schema. This means that they will read and write to the same state channels. But, there are cases where we want more control over this:

- Internal nodes can pass information that is not required in the graph's input / output.
- We may also want to use different input / output schemas for the graph. The output might, for example, only contain a single relevant output key.

It is possible to have nodes write to private state channels inside the graph for internal node communication. We can simply define a private schema, `PrivateState`. See [this notebook](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/) for more detail.

It is also possible to define explicit input and output schemas for a graph. In these cases, we define an "internal" schema that contains _all_ keys relevant to graph operations. But, we also define `input` and `output` schemas that are sub-sets of the "internal" schema to constrain the input and output of the graph. See [this notebook](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/) for more detail.

Let's look at an example:

```md-code__content
class InputState(TypedDict):
    user_input: str

class OutputState(TypedDict):
    graph_output: str

class OverallState(TypedDict):
    foo: str
    user_input: str
    graph_output: str

class PrivateState(TypedDict):
    bar: str

def node_1(state: InputState) -> OverallState:
    # Write to OverallState
    return {"foo": state["user_input"] + " name"}

def node_2(state: OverallState) -> PrivateState:
    # Read from OverallState, write to PrivateState
    return {"bar": state["foo"] + " is"}

def node_3(state: PrivateState) -> OutputState:
    # Read from PrivateState, write to OutputState
    return {"graph_output": state["bar"] + " Lance"}

builder = StateGraph(OverallState,input=InputState,output=OutputState)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)
builder.add_edge(START, "node_1")
builder.add_edge("node_1", "node_2")
builder.add_edge("node_2", "node_3")
builder.add_edge("node_3", END)

graph = builder.compile()
graph.invoke({"user_input":"My"})
{'graph_output': 'My name is Lance'}

```

There are two subtle and important points to note here:

1. We pass `state: InputState` as the input schema to `node_1`. But, we write out to `foo`, a channel in `OverallState`. How can we write out to a state channel that is not included in the input schema? This is because a node _can write to any state channel in the graph state._ The graph state is the union of of the state channels defined at initialization, which includes `OverallState` and the filters `InputState` and `OutputState`.

2. We initialize the graph with `StateGraph(OverallState,input=InputState,output=OutputState)`. So, how can we write to `PrivateState` in `node_2`? How does the graph gain access to this schema if it was not passed in the `StateGraph` initialization? We can do this because _nodes can also declare additional state channels_ as long as the state schema definition exists. In this case, the `PrivateState` schema is defined, so we can add `bar` as a new state channel in the graph and write to it.


### Reducers [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#reducers "Permanent link")

Reducers are key to understanding how updates from nodes are applied to the `State`. Each key in the `State` has its own independent reducer function. If no reducer function is explicitly specified then it is assumed that all updates to that key should override it. There are a few different types of reducers, starting with the default type of reducer:

#### Default Reducer [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#default-reducer "Permanent link")

These two examples show how to use the default reducer:

**Example A:**

```md-code__content
from typing_extensions import TypedDict

class State(TypedDict):
    foo: int
    bar: list[str]

```

In this example, no reducer functions are specified for any key. Let's assume the input to the graph is `{"foo": 1, "bar": ["hi"]}`. Let's then assume the first `Node` returns `{"foo": 2}`. This is treated as an update to the state. Notice that the `Node` does not need to return the whole `State` schema - just an update. After applying this update, the `State` would then be `{"foo": 2, "bar": ["hi"]}`. If the second node returns `{"bar": ["bye"]}` then the `State` would then be `{"foo": 2, "bar": ["bye"]}`

**Example B:**

```md-code__content
from typing import Annotated
from typing_extensions import TypedDict
from operator import add

class State(TypedDict):
    foo: int
    bar: Annotated[list[str], add]

```

In this example, we've used the `Annotated` type to specify a reducer function ( `operator.add`) for the second key ( `bar`). Note that the first key remains unchanged. Let's assume the input to the graph is `{"foo": 1, "bar": ["hi"]}`. Let's then assume the first `Node` returns `{"foo": 2}`. This is treated as an update to the state. Notice that the `Node` does not need to return the whole `State` schema - just an update. After applying this update, the `State` would then be `{"foo": 2, "bar": ["hi"]}`. If the second node returns `{"bar": ["bye"]}` then the `State` would then be `{"foo": 2, "bar": ["hi", "bye"]}`. Notice here that the `bar` key is updated by adding the two lists together.

### Working with Messages in Graph State [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#working-with-messages-in-graph-state "Permanent link")

#### Why use messages? [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#why-use-messages "Permanent link")

Most modern LLM providers have a chat model interface that accepts a list of messages as input. LangChain's [`ChatModel`](https://python.langchain.com/docs/concepts/#chat-models) in particular accepts a list of `Message` objects as inputs. These messages come in a variety of forms such as `HumanMessage` (user input) or `AIMessage` (LLM response). To read more about what message objects are, please refer to [this](https://python.langchain.com/docs/concepts/#messages) conceptual guide.

#### Using Messages in your Graph [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#using-messages-in-your-graph "Permanent link")

In many cases, it is helpful to store prior conversation history as a list of messages in your graph state. To do so, we can add a key (channel) to the graph state that stores a list of `Message` objects and annotate it with a reducer function (see `messages` key in the example below). The reducer function is vital to telling the graph how to update the list of `Message` objects in the state with each state update (for example, when a node sends an update). If you don't specify a reducer, every state update will overwrite the list of messages with the most recently provided value. If you wanted to simply append messages to the existing list, you could use `operator.add` as a reducer.

However, you might also want to manually update messages in your graph state (e.g. human-in-the-loop). If you were to use `operator.add`, the manual state updates you send to the graph would be appended to the existing list of messages, instead of updating existing messages. To avoid that, you need a reducer that can keep track of message IDs and overwrite existing messages, if updated. To achieve this, you can use the prebuilt `add_messages` function. For brand new messages, it will simply append to existing list, but it will also handle the updates for existing messages correctly.

#### Serialization [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#serialization "Permanent link")

In addition to keeping track of message IDs, the `add_messages` function will also try to deserialize messages into LangChain `Message` objects whenever a state update is received on the `messages` channel. See more information on LangChain serialization/deserialization [here](https://python.langchain.com/docs/how_to/serialization/). This allows sending graph inputs / state updates in the following format:

```md-code__content
# this is supported
{"messages": [HumanMessage(content="message")]}

# and this is also supported
{"messages": [{"type": "human", "content": "message"}]}

```

Since the state updates are always deserialized into LangChain `Messages` when using `add_messages`, you should use dot notation to access message attributes, like `state["messages"][-1].content`. Below is an example of a graph that uses `add_messages` as it's reducer function.

```md-code__content
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import TypedDict

class GraphState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]

```

API Reference: [AnyMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.AnyMessage.html) \| [add\_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages)

#### MessagesState [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#messagesstate "Permanent link")

Since having a list of messages in your state is so common, there exists a prebuilt state called `MessagesState` which makes it easy to use messages. `MessagesState` is defined with a single `messages` key which is a list of `AnyMessage` objects and uses the `add_messages` reducer. Typically, there is more state to track than just messages, so we see people subclass this state and add more fields, like:

```md-code__content
from langgraph.graph import MessagesState

class State(MessagesState):
    documents: list[str]

```

## Nodes [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#nodes "Permanent link")

In LangGraph, nodes are typically python functions (sync or async) where the **first** positional argument is the [state](https://langchain-ai.github.io/langgraph/concepts/low_level/#state), and (optionally), the **second** positional argument is a "config", containing optional [configurable parameters](https://langchain-ai.github.io/langgraph/concepts/low_level/#configuration) (such as a `thread_id`).

Similar to `NetworkX`, you add these nodes to a graph using the [add\_node](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph.add_node) method:

```md-code__content
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph

builder = StateGraph(dict)

def my_node(state: dict, config: RunnableConfig):
    print("In node: ", config["configurable"]["user_id"])
    return {"results": f"Hello, {state['input']}!"}

# The second argument is optional
def my_other_node(state: dict):
    return state

builder.add_node("my_node", my_node)
builder.add_node("other_node", my_other_node)
...

```

API Reference: [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html) \| [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

Behind the scenes, functions are converted to [RunnableLambda](https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.base.RunnableLambda.html#langchain_core.runnables.base.RunnableLambda) s, which add batch and async support to your function, along with native tracing and debugging.

If you add a node to a graph without specifying a name, it will be given a default name equivalent to the function name.

```md-code__content
builder.add_node(my_node)
# You can then create edges to/from this node by referencing it as `"my_node"`

```

### `START` Node [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#start-node "Permanent link")

The `START` Node is a special node that represents the node that sends user input to the graph. The main purpose for referencing this node is to determine which nodes should be called first.

```md-code__content
from langgraph.graph import START

graph.add_edge(START, "node_a")

```

API Reference: [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

### `END` Node [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#end-node "Permanent link")

The `END` Node is a special node that represents a terminal node. This node is referenced when you want to denote which edges have no actions after they are done.

```md-code__content
from langgraph.graph import END

graph.add_edge("node_a", END)

```

## Edges [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#edges "Permanent link")

Edges define how the logic is routed and how the graph decides to stop. This is a big part of how your agents work and how different nodes communicate with each other. There are a few key types of edges:

- Normal Edges: Go directly from one node to the next.
- Conditional Edges: Call a function to determine which node(s) to go to next.
- Entry Point: Which node to call first when user input arrives.
- Conditional Entry Point: Call a function to determine which node(s) to call first when user input arrives.

A node can have MULTIPLE outgoing edges. If a node has multiple out-going edges, **all** of those destination nodes will be executed in parallel as a part of the next superstep.

### Normal Edges [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#normal-edges "Permanent link")

If you **always** want to go from node A to node B, you can use the [add\_edge](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph.add_edge) method directly.

```md-code__content
graph.add_edge("node_a", "node_b")

```

### Conditional Edges [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#conditional-edges "Permanent link")

If you want to **optionally** route to 1 or more edges (or optionally terminate), you can use the [add\_conditional\_edges](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph.add_conditional_edges) method. This method accepts the name of a node and a "routing function" to call after that node is executed:

```md-code__content
graph.add_conditional_edges("node_a", routing_function)

```

Similar to nodes, the `routing_function` accepts the current `state` of the graph and returns a value.

By default, the return value `routing_function` is used as the name of the node (or list of nodes) to send the state to next. All those nodes will be run in parallel as a part of the next superstep.

You can optionally provide a dictionary that maps the `routing_function`'s output to the name of the next node.

```md-code__content
graph.add_conditional_edges("node_a", routing_function, {True: "node_b", False: "node_c"})

```

Tip

Use [`Command`](https://langchain-ai.github.io/langgraph/concepts/low_level/#command) instead of conditional edges if you want to combine state updates and routing in a single function.

### Entry Point [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#entry-point "Permanent link")

The entry point is the first node(s) that are run when the graph starts. You can use the [`add_edge`](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph.add_edge) method from the virtual [`START`](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) node to the first node to execute to specify where to enter the graph.

```md-code__content
from langgraph.graph import START

graph.add_edge(START, "node_a")

```

API Reference: [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

### Conditional Entry Point [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#conditional-entry-point "Permanent link")

A conditional entry point lets you start at different nodes depending on custom logic. You can use [`add_conditional_edges`](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph.add_conditional_edges) from the virtual [`START`](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) node to accomplish this.

```md-code__content
from langgraph.graph import START

graph.add_conditional_edges(START, routing_function)

```

API Reference: [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

You can optionally provide a dictionary that maps the `routing_function`'s output to the name of the next node.

```md-code__content
graph.add_conditional_edges(START, routing_function, {True: "node_b", False: "node_c"})

```

## `Send` [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#send "Permanent link")

By default, `Nodes` and `Edges` are defined ahead of time and operate on the same shared state. However, there can be cases where the exact edges are not known ahead of time and/or you may want different versions of `State` to exist at the same time. A common example of this is with [map-reduce](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/) design patterns. In this design pattern, a first node may generate a list of objects, and you may want to apply some other node to all those objects. The number of objects may be unknown ahead of time (meaning the number of edges may not be known) and the input `State` to the downstream `Node` should be different (one for each generated object).

To support this design pattern, LangGraph supports returning [`Send`](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Send) objects from conditional edges. `Send` takes two arguments: first is the name of the node, and second is the state to pass to that node.

```md-code__content
def continue_to_jokes(state: OverallState):
    return [Send("generate_joke", {"subject": s}) for s in state['subjects']]

graph.add_conditional_edges("node_a", continue_to_jokes)

```

## `Command` [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#command "Permanent link")

It can be useful to combine control flow (edges) and state updates (nodes). For example, you might want to BOTH perform state updates AND decide which node to go to next in the SAME node. LangGraph provides a way to do so by returning a [`Command`](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) object from node functions:

```md-code__content
def my_node(state: State) -> Command[Literal["my_other_node"]]:
    return Command(
        # state update
        update={"foo": "bar"},
        # control flow
        goto="my_other_node"
    )

```

With `Command` you can also achieve dynamic control flow behavior (identical to [conditional edges](https://langchain-ai.github.io/langgraph/concepts/low_level/#conditional-edges)):

```md-code__content
def my_node(state: State) -> Command[Literal["my_other_node"]]:
    if state["foo"] == "bar":
        return Command(update={"foo": "baz"}, goto="my_other_node")

```

Important

When returning `Command` in your node functions, you must add return type annotations with the list of node names the node is routing to, e.g. `Command[Literal["my_other_node"]]`. This is necessary for the graph rendering and tells LangGraph that `my_node` can navigate to `my_other_node`.

Check out this [how-to guide](https://langchain-ai.github.io/langgraph/how-tos/command/) for an end-to-end example of how to use `Command`.

### When should I use Command instead of conditional edges? [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#when-should-i-use-command-instead-of-conditional-edges "Permanent link")

Use `Command` when you need to **both** update the graph state **and** route to a different node. For example, when implementing [multi-agent handoffs](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#handoffs) where it's important to route to a different agent and pass some information to that agent.

Use [conditional edges](https://langchain-ai.github.io/langgraph/concepts/low_level/#conditional-edges) to route between nodes conditionally without updating the state.

### Navigating to a node in a parent graph [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#navigating-to-a-node-in-a-parent-graph "Permanent link")

If you are using [subgraphs](https://langchain-ai.github.io/langgraph/concepts/low_level/#subgraphs), you might want to navigate from a node within a subgraph to a different subgraph (i.e. a different node in the parent graph). To do so, you can specify `graph=Command.PARENT` in `Command`:

```md-code__content
def my_node(state: State) -> Command[Literal["my_other_node"]]:
    return Command(
        update={"foo": "bar"},
        goto="other_subgraph",  # where `other_subgraph` is a node in the parent graph
        graph=Command.PARENT
    )

```

Note

Setting `graph` to `Command.PARENT` will navigate to the closest parent graph.

State updates with `Command.PARENT`

When you send updates from a subgraph node to a parent graph node for a key that's shared by both parent and subgraph [state schemas](https://langchain-ai.github.io/langgraph/concepts/low_level/#schema), you **must** define a [reducer](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers) for the key you're updating in the parent graph state. See this [example](https://langchain-ai.github.io/langgraph/how-tos/command/#navigating-to-a-node-in-a-parent-graph).

This is particularly useful when implementing [multi-agent handoffs](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#handoffs).

### Using inside tools [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#using-inside-tools "Permanent link")

A common use case is updating graph state from inside a tool. For example, in a customer support application you might want to look up customer information based on their account number or ID in the beginning of the conversation. To update the graph state from the tool, you can return `Command(update={"my_custom_key": "foo", "messages": [...]})` from the tool:

```md-code__content
@tool
def lookup_user_info(tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig):
    """Use this to look up user information to better assist them with their questions."""
    user_info = get_user_info(config.get("configurable", {}).get("user_id"))
    return Command(
        update={
            # update the state keys
            "user_info": user_info,
            # update the message history
            "messages": [ToolMessage("Successfully looked up user information", tool_call_id=tool_call_id)]
        }
    )

```

Important

You MUST include `messages` (or any state key used for the message history) in `Command.update` when returning `Command` from a tool and the list of messages in `messages` MUST contain a `ToolMessage`. This is necessary for the resulting message history to be valid (LLM providers require AI messages with tool calls to be followed by the tool result messages).

If you are using tools that update state via `Command`, we recommend using prebuilt [`ToolNode`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode) which automatically handles tools returning `Command` objects and propagates them to the graph state. If you're writing a custom node that calls tools, you would need to manually propagate `Command` objects returned by the tools as the update from the node.

### Human-in-the-loop [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#human-in-the-loop "Permanent link")

`Command` is an important part of human-in-the-loop workflows: when using `interrupt()` to collect user input, `Command` is then used to supply the input and resume execution via `Command(resume="User input")`. Check out [this conceptual guide](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) for more information.

## Persistence [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#persistence "Permanent link")

LangGraph provides built-in persistence for your agent's state using [checkpointers](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver). Checkpointers save snapshots of the graph state at every superstep, allowing resumption at any time. This enables features like human-in-the-loop interactions, memory management, and fault-tolerance. You can even directly manipulate a graph's state after its execution using the
appropriate `get` and `update` methods. For more details, see the [persistence conceptual guide](https://langchain-ai.github.io/langgraph/concepts/persistence/).

## Threads [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#threads "Permanent link")

Threads in LangGraph represent individual sessions or conversations between your graph and a user. When using checkpointing, turns in a single conversation (and even steps within a single graph execution) are organized by a unique thread ID.

## Storage [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#storage "Permanent link")

LangGraph provides built-in document storage through the [BaseStore](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) interface. Unlike checkpointers, which save state by thread ID, stores use custom namespaces for organizing data. This enables cross-thread persistence, allowing agents to maintain long-term memories, learn from past interactions, and accumulate knowledge over time. Common use cases include storing user profiles, building knowledge bases, and managing global preferences across all threads.

## Graph Migrations [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#graph-migrations "Permanent link")

LangGraph can easily handle migrations of graph definitions (nodes, edges, and state) even when using a checkpointer to track state.

- For threads at the end of the graph (i.e. not interrupted) you can change the entire topology of the graph (i.e. all nodes and edges, remove, add, rename, etc)
- For threads currently interrupted, we support all topology changes other than renaming / removing nodes (as that thread could now be about to enter a node that no longer exists) -- if this is a blocker please reach out and we can prioritize a solution.
- For modifying state, we have full backwards and forwards compatibility for adding and removing keys
- State keys that are renamed lose their saved state in existing threads
- State keys whose types change in incompatible ways could currently cause issues in threads with state from before the change -- if this is a blocker please reach out and we can prioritize a solution.

## Configuration [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#configuration "Permanent link")

When creating a graph, you can also mark that certain parts of the graph are configurable. This is commonly done to enable easily switching between models or system prompts. This allows you to create a single "cognitive architecture" (the graph) but have multiple different instance of it.

You can optionally specify a `config_schema` when creating a graph.

```md-code__content
class ConfigSchema(TypedDict):
    llm: str

graph = StateGraph(State, config_schema=ConfigSchema)

```

You can then pass this configuration into the graph using the `configurable` config field.

```md-code__content
config = {"configurable": {"llm": "anthropic"}}

graph.invoke(inputs, config=config)

```

You can then access and use this configuration inside a node:

```md-code__content
def node_a(state, config):
    llm_type = config.get("configurable", {}).get("llm", "openai")
    llm = get_llm(llm_type)
    ...

```

See [this guide](https://langchain-ai.github.io/langgraph/how-tos/configuration/) for a full breakdown on configuration.

### Recursion Limit [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#recursion-limit "Permanent link")

The recursion limit sets the maximum number of [super-steps](https://langchain-ai.github.io/langgraph/concepts/low_level/#graphs) the graph can execute during a single execution. Once the limit is reached, LangGraph will raise `GraphRecursionError`. By default this value is set to 25 steps. The recursion limit can be set on any graph at runtime, and is passed to `.invoke`/ `.stream` via the config dictionary. Importantly, `recursion_limit` is a standalone `config` key and should not be passed inside the `configurable` key as all other user-defined configuration. See the example below:

```md-code__content
graph.invoke(inputs, config={"recursion_limit": 5, "configurable":{"llm": "anthropic"}})

```

Read [this how-to](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/) to learn more about how the recursion limit works.

## `interrupt` [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#interrupt "Permanent link")

Use the [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) function to **pause** the graph at specific points to collect user input. The `interrupt` function surfaces interrupt information to the client, allowing the developer to collect user input, validate the graph state, or make decisions before resuming execution.

```md-code__content
from langgraph.types import interrupt

def human_approval_node(state: State):
    ...
    answer = interrupt(
        # This value will be sent to the client.
        # It can be any JSON serializable value.
        {"question": "is it ok to continue?"},
    )
    ...

```

API Reference: [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

Resuming the graph is done by passing a [`Command`](https://langchain-ai.github.io/langgraph/concepts/low_level/#command) object to the graph with the `resume` key set to the value returned by the `interrupt` function.

Read more about how the `interrupt` is used for **human-in-the-loop** workflows in the [Human-in-the-loop conceptual guide](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/).

## Breakpoints [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#breakpoints "Permanent link")

Breakpoints pause graph execution at specific points and enable stepping through execution step by step. Breakpoints are powered by LangGraph's [**persistence layer**](https://langchain-ai.github.io/langgraph/concepts/persistence/), which saves the state after each graph step. Breakpoints can also be used to enable [**human-in-the-loop**](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) workflows, though we recommend using the [`interrupt` function](https://langchain-ai.github.io/langgraph/concepts/low_level/#interrupt) for this purpose.

Read more about breakpoints in the [Breakpoints conceptual guide](https://langchain-ai.github.io/langgraph/concepts/breakpoints/).

## Subgraphs [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#subgraphs "Permanent link")

A subgraph is a [graph](https://langchain-ai.github.io/langgraph/concepts/low_level/#graphs) that is used as a [node](https://langchain-ai.github.io/langgraph/concepts/low_level/#nodes) in another graph. This is nothing more than the age-old concept of encapsulation, applied to LangGraph. Some reasons for using subgraphs are:

- building [multi-agent systems](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)

- when you want to reuse a set of nodes in multiple graphs, which maybe share some state, you can define them once in a subgraph and then use them in multiple parent graphs

- when you want different teams to work on different parts of the graph independently, you can define each part as a subgraph, and as long as the subgraph interface (the input and output schemas) is respected, the parent graph can be built without knowing any details of the subgraph


There are two ways to add subgraphs to a parent graph:

- add a node with the compiled subgraph: this is useful when the parent graph and the subgraph share state keys and you don't need to transform state on the way in or out

```md-code__content
builder.add_node("subgraph", subgraph_builder.compile())

```

- add a node with a function that invokes the subgraph: this is useful when the parent graph and the subgraph have different state schemas and you need to transform state before or after calling the subgraph

```md-code__content
subgraph = subgraph_builder.compile()

def call_subgraph(state: State):
    return subgraph.invoke({"subgraph_key": state["parent_key"]})

builder.add_node("subgraph", call_subgraph)

```

Let's take a look at examples for each.

### As a compiled graph [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#as-a-compiled-graph "Permanent link")

The simplest way to create subgraph nodes is by using a [compiled subgraph](https://langchain-ai.github.io/langgraph/concepts/low_level/#compiling-your-graph) directly. When doing so, it is **important** that the parent graph and the subgraph [state schemas](https://langchain-ai.github.io/langgraph/concepts/low_level/#state) share at least one key which they can use to communicate. If your graph and subgraph do not share any keys, you should write a function [invoking the subgraph](https://langchain-ai.github.io/langgraph/concepts/low_level/#as-a-function) instead.

Note

If you pass extra keys to the subgraph node (i.e., in addition to the shared keys), they will be ignored by the subgraph node. Similarly, if you return extra keys from the subgraph, they will be ignored by the parent graph.

```md-code__content
from langgraph.graph import StateGraph
from typing import TypedDict

class State(TypedDict):
    foo: str

class SubgraphState(TypedDict):
    foo: str  # note that this key is shared with the parent graph state
    bar: str

# Define subgraph
def subgraph_node(state: SubgraphState):
    # note that this subgraph node can communicate with the parent graph via the shared "foo" key
    return {"foo": state["foo"] + "bar"}

subgraph_builder = StateGraph(SubgraphState)
subgraph_builder.add_node(subgraph_node)
...
subgraph = subgraph_builder.compile()

# Define parent graph
builder = StateGraph(State)
builder.add_node("subgraph", subgraph)
...
graph = builder.compile()

```

API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

### As a function [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#as-a-function "Permanent link")

You might want to define a subgraph with a completely different schema. In this case, you can create a node function that invokes the subgraph. This function will need to [transform](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/) the input (parent) state to the subgraph state before invoking the subgraph, and transform the results back to the parent state before returning the state update from the node.

```md-code__content
class State(TypedDict):
    foo: str

class SubgraphState(TypedDict):
    # note that none of these keys are shared with the parent graph state
    bar: str
    baz: str

# Define subgraph
def subgraph_node(state: SubgraphState):
    return {"bar": state["bar"] + "baz"}

subgraph_builder = StateGraph(SubgraphState)
subgraph_builder.add_node(subgraph_node)
...
subgraph = subgraph_builder.compile()

# Define parent graph
def node(state: State):
    # transform the state to the subgraph state
    response = subgraph.invoke({"bar": state["foo"]})
    # transform response back to the parent state
    return {"foo": response["bar"]}

builder = StateGraph(State)
# note that we are using `node` function instead of a compiled subgraph
builder.add_node(node)
...
graph = builder.compile()

```

## Visualization [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#visualization "Permanent link")

It's often nice to be able to visualize graphs, especially as they get more complex. LangGraph comes with several built-in ways to visualize graphs. See [this how-to guide](https://langchain-ai.github.io/langgraph/how-tos/visualization/) for more info.

## Streaming [¶](https://langchain-ai.github.io/langgraph/concepts/low_level/\#streaming "Permanent link")

LangGraph is built with first class support for streaming, including streaming updates from graph nodes during the execution, streaming tokens from LLM calls and more. See this [conceptual guide](https://langchain-ai.github.io/langgraph/concepts/streaming/) for more information.

## Comments

giscus

#### [29 reactions](https://github.com/langchain-ai/langgraph/discussions/778)

👍11🎉4❤️8🚀6

#### [14 comments](https://github.com/langchain-ai/langgraph/discussions/778)

#### ·

#### 10 replies

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@pradeepjung45](https://avatars.githubusercontent.com/u/90687887?u=ac87a192b883c6c1b518d283295ce386334b9d58&v=4)pradeepjung45](https://github.com/pradeepjung45) [Jun 24, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-9856584)

provide more code tutorials about the real world use case scenerios.

1

👍1

1 reply

[![@hwchase17](https://avatars.githubusercontent.com/u/11986836?u=f4c4f21a82b2af6c9f91e1f1d99ea40062f7a101&v=4)](https://github.com/hwchase17)

[hwchase17](https://github.com/hwchase17) [Jun 24, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-9861776)

Contributor

those will be in the tutorials and how-to sections, we'll add links

👍3❤️1

[![@siddicky](https://avatars.githubusercontent.com/u/44811336?u=6b42d79a6dc9b974e00748c2dbf885cd67d4e4c6&v=4)siddicky](https://github.com/siddicky) [Jun 25, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-9876044)

Super excited to see `Send` capability! As always, Langchain Team is miles ahead of the competition.

1

0 replies

[![@ArturNiklewicz](https://avatars.githubusercontent.com/u/107845868?u=b84886d4a4e171b0ab447c7dbadd066493a1c670&v=4)ArturNiklewicz](https://github.com/ArturNiklewicz) [Jun 26, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-9884855)

Hi Harrison,

I just wanted to sincerely thank you for all the work you have done and shared with all of us. What you are doing is absolutely great and I wish you all the best :)

My biased & subjective junior feedback:

For most people, this should be the starting point of trying to understand how any of the code actually works.

I have just finished the LangGraph miniseries from deeplearning.ai platform, however, I had not known the abstract LangGraph concepts. The vidoes are too long for not trying to understand what is going on under the hood and too short for catching up, when so many new concepts are introduced. It is actually an intuitive practice of professionals and experienced people to explain elaborated concepts with ease in a relatively fast pace format, due to the psychological phenomena of "Curse of expertise", or "WYSIATI" (Kahneman, D. (2011). Thinking, fast and slow. Farrar, Straus and Giroux.)

I think that the most streamlined way of inviting people to experiment with LangGraph would be:

1. Showcase what can be achieved with LangGraph in a short video - a reel
2. This documentation page paired with a folder of: Jupyter notebookes of real-life popular scenarios such as the \[Essay Writer, Research Assistants, etc.\]

1

👍1

1 reply

[![@serafinski](https://avatars.githubusercontent.com/u/88508650?u=e643ec8c99ac0f941ad1762bc5db7e44823362c5&v=4)](https://github.com/serafinski)

[serafinski](https://github.com/serafinski) [Aug 7, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-10269183)

Agree!

[![@vaibhavp4](https://avatars.githubusercontent.com/u/4822281?v=4)vaibhavp4](https://github.com/vaibhavp4) [Jun 26, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-9887779)

Couldn't find the documentation on exactly how the state is updated by the nodes.

1

1 reply

[![@ArturNiklewicz](https://avatars.githubusercontent.com/u/107845868?u=b84886d4a4e171b0ab447c7dbadd066493a1c670&v=4)](https://github.com/ArturNiklewicz)

[ArturNiklewicz](https://github.com/ArturNiklewicz) [Jun 27, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-9891461)

The agent follows along the path of the compiled graph, as defined with the nodes and edges. The edges decide the direction of the next step, whereas the nodes decide the triggered logic. Each node function contains the state (TypedDict or Pydantic BaseModel) as a parameter and each node function return (a) key-value pair(s) of the state (TypedDict or Pydantic BaseModel)

👍1

[![@gabayben](https://avatars.githubusercontent.com/u/9704848?v=4)gabayben](https://github.com/gabayben) [Jul 8, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-9983743)

Please please document the low level components, Pregel, PregelNode, ChannelRead, ChannelWrite, and most importantly, channels. This is relevant for those wishing to implement their own Graph/CompiledGraph out out Pregel.

1

4 replies

[![@gabayben](https://avatars.githubusercontent.com/u/9704848?v=4)](https://github.com/gabayben)

[gabayben](https://github.com/gabayben) [Jul 8, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-9983751)

out of Pregel\*

[![@hinthornw](https://avatars.githubusercontent.com/u/13333726?u=82ebf1e0eb0663ebd49ba66f67a43f51bbf11442&v=4)](https://github.com/hinthornw)

[hinthornw](https://github.com/hinthornw) [Sep 10, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-10603684)

Contributor

Pregel isn't really a public interface and we exclude them from the docs on purpose

[![@gabayben](https://avatars.githubusercontent.com/u/9704848?v=4)](https://github.com/gabayben)

[gabayben](https://github.com/gabayben) [Sep 17, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-10673207)

edited

Yeah I know but Pregel, despite being low level, is the beauty of Langgraph. StateGraph is nothing but a builder, Pregel only knows about nodes and channels. Someone can even implement a graph that resembles Haystack's Pipeline, with field-level relationships, with a compile method that returns an instance of Pregel. Which is why it should be documented.

[![@gabayben](https://avatars.githubusercontent.com/u/9704848?v=4)](https://github.com/gabayben)

[gabayben](https://github.com/gabayben) [Sep 17, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-10673212)

I'm just saying, you're selling this framework short. It's worth a lot more than just the StateGraph builder.

[![@JianXiao2021](https://avatars.githubusercontent.com/u/88485732?v=4)JianXiao2021](https://github.com/JianXiao2021) [Jul 19, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-10093558)

Hello! I would like to ask if there is a way to directly manipulate the state without invoking the reducer? I have a list like the `bar` in the example of the "Update state" section. I need to append element to it in a single run of the graph, but I also need to completely clear this list after the run is completed.

1

0 replies

[![@donatoaz](https://avatars.githubusercontent.com/u/127527?v=4)donatoaz](https://github.com/donatoaz) [Jul 25, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-10143506)

What is the recommended way to check if the execution was interrupted due to an "interrupt\_before"? Currently I just get as a result the state as it is mid-execution of the graph. Should I have control variables in the state indicating that I hit a breakpoint?

2

1 reply

[![@donatoaz](https://avatars.githubusercontent.com/u/127527?v=4)](https://github.com/donatoaz)

[donatoaz](https://github.com/donatoaz) [Aug 6, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-10255031)

edited

I found in an example:

```notranslate
snapshot = app.get_state(thread)

if snapshot.next:
  # There was an interruption, do work ...

```

[![@Fasttyper](https://avatars.githubusercontent.com/u/37948718?u=db5fb9cc5d421012e6f3b9fd8a952f27640792c7&v=4)Fasttyper](https://github.com/Fasttyper) [Aug 6, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-10253364)

I was struggling to understand the low level concepts for a while. Great doc, this was exactly what I needed. Keep up the good work!

1

👍1

0 replies

[![@davlu93](https://avatars.githubusercontent.com/u/54266602?v=4)davlu93](https://github.com/davlu93) [Aug 9, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-10285764)

Hello,

thanks for the amazin work. I would like though to see some practical implementation for production cases where the persistence is store in a database stored in the cloud, example google big query or similar.

1

0 replies

[![@Me-Baran](https://avatars.githubusercontent.com/u/149557825?u=1bf29b5fc7ae715b7f3ae4bfcdf07322d9462a0b&v=4)Me-Baran](https://github.com/Me-Baran) [Sep 10, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-10601566)

Hello,

Thank you for providing this comprehensive documentation. I'm reading through the section about checkpointers and threads, and I've come across a sentence that I'm finding a bit unclear. The sentence is:

"You can use checkpointers to create threads and save the state ..."

I'm not sure I fully understand the relationship between checkpointers and threads as described here. Could you please clarify this?

Thank you for your time and for helping me understand this concept better.

1

0 replies

[![@pdhoolia](https://avatars.githubusercontent.com/u/820408?v=4)pdhoolia](https://github.com/pdhoolia) [Sep 11, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-10612180)

I was exploring `guard-rails`. [Guardrails example](https://github.com/langchain-ai/langgraph-guardrails-example) is a great resource. The supported pattern however requires an explicit (imperative) placement of guard node in the graph. While this is sufficient for a lot of cases, I wanted to check if a more declarative placement is possible as well.

My guardrails case is that of a PII (Personally Identifiable Information). So I create a `pii_guard` node which wants to mask PIIs (in user\_message, or tool\_call results) before any of the edges target an LLM nodes. I was looking for an `interrupt` like declaration. Something like:

```notranslate
workflow.compile(
    checkpointer=memory,
    apply_before=(["agent1", "agent2"], pii_guard),
    apply_after=(["agent1", "agent2"], pii_unguard),
)

```

Such an aspect-oriented binding, makes it much simpler to ensure that no matter how I land up on my LLM node, the desired masking would happen, and post LLM the desired un-masking would happen. Explicit specification in the imperative flow is a bit of a pain.

1

1 reply

[![@pdhoolia](https://avatars.githubusercontent.com/u/820408?v=4)](https://github.com/pdhoolia)

[pdhoolia](https://github.com/pdhoolia) [Sep 18, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-10679635)

Ignore previous comment. The declarative `apply_before` and `apply_after` should already be do-able using decorators. E.g. in the python version I should already be able to do something like:

```
import functools

def pre(state, config):
    # Pre-processing logic
    print("Running pre-processing...")
    state['pre_processed'] = True
    return state, config

def post(state, config):
    # Post-processing logic
    print("Running post-processing...")
    state['post_processed'] = True
    return state, config

# Define a decorator that wraps pre and post logic around any function
def pre_post_decorator(func):
    @functools.wraps(func)
    def wrapper(state, config):
        # Run pre-processing logic
        state, config = pre(state, config)

        # Execute the original function
        result = func(state, config)

        # Run post-processing logic
        state, config = post(state, config)

        return result
    return wrapper

# Example agent functions
@pre_post_decorator
def call_agent_1(state, config):
    print(f"Executing agent 1: {state}")
    # Agent computation here
    return state

@pre_post_decorator
def call_agent_2(state, config):
    print(f"Executing agent 2: {state}")
    # Agent computation here
    return state

# Let's see this in action
state = {'pre_processed': False, 'post_processed': False}
config = {}

# These function calls will automatically run the pre and post logic
call_agent_1(state, config)
print(f"{state}")
state = {'pre_processed': False, 'post_processed': False}
call_agent_2(state, config)
print(f"{state}")
```

And in the javascript version, I should be able to do:

```
// Define the pre-processing function
function pre(state, config) {
    console.log("Running pre-processing...");
    state.preProcessed = true;
    return [state, config];
  }

  // Define the post-processing function
  function post(state, config) {
    console.log("Running post-processing...");
    state.postProcessed = true;
    return [state, config];
  }

  // Create a higher-order function (decorator) to wrap around the agent functions
  function prePostWrapper(func) {
    return function (state, config) {
      // Run pre-processing
      [state, config] = pre(state, config);

      // Execute the original function
      const result = func(state, config);

      // Run post-processing
      [state, config] = post(state, config);

      return result;
    };
  }

  // Example agent functions
  function callAgent1(state, config) {
    console.log("Executing agent 1: " + JSON.stringify(state));
    // Agent computation here
    return state;
  }

  function callAgent2(state, config) {
    console.log("Executing agent 2: " + JSON.stringify(state));
    // Agent computation here
    return state;
  }

  // Wrap the agent functions with prePostWrapper
  const wrappedAgentModel1 = prePostWrapper(callAgent1);
  const wrappedAgentModel2 = prePostWrapper(callAgent2);


  // Let's see this in action
  let state = { preProcessed: false, postProcessed: false };
  let config = {};

  // Use wrapped function. They will automatically run the pre and post logic
  wrappedAgentModel1(state, config);
  state = { preProcessed: false, postProcessed: false };
  wrappedAgentModel2(state, config);
```

[![@Eknathabhiram](https://avatars.githubusercontent.com/u/150422670?v=4)Eknathabhiram](https://github.com/Eknathabhiram) [Sep 21, 2024](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-10711359)

I want to know whether we make routing function return to different nodes for the same key .

1

0 replies

[![@djprawns](https://avatars.githubusercontent.com/u/3663330?u=35367c8a7be62f945e489c43d25e5481f1f616f7&v=4)djprawns](https://github.com/djprawns) [Jan 10](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-11796807)

lets say i want to have a certain method to be called after every node invocation, how can i achieve that? also how can i specify that for certain nodes, lets say START and END?

1

0 replies

[![@vabbybansal](https://avatars.githubusercontent.com/u/10529264?v=4)vabbybansal](https://github.com/vabbybansal) [Jan 31](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-12013964)

Is there any way to create dependency graph functionality as well? Currently, graph nodes do not wait for all dependencies to resolve before executing a node by design. If we can also achieve some dependency graph kind of use-cases by adding some graph param then, that would be great!

1

1 reply

[![@vabbybansal](https://avatars.githubusercontent.com/u/10529264?v=4)](https://github.com/vabbybansal)

[vabbybansal](https://github.com/vabbybansal) [Jan 31](https://github.com/langchain-ai/langgraph/discussions/778#discussioncomment-12014059)

Looks like this can be achieved by creating a multi-node edge, something like this -

graph.add\_edge(\["node1", "node2"\], "node3")

This way, node3 waits for both node1 and node2 to finish and we can achieve task dependency properly.

Can we please add this to the main langgraph documentation? I found this on a github comment - [#954](https://github.com/langchain-ai/langgraph/issues/954)

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fconcepts%2Flow_level%2F)