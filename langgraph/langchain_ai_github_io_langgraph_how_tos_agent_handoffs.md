[Skip to content](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#how-to-implement-handoffs-between-agents)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/agent-handoffs.ipynb "Edit this page")

# How to implement handoffs between agents [¶](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/\#how-to-implement-handoffs-between-agents "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

- [Multi-agent systems](https://langchain-ai.github.io/langgraph/concepts/multi_agent)
- [Command](https://langchain-ai.github.io/langgraph/concepts/low_level/#command)
- [LangGraph Glossary](https://langchain-ai.github.io/langgraph/concepts/low_level/)

In multi-agent architectures, agents can be represented as graph nodes. Each agent node executes its step(s) and decides whether to finish execution or route to another agent, including potentially routing to itself (e.g., running in a loop). A natural pattern in multi-agent interactions is [handoffs](https://langchain-ai.github.io/langgraph/concepts/multi_agent#handoffs), where one agent hands off control to another. Handoffs allow you to specify:

- **destination**: target agent to navigate to - node name in LangGraph
- **payload**: information to pass to that agent - state update in LangGraph

To implement handoffs in LangGraph, agent nodes can return `Command` object that allows you to [combine both control flow and state updates](https://langchain-ai.github.io/langgraph/how-tos/command):

```md-code__content
def agent(state) -> Command[Literal["agent", "another_agent"]]:
    # the condition for routing/halting can be anything, e.g. LLM tool call / structured output, etc.
    goto = get_next_agent(...)  # 'agent' / 'another_agent'
    return Command(
        # Specify which agent to call next
        goto=goto,
        # Update the graph state
        update={"my_state_key": "my_state_value"}
    )

```

One of the most common agent types is a tool-calling agent. For those types of agents, one pattern is wrapping a handoff in a tool call, e.g.:

```md-code__content
@tool
def transfer_to_bob(state):
    """Transfer to bob."""
    return Command(
        goto="bob",
        update={"my_state_key": "my_state_value"},
        # Each tool-calling agent is implemented as a subgraph.
        # As a result, to navigate to another agent (a sibling sub-graph),
        # we need to specify that navigation is w/ respect to the parent graph.
        graph=Command.PARENT,
    )

```

This guide shows how you can:

- implement handoffs using `Command`: agent node makes a decision on who to hand off to (usually LLM-based), and explicitly returns a handoff via `Command`. These are useful when you need fine-grained control over how an agent routes to another agent. It could be well suited for implementing a supervisor agent in a supervisor architecture.
- implement handoffs using tools: a tool-calling agent has access to tools that can return a handoff via `Command`. The tool-executing node in the agent recognizes `Command` objects returned by the tools and routes accordingly. Handoff tool a general-purpose primitive that is useful in any multi-agent systems that contain tool-calling agents.

## Setup [¶](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/\#setup "Permanent link")

```md-code__content
%%capture --no-stderr
%pip install -U langgraph langchain-anthropic

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


## Implement handoffs using `Command` [¶](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/\#implement-handoffs-using-command "Permanent link")

Let's implement a system with two agents:

- an addition expert (can only add numbers)
- a multiplication expert (can only multiply numbers).

In this example the agents will be relying on the LLM for doing math. In a more realistic [follow-up example](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#using-with-a-custom-agent), we will give the agents tools for doing math.

When the addition expert needs help with multiplication, it hands off to the multiplication expert and vice-versa. This is an example of a simple multi-agent network.

Each agent will have a corresponding node function that can conditionally return a `Command` object (e.g. our handoff). The node function will use an LLM with a system prompt and a tool that lets it signal when it needs to hand off to another agent. If the LLM responds with the tool calls, we will return a `Command(goto=<other_agent>)`.

> **Note**: while we're using tools for the LLM to signal that it needs a handoff, the condition for the handoff can be anything: a specific response text from the LLM, structured output from the LLM, any other custom logic, etc.

```md-code__content
from typing_extensions import Literal
from langchain_core.messages import ToolMessage
from langchain_core.tools import tool
from langchain_anthropic import ChatAnthropic
from langgraph.graph import MessagesState, StateGraph, START
from langgraph.types import Command

model = ChatAnthropic(model="claude-3-5-sonnet-latest")

@tool
def transfer_to_multiplication_expert():
    """Ask multiplication agent for help."""
    # This tool is not returning anything: we're just using it
    # as a way for LLM to signal that it needs to hand off to another agent
    # (See the paragraph above)
    return

@tool
def transfer_to_addition_expert():
    """Ask addition agent for help."""
    return

def addition_expert(
    state: MessagesState,
) -> Command[Literal["multiplication_expert", "__end__"]]:
    system_prompt = (
        "You are an addition expert, you can ask the multiplication expert for help with multiplication. "
        "Always do your portion of calculation before the handoff."
    )
    messages = [{"role": "system", "content": system_prompt}] + state["messages"]
    ai_msg = model.bind_tools([transfer_to_multiplication_expert]).invoke(messages)
    # If there are tool calls, the LLM needs to hand off to another agent
    if len(ai_msg.tool_calls) > 0:
        tool_call_id = ai_msg.tool_calls[-1]["id"]
        # NOTE: it's important to insert a tool message here because LLM providers are expecting
        # all AI messages to be followed by a corresponding tool result message
        tool_msg = {
            "role": "tool",
            "content": "Successfully transferred",
            "tool_call_id": tool_call_id,
        }
        return Command(
            goto="multiplication_expert", update={"messages": [ai_msg, tool_msg]}
        )

    # If the expert has an answer, return it directly to the user
    return {"messages": [ai_msg]}

def multiplication_expert(
    state: MessagesState,
) -> Command[Literal["addition_expert", "__end__"]]:
    system_prompt = (
        "You are a multiplication expert, you can ask an addition expert for help with addition. "
        "Always do your portion of calculation before the handoff."
    )
    messages = [{"role": "system", "content": system_prompt}] + state["messages"]
    ai_msg = model.bind_tools([transfer_to_addition_expert]).invoke(messages)
    if len(ai_msg.tool_calls) > 0:
        tool_call_id = ai_msg.tool_calls[-1]["id"]
        tool_msg = {
            "role": "tool",
            "content": "Successfully transferred",
            "tool_call_id": tool_call_id,
        }
        return Command(goto="addition_expert", update={"messages": [ai_msg, tool_msg]})

    return {"messages": [ai_msg]}

```

API Reference: [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html) \| [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) \| [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) \| [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) \| [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) \| [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

Let's now combine both of these nodes into a single graph. Note that there are no edges between the agents! If the expert has an answer, it will return it directly to the user, otherwise it will route to the other expert for help.

```md-code__content
builder = StateGraph(MessagesState)
builder.add_node("addition_expert", addition_expert)
builder.add_node("multiplication_expert", multiplication_expert)
# we'll always start with the addition expert
builder.add_edge(START, "addition_expert")
graph = builder.compile()

```

Finally, let's define a helper function to render the streamed outputs nicely:

```md-code__content
from langchain_core.messages import convert_to_messages

def pretty_print_messages(update):
    if isinstance(update, tuple):
        ns, update = update
        # skip parent graph updates in the printouts
        if len(ns) == 0:
            return

        graph_id = ns[-1].split(":")[0]
        print(f"Update from subgraph {graph_id}:")
        print("\n")

    for node_name, node_update in update.items():
        print(f"Update from node {node_name}:")
        print("\n")

        for m in convert_to_messages(node_update["messages"]):
            m.pretty_print()
        print("\n")

```

API Reference: [convert\_to\_messages](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.convert_to_messages.html)

Let's run the graph with an expression that requires both addition and multiplication:

```md-code__content
for chunk in graph.stream(
    {"messages": [("user", "what's (3 + 5) * 12")]},
):
    pretty_print_messages(chunk)

```

```md-code__content
Update from node addition_expert:

==================================[1m Ai Message [0m==================================\
\
[{'text': "Let me help break this down:\n\nFirst, I'll handle the addition part since I'm the addition expert:\n3 + 5 = 8\n\nNow, for the multiplication of 8 * 12, I'll need to ask the multiplication expert for help.", 'type': 'text'}, {'id': 'toolu_015LCrsomHbeoQPtCzuff78Y', 'input': {}, 'name': 'transfer_to_multiplication_expert', 'type': 'tool_use'}]\
Tool Calls:\
  transfer_to_multiplication_expert (toolu_015LCrsomHbeoQPtCzuff78Y)\
 Call ID: toolu_015LCrsomHbeoQPtCzuff78Y\
  Args:\
=================================[1m Tool Message [0m=================================\
\
Successfully transferred\
\
Update from node multiplication_expert:\
\
==================================[1m Ai Message [0m==================================\
\
[{'text': 'I see there was an error in my approach. I am actually the multiplication expert, and I need to ask the addition expert for help with (3 + 5) first.', 'type': 'text'}, {'id': 'toolu_01HFcB8WesPfDyrdgxoXApZk', 'input': {}, 'name': 'transfer_to_addition_expert', 'type': 'tool_use'}]\
Tool Calls:\
  transfer_to_addition_expert (toolu_01HFcB8WesPfDyrdgxoXApZk)\
 Call ID: toolu_01HFcB8WesPfDyrdgxoXApZk\
  Args:\
=================================[1m Tool Message [0m=================================\
\
Successfully transferred\
\
Update from node addition_expert:\
\
==================================[1m Ai Message [0m==================================\
\
Now that I have the result of 3 + 5 = 8 from the addition expert, I can multiply 8 * 12:\
\
8 * 12 = 96\
\
So, (3 + 5) * 12 = 96\
\
```\
\
You can see that the addition expert first handled the expression in the parentheses, and then handed off to the multiplication expert to finish the calculation.\
\
Now let's see how we can implement this same system using special handoff tools and give our agents actual math tools.\
\
## Implement handoffs using tools [¶](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/\#implement-handoffs-using-tools "Permanent link")\
\
### Implement a handoff tool [¶](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/\#implement-a-handoff-tool "Permanent link")\
\
In the previous example we explicitly defined custom handoffs in each of the agent nodes. Another pattern is to create special **handoff tools** that directly return `Command` objects. When an agent calls a tool like this, it hands the control off to a different agent. Specifically, the tool-executing node in the agent recognizes the `Command` objects returned by the tools and routes control flow accordingly. **Note**: unlike the previous example, a tool-calling agent is not a single node but another graph that can be added to the multi-agent graph as a subgraph node.\
\
There are a few important considerations when implementing handoff tools:\
\
- since each agent is a **subgraph** node in another graph, and the tools will be called in one of the agent subgraph nodes (e.g. tool executor), we need to specify `graph=Command.PARENT` in the `Command`, so that LangGraph knows to navigate outside of the agent subgraph\
- we can optionally specify a state update that will be applied to the parent graph state before the next agent is called\
  - these state updates can be used to control [how much of the chat message history](https://langchain-ai.github.io/langgraph/concepts/multi_agent#shared-message-list) the target agent sees. For example, you might choose to just share the last AI messages from the current agent, or its full internal chat history, etc. In the examples below we'll be sharing the full internal chat history.\
- we can optionally provide the following to the tool (in the tool function signature):\
\
\
  - graph state (using [`InjectedState`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedState))\
  - graph long-term memory (using [`InjectedStore`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedStore))\
  - the current tool call ID (using [`InjectedToolCallId`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.InjectedToolCallId.html))\
\
These are not necessary but are useful for creating the state update passed to the next agent.\
\
```md-code__content\
from typing import Annotated\
\
from langchain_core.tools import tool\
from langchain_core.tools.base import InjectedToolCallId\
from langgraph.prebuilt import InjectedState\
\
def make_handoff_tool(*, agent_name: str):\
    """Create a tool that can return handoff via a Command"""\
    tool_name = f"transfer_to_{agent_name}"\
\
    @tool(tool_name)\
    def handoff_to_agent(\
        # # optionally pass current graph state to the tool (will be ignored by the LLM)\
        state: Annotated[dict, InjectedState],\
        # optionally pass the current tool call ID (will be ignored by the LLM)\
        tool_call_id: Annotated[str, InjectedToolCallId],\
    ):\
        """Ask another agent for help."""\
        tool_message = {\
            "role": "tool",\
            "content": f"Successfully transferred to {agent_name}",\
            "name": tool_name,\
            "tool_call_id": tool_call_id,\
        }\
        return Command(\
            # navigate to another agent node in the PARENT graph\
            goto=agent_name,\
            graph=Command.PARENT,\
            # This is the state update that the agent `agent_name` will see when it is invoked.\
            # We're passing agent's FULL internal message history AND adding a tool message to make sure\
            # the resulting chat history is valid. See the paragraph above for more information.\
            update={"messages": state["messages"] + [tool_message]},\
        )\
\
    return handoff_to_agent\
\
```\
\
API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) \| [InjectedToolCallId](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.InjectedToolCallId.html) \| [InjectedState](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedState)\
\
### Using with a custom agent [¶](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/\#using-with-a-custom-agent "Permanent link")\
\
To demonstrate how to use handoff tools, let's first implement a simple version of the prebuilt [create\_react\_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent). This is useful in case you want to have a custom tool-calling agent implementation and want to leverage handoff tools.\
\
```md-code__content\
from typing_extensions import Literal\
from langchain_core.messages import ToolMessage\
from langchain_core.tools import tool\
from langgraph.graph import MessagesState, StateGraph, START\
from langgraph.types import Command\
\
def make_agent(model, tools, system_prompt=None):\
    model_with_tools = model.bind_tools(tools)\
    tools_by_name = {tool.name: tool for tool in tools}\
\
    def call_model(state: MessagesState) -> Command[Literal["call_tools", "__end__"]]:\
        messages = state["messages"]\
        if system_prompt:\
            messages = [{"role": "system", "content": system_prompt}] + messages\
\
        response = model_with_tools.invoke(messages)\
        if len(response.tool_calls) > 0:\
            return Command(goto="call_tools", update={"messages": [response]})\
\
        return {"messages": [response]}\
\
    # NOTE: this is a simplified version of the prebuilt ToolNode\
    # If you want to have a tool node that has full feature parity, please refer to the source code\
    def call_tools(state: MessagesState) -> Command[Literal["call_model"]]:\
        tool_calls = state["messages"][-1].tool_calls\
        results = []\
        for tool_call in tool_calls:\
            tool_ = tools_by_name[tool_call["name"]]\
            tool_input_fields = tool_.get_input_schema().model_json_schema()[\
                "properties"\
            ]\
\
            # this is simplified for demonstration purposes and\
            # is different from the ToolNode implementation\
            if "state" in tool_input_fields:\
                # inject state\
                tool_call = {**tool_call, "args": {**tool_call["args"], "state": state}}\
\
            tool_response = tool_.invoke(tool_call)\
            if isinstance(tool_response, ToolMessage):\
                results.append(Command(update={"messages": [tool_response]}))\
\
            # handle tools that return Command directly\
            elif isinstance(tool_response, Command):\
                results.append(tool_response)\
\
        # NOTE: nodes in LangGraph allow you to return list of updates, including Command objects\
        return results\
\
    graph = StateGraph(MessagesState)\
    graph.add_node(call_model)\
    graph.add_node(call_tools)\
    graph.add_edge(START, "call_model")\
    graph.add_edge("call_tools", "call_model")\
\
    return graph.compile()\
\
```\
\
API Reference: [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html) \| [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) \| [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) \| [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) \| [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)\
\
Let's also define math tools that we'll give our agents:\
\
```md-code__content\
@tool\
def add(a: int, b: int) -> int:\
    """Adds two numbers."""\
    return a + b\
\
@tool\
def multiply(a: int, b: int) -> int:\
    """Multiplies two numbers."""\
    return a * b\
\
```\
\
Let's test the agent implementation out to make sure it's working as expected:\
\
```md-code__content\
agent = make_agent(model, [add, multiply])\
\
for chunk in agent.stream({"messages": [("user", "what's (3 + 5) * 12")]}):\
    pretty_print_messages(chunk)\
\
```\
\
```md-code__content\
Update from node call_model:\
\
==================================[1m Ai Message [0m==================================\
\
[{'text': "I'll help break this down into two steps:\n1. First calculate 3 + 5\n2. Then multiply that result by 12\n\nLet me make these calculations:\n\n1. Adding 3 and 5:", 'type': 'text'}, {'id': 'toolu_01DUAzgWFqq6XZtj1hzHTka9', 'input': {'a': 3, 'b': 5}, 'name': 'add', 'type': 'tool_use'}]\
Tool Calls:\
  add (toolu_01DUAzgWFqq6XZtj1hzHTka9)\
 Call ID: toolu_01DUAzgWFqq6XZtj1hzHTka9\
  Args:\
    a: 3\
    b: 5\
\
Update from node call_tools:\
\
=================================[1m Tool Message [0m=================================\
Name: add\
\
8\
\
Update from node call_model:\
\
==================================[1m Ai Message [0m==================================\
\
[{'text': '2. Multiplying the result (8) by 12:', 'type': 'text'}, {'id': 'toolu_01QXi1prSN4etgJ1QCuFJsgN', 'input': {'a': 8, 'b': 12}, 'name': 'multiply', 'type': 'tool_use'}]\
Tool Calls:\
  multiply (toolu_01QXi1prSN4etgJ1QCuFJsgN)\
 Call ID: toolu_01QXi1prSN4etgJ1QCuFJsgN\
  Args:\
    a: 8\
    b: 12\
\
Update from node call_tools:\
\
=================================[1m Tool Message [0m=================================\
Name: multiply\
\
96\
\
Update from node call_model:\
\
==================================[1m Ai Message [0m==================================\
\
The result of (3 + 5) * 12 = 96\
\
```\
\
Now, we can implement our multi-agent system with the multiplication and addition expert agents. This time we'll give them the tools for doing math, as well as our special handoff tools:\
\
```md-code__content\
addition_expert = make_agent(\
    model,\
    [add, make_handoff_tool(agent_name="multiplication_expert")],\
    system_prompt="You are an addition expert, you can ask the multiplication expert for help with multiplication.",\
)\
multiplication_expert = make_agent(\
    model,\
    [multiply, make_handoff_tool(agent_name="addition_expert")],\
    system_prompt="You are a multiplication expert, you can ask an addition expert for help with addition.",\
)\
\
builder = StateGraph(MessagesState)\
builder.add_node("addition_expert", addition_expert)\
builder.add_node("multiplication_expert", multiplication_expert)\
builder.add_edge(START, "addition_expert")\
graph = builder.compile()\
\
```\
\
Let's run the graph with the same multi-step calculation input as before:\
\
```md-code__content\
for chunk in graph.stream(\
    {"messages": [("user", "what's (3 + 5) * 12")]}, subgraphs=True\
):\
    pretty_print_messages(chunk)\
\
```\
\
```md-code__content\
Update from subgraph addition_expert:\
\
Update from node call_model:\
\
==================================[1m Ai Message [0m==================================\
\
[{'text': "I can help with the addition part (3 + 5), but I'll need to ask the multiplication expert for help with multiplying the result by 12. Let me break this down:\n\n1. First, let me calculate 3 + 5:", 'type': 'text'}, {'id': 'toolu_01McaW4XWczLGKaetg88fxQ5', 'input': {'a': 3, 'b': 5}, 'name': 'add', 'type': 'tool_use'}]\
Tool Calls:\
  add (toolu_01McaW4XWczLGKaetg88fxQ5)\
 Call ID: toolu_01McaW4XWczLGKaetg88fxQ5\
  Args:\
    a: 3\
    b: 5\
\
Update from subgraph addition_expert:\
\
Update from node call_tools:\
\
=================================[1m Tool Message [0m=================================\
Name: add\
\
8\
\
Update from subgraph addition_expert:\
\
Update from node call_model:\
\
==================================[1m Ai Message [0m==================================\
\
[{'text': "Now that we have 8, we need to multiply it by 12. I'll ask the multiplication expert for help with this:", 'type': 'text'}, {'id': 'toolu_01KpdUhHuyrmha62z5SduKRc', 'input': {}, 'name': 'transfer_to_multiplication_expert', 'type': 'tool_use'}]\
Tool Calls:\
  transfer_to_multiplication_expert (toolu_01KpdUhHuyrmha62z5SduKRc)\
 Call ID: toolu_01KpdUhHuyrmha62z5SduKRc\
  Args:\
\
Update from subgraph multiplication_expert:\
\
Update from node call_model:\
\
==================================[1m Ai Message [0m==================================\
\
[{'text': 'Now that we have 8 as the result of the addition, I can help with the multiplication by 12:', 'type': 'text'}, {'id': 'toolu_01Vnp4k3TE87siad3BNJgRKb', 'input': {'a': 8, 'b': 12}, 'name': 'multiply', 'type': 'tool_use'}]\
Tool Calls:\
  multiply (toolu_01Vnp4k3TE87siad3BNJgRKb)\
 Call ID: toolu_01Vnp4k3TE87siad3BNJgRKb\
  Args:\
    a: 8\
    b: 12\
\
Update from subgraph multiplication_expert:\
\
Update from node call_tools:\
\
=================================[1m Tool Message [0m=================================\
Name: multiply\
\
96\
\
Update from subgraph multiplication_expert:\
\
Update from node call_model:\
\
==================================[1m Ai Message [0m==================================\
\
The final result is 96.\
\
To break down the steps:\
1. 3 + 5 = 8\
2. 8 * 12 = 96\
\
```\
\
We can see that after the addition expert is done with the first part of the calculation (after calling the `add` tool), it decides to hand off to the multiplication expert, which computes the final result.\
\
## Using with a prebuilt ReAct agent [¶](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/\#using-with-a-prebuilt-react-agent "Permanent link")\
\
If you don't need extra customization, you can use the prebuilt [`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent), which includes built-in support for handoff tools through [`ToolNode`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode).\
\
```md-code__content\
from langgraph.prebuilt import create_react_agent\
\
addition_expert = create_react_agent(\
    model,\
    [add, make_handoff_tool(agent_name="multiplication_expert")],\
    prompt="You are an addition expert, you can ask the multiplication expert for help with multiplication.",\
)\
\
multiplication_expert = create_react_agent(\
    model,\
    [multiply, make_handoff_tool(agent_name="addition_expert")],\
    prompt="You are a multiplication expert, you can ask an addition expert for help with addition.",\
)\
\
builder = StateGraph(MessagesState)\
builder.add_node("addition_expert", addition_expert)\
builder.add_node("multiplication_expert", multiplication_expert)\
builder.add_edge(START, "addition_expert")\
graph = builder.compile()\
\
```\
\
API Reference: [create\_react\_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)\
\
We can now verify that the prebuilt ReAct agent works exactly the same as the custom agent above:\
\
```md-code__content\
for chunk in graph.stream(\
    {"messages": [("user", "what's (3 + 5) * 12")]}, subgraphs=True\
):\
    pretty_print_messages(chunk)\
\
```\
\
```md-code__content\
Update from subgraph addition_expert:\
\
Update from node agent:\
\
==================================[1m Ai Message [0m==================================\
\
[{'text': "I can help with the addition part of this calculation (3 + 5), and then I'll need to ask the multiplication expert for help with multiplying the result by 12.\n\nLet me first calculate 3 + 5:", 'type': 'text'}, {'id': 'toolu_01GUasumGGJVXDV7TJEqEfmY', 'input': {'a': 3, 'b': 5}, 'name': 'add', 'type': 'tool_use'}]\
Tool Calls:\
  add (toolu_01GUasumGGJVXDV7TJEqEfmY)\
 Call ID: toolu_01GUasumGGJVXDV7TJEqEfmY\
  Args:\
    a: 3\
    b: 5\
\
Update from subgraph addition_expert:\
\
Update from node tools:\
\
=================================[1m Tool Message [0m=================================\
Name: add\
\
8\
\
Update from subgraph addition_expert:\
\
Update from node agent:\
\
==================================[1m Ai Message [0m==================================\
\
[{'text': "Now that we have 8, we need to multiply it by 12. Since I'm an addition expert, I'll transfer this to the multiplication expert to complete the calculation:", 'type': 'text'}, {'id': 'toolu_014HEbwiH2jVno8r1Pc6t9Qh', 'input': {}, 'name': 'transfer_to_multiplication_expert', 'type': 'tool_use'}]\
Tool Calls:\
  transfer_to_multiplication_expert (toolu_014HEbwiH2jVno8r1Pc6t9Qh)\
 Call ID: toolu_014HEbwiH2jVno8r1Pc6t9Qh\
  Args:\
\
Update from subgraph multiplication_expert:\
\
Update from node agent:\
\
==================================[1m Ai Message [0m==================================\
\
[{'text': 'I notice I made a mistake - I actually don\'t have access to the "add" function or "transfer_to_multiplication_expert". Instead, I am the multiplication expert and I should ask the addition expert for help with the first part. Let me correct this:', 'type': 'text'}, {'id': 'toolu_01VAGpmr4ysHjvvuZp3q5Dzj', 'input': {}, 'name': 'transfer_to_addition_expert', 'type': 'tool_use'}]\
Tool Calls:\
  transfer_to_addition_expert (toolu_01VAGpmr4ysHjvvuZp3q5Dzj)\
 Call ID: toolu_01VAGpmr4ysHjvvuZp3q5Dzj\
  Args:\
\
Update from subgraph addition_expert:\
\
Update from node agent:\
\
==================================[1m Ai Message [0m==================================\
\
[{'text': "I'll help you with the addition part of (3 + 5) * 12. First, let me calculate 3 + 5:", 'type': 'text'}, {'id': 'toolu_01RE16cRGVo4CC4wwHFB6gaE', 'input': {'a': 3, 'b': 5}, 'name': 'add', 'type': 'tool_use'}]\
Tool Calls:\
  add (toolu_01RE16cRGVo4CC4wwHFB6gaE)\
 Call ID: toolu_01RE16cRGVo4CC4wwHFB6gaE\
  Args:\
    a: 3\
    b: 5\
\
Update from subgraph addition_expert:\
\
Update from node tools:\
\
=================================[1m Tool Message [0m=================================\
Name: add\
\
8\
\
Update from subgraph addition_expert:\
\
Update from node agent:\
\
==================================[1m Ai Message [0m==================================\
\
[{'text': "Now that we have 8, we need to multiply it by 12. Since I'm an addition expert, I'll need to transfer this to the multiplication expert to complete the calculation:", 'type': 'text'}, {'id': 'toolu_01HBDRh64SzGcCp7EX1u3MFa', 'input': {}, 'name': 'transfer_to_multiplication_expert', 'type': 'tool_use'}]\
Tool Calls:\
  transfer_to_multiplication_expert (toolu_01HBDRh64SzGcCp7EX1u3MFa)\
 Call ID: toolu_01HBDRh64SzGcCp7EX1u3MFa\
  Args:\
\
Update from subgraph multiplication_expert:\
\
Update from node agent:\
\
==================================[1m Ai Message [0m==================================\
\
[{'text': 'Now that I have the result of 3 + 5 = 8, I can help with multiplying by 12:', 'type': 'text'}, {'id': 'toolu_014Ay95rsKvvbWWJV4CcZSPY', 'input': {'a': 8, 'b': 12}, 'name': 'multiply', 'type': 'tool_use'}]\
Tool Calls:\
  multiply (toolu_014Ay95rsKvvbWWJV4CcZSPY)\
 Call ID: toolu_014Ay95rsKvvbWWJV4CcZSPY\
  Args:\
    a: 8\
    b: 12\
\
Update from subgraph multiplication_expert:\
\
Update from node tools:\
\
=================================[1m Tool Message [0m=================================\
Name: multiply\
\
96\
\
Update from subgraph multiplication_expert:\
\
Update from node agent:\
\
==================================[1m Ai Message [0m==================================\
\
The final result is 96. Here's the complete calculation:\
(3 + 5) * 12 = 8 * 12 = 96\
\
```\
\
## Comments\
\
giscus\
\
#### [1 reaction](https://github.com/langchain-ai/langgraph/discussions/2840)\
\
👍1\
\
#### [3 comments](https://github.com/langchain-ai/langgraph/discussions/2840)\
\
_– powered by [giscus](https://giscus.app/)_\
\
- Oldest\
- Newest\
\
[![@lesong36](https://avatars.githubusercontent.com/u/85875665?v=4)lesong36](https://github.com/lesong36) [Dec 27, 2024](https://github.com/langchain-ai/langgraph/discussions/2840#discussioncomment-11674990)\
\
it's better off to use have more clear state\_modifier, as below, for handoffs using tools and ReAct agent.\
\
state\_modifier="You are an addition expert, you can ask the multiplication expert for help with multiplication, Always do your portion of calculation before the handoff.",\
\
and\
\
state\_modifier="You are a multiplication expert, you can ask an addition expert for help with addition, Always do your portion of calculation before the handoff.",\
\
1\
\
0 replies\
\
[![@lesong36](https://avatars.githubusercontent.com/u/85875665?v=4)lesong36](https://github.com/lesong36) [Jan 23](https://github.com/langchain-ai/langgraph/discussions/2840#discussioncomment-11926558)\
\
so if no explicated edge or command, how can we get the correct visualization?\
\
1\
\
👍1\
\
0 replies\
\
[![@nick-youngblut](https://avatars.githubusercontent.com/u/2468572?u=257f896c1ce6dca97e0a7d840725cbc023a71839&v=4)nick-youngblut](https://github.com/nick-youngblut) [Feb 2](https://github.com/langchain-ai/langgraph/discussions/2840#discussioncomment-12034250)\
\
An error is thrown if the agent (e.g., react agent) is invoked outside of the graph context. Very annoying when directly testing agents.\
\
1\
\
0 replies\
\
WritePreview\
\
[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")\
\
[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fhow-tos%2Fagent-handoffs%2F)