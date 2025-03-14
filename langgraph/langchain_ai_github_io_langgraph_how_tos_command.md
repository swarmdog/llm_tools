[Skip to content](https://langchain-ai.github.io/langgraph/how-tos/command/#how-to-combine-control-flow-and-state-updates-with-command)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/command.ipynb "Edit this page")

# How to combine control flow and state updates with Command [¶](https://langchain-ai.github.io/langgraph/how-tos/command/\#how-to-combine-control-flow-and-state-updates-with-command "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

- [State](https://langchain-ai.github.io/langgraph/concepts/low_level#state)
- [Nodes](https://langchain-ai.github.io/langgraph/concepts/low_level#nodes)
- [Edges](https://langchain-ai.github.io/langgraph/concepts/low_level#edges)
- [Command](https://langchain-ai.github.io/langgraph/concepts/low_level#command)

It can be useful to combine control flow (edges) and state updates (nodes). For example, you might want to BOTH perform state updates AND decide which node to go to next in the SAME node. LangGraph provides a way to do so by returning a `Command` object from node functions:

```md-code__content
def my_node(state: State) -> Command[Literal["my_other_node"]]:
    return Command(
        # state update
        update={"foo": "bar"},
        # control flow
        goto="my_other_node"
    )

```

If you are using [subgraphs](https://langchain-ai.github.io/langgraph/how-tos/command/#subgraphs), you might want to navigate from a node a subgraph to a different subgraph (i.e. a different node in the parent graph). To do so, you can specify `graph=Command.PARENT` in `Command`:

```md-code__content
def my_node(state: State) -> Command[Literal["my_other_node"]]:
    return Command(
        update={"foo": "bar"},
        goto="other_subgraph",  # where `other_subgraph` is a node in the parent graph
        graph=Command.PARENT
    )

```

State updates with `Command.PARENT`

When you send updates from a subgraph node to a parent graph node for a key that's shared by both parent and subgraph [state schemas](https://langchain-ai.github.io/langgraph/concepts/low_level#schema), you **must** define a [reducer](https://langchain-ai.github.io/langgraph/concepts/low_level#reducers) for the key you're updating in the parent graph state. See this [example](https://langchain-ai.github.io/langgraph/how-tos/command/#navigating-to-a-node-in-a-parent-graph) below.

This guide shows how you can do use `Command` to add dynamic control flow in your LangGraph app.

## Setup [¶](https://langchain-ai.github.io/langgraph/how-tos/command/\#setup "Permanent link")

First, let's install the required packages

```md-code__content
%%capture --no-stderr
%pip install -U langgraph

```

Set up [LangSmith](https://smith.langchain.com/) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com/).


Let's create a simple graph with 3 nodes: A, B and C. We will first execute node A, and then decide whether to go to Node B or Node C next based on the output of node A.

## Basic usage [¶](https://langchain-ai.github.io/langgraph/how-tos/command/\#basic-usage "Permanent link")

```md-code__content
import random
from typing_extensions import TypedDict, Literal

from langgraph.graph import StateGraph, START
from langgraph.types import Command

# Define graph state
class State(TypedDict):
    foo: str

# Define the nodes

def node_a(state: State) -> Command[Literal["node_b", "node_c"]]:
    print("Called A")
    value = random.choice(["a", "b"])
    # this is a replacement for a conditional edge function
    if value == "a":
        goto = "node_b"
    else:
        goto = "node_c"

    # note how Command allows you to BOTH update the graph state AND route to the next node
    return Command(
        # this is the state update
        update={"foo": value},
        # this is a replacement for an edge
        goto=goto,
    )

def node_b(state: State):
    print("Called B")
    return {"foo": state["foo"] + "b"}

def node_c(state: State):
    print("Called C")
    return {"foo": state["foo"] + "c"}

```

API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) \| [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) \| [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

We can now create the `StateGraph` with the above nodes. Notice that the graph doesn't have [conditional edges](https://langchain-ai.github.io/langgraph/concepts/low_level#conditional-edges) for routing! This is because control flow is defined with `Command` inside `node_a`.

```md-code__content
builder = StateGraph(State)
builder.add_edge(START, "node_a")
builder.add_node(node_a)
builder.add_node(node_b)
builder.add_node(node_c)
# NOTE: there are no edges between nodes A, B and C!

graph = builder.compile()

```

Important

You might have noticed that we used `Command` as a return type annotation, e.g. `Command[Literal["node_b", "node_c"]]`. This is necessary for the graph rendering and tells LangGraph that `node_a` can navigate to `node_b` and `node_c`.

```md-code__content
from IPython.display import display, Image

display(Image(graph.get_graph().draw_mermaid_png()))

```

![](<Base64-Image-Removed>)

If we run the graph multiple times, we'd see it take different paths (A -> B or A -> C) based on the random choice in node A.

```md-code__content
graph.invoke({"foo": ""})

```

```md-code__content
Called A
Called C

```

```md-code__content
{'foo': 'bc'}

```

## Navigating to a node in a parent graph [¶](https://langchain-ai.github.io/langgraph/how-tos/command/\#navigating-to-a-node-in-a-parent-graph "Permanent link")

Now let's demonstrate how you can navigate from inside a subgraph to a different node in a parent graph. We'll do so by changing `node_a` in the above example into a single-node graph that we'll add as a subgraph to our parent graph.

State updates with `Command.PARENT`

When you send updates from a subgraph node to a parent graph node for a key that's shared by both parent and subgraph [state schemas](https://langchain-ai.github.io/langgraph/concepts/low_level#schema), you **must** define a [reducer](https://langchain-ai.github.io/langgraph/concepts/low_level#reducers) for the key you're updating in the parent graph state.

```md-code__content
import operator
from typing_extensions import Annotated

class State(TypedDict):
    # NOTE: we define a reducer here
    foo: Annotated[str, operator.add]

def node_a(state: State):
    print("Called A")
    value = random.choice(["a", "b"])
    # this is a replacement for a conditional edge function
    if value == "a":
        goto = "node_b"
    else:
        goto = "node_c"

    # note how Command allows you to BOTH update the graph state AND route to the next node
    return Command(
        update={"foo": value},
        goto=goto,
        # this tells LangGraph to navigate to node_b or node_c in the parent graph
        # NOTE: this will navigate to the closest parent graph relative to the subgraph
        graph=Command.PARENT,
    )

subgraph = StateGraph(State).add_node(node_a).add_edge(START, "node_a").compile()

def node_b(state: State):
    print("Called B")
    # NOTE: since we've defined a reducer, we don't need to manually append
    # new characters to existing 'foo' value. instead, reducer will append these
    # automatically (via operator.add)
    return {"foo": "b"}

def node_c(state: State):
    print("Called C")
    return {"foo": "c"}

```

```md-code__content
builder = StateGraph(State)
builder.add_edge(START, "subgraph")
builder.add_node("subgraph", subgraph)
builder.add_node(node_b)
builder.add_node(node_c)

graph = builder.compile()

```

```md-code__content
graph.invoke({"foo": ""})

```

```md-code__content
Called A
Called C

```

```md-code__content
{'foo': 'bc'}

```

## Comments

giscus

#### [3 reactions](https://github.com/langchain-ai/langgraph/discussions/2654)

👍2🎉1

#### [13 comments](https://github.com/langchain-ai/langgraph/discussions/2654)

#### ·

#### 16 replies

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@DorSimoni](https://avatars.githubusercontent.com/u/73647914?v=4)DorSimoni](https://github.com/DorSimoni) [Dec 5, 2024](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11475925)

Hey,

First, thank you for your contribution and efforts.

I'm encountering some issues with implementing "Command".

I'm using the most updated LangGraph version (0.2.56).

I see that "goto" parameter does not exist in Command class, and "update" parameter does not exist in GraphCommand class either.

Did I miss something?

My goal is to iterate through a list of objects. For each object that I classify as "yes," I want to return it to the user (edge END?) while, at the same time, allowing the graph to continue classifying the remaining objects.

Within the loop, I have conditions to check whether I have classified enough objects and whether I have classified enough "yes" responses.

I thought using Command might be a good approach for this.

Would you suggest a different solution?

Thanks,

Dor

1

2 replies

[![@vbarda](https://avatars.githubusercontent.com/u/19161700?u=e76bcd472b51c9f07befd2654783d0a381f49005&v=4)](https://github.com/vbarda)

[vbarda](https://github.com/vbarda) [Dec 5, 2024](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11477997)

Collaborator

[@DorSimoni](https://github.com/DorSimoni) you shouldn't see `GraphCommand` at all in the latest version of `LangGraph`, only `Command`, could you please double check in a fresh virtual environment?

as for you idea, could you clarity: what does it mean to "return to the user" in this case? is the user supposed to take any additional actions?

[![@DorSimoni](https://avatars.githubusercontent.com/u/73647914?v=4)](https://github.com/DorSimoni)

[DorSimoni](https://github.com/DorSimoni) [Dec 6, 2024](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11491031)

Thanks for your quick response.

I tried it in a clean virtual environment, and the Command function now has the correct parameters.

As for the idea, sorry for the confusion. By "return to the user," I meant that the graph will output an answer to the user while continuing to classify more documents. Each document classified as "yes" will be output to the user.

The user is not supposed to take any additional actions (at least not at this stage. in the next stage, they will, but that's a different challenge for HILP).

[![@samgoos7](https://avatars.githubusercontent.com/u/139918151?v=4)samgoos7](https://github.com/samgoos7) [Dec 10, 2024](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11524275)

I am having issues with using Command, im getting the following error: TypeError: Command. **init**() got an unexpected keyword argument 'goto'

Even when running the exact examples in shown on this page, including the imports.

Am I doing something wrong?

Thanks,

Sam

1

1 reply

[![@vbarda](https://avatars.githubusercontent.com/u/19161700?u=e76bcd472b51c9f07befd2654783d0a381f49005&v=4)](https://github.com/vbarda)

[vbarda](https://github.com/vbarda) [Dec 11, 2024](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11538243)

Collaborator

hm, i would recommend reinstalling in a fresh virtualenv, but please let me know if that doesn't help

[![@dillon-nidoai](https://avatars.githubusercontent.com/u/189019555?v=4)dillon-nidoai](https://github.com/dillon-nidoai) [Dec 10, 2024](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11524477)

Is this meant to replace SEND? Or be more of an augmentation to be able to map reduce while updating state. Should commands replace conditional edges?

0

7 replies

Show 2 previous replies

[![@gbaian10](https://avatars.githubusercontent.com/u/34255899?u=05aba76f1912a56538c8a5141f8135d0e3b1e1bd&v=4)](https://github.com/gbaian10)

[gbaian10](https://github.com/gbaian10) [Dec 11, 2024](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11527892)

Contributor

[@samgoos7](https://github.com/samgoos7) You mentioned a question I've always wanted to know about.

In the past, when there was only a conditional edge, were we unable to both enter the edge's route and update the state simultaneously?

Was the Command introduced to solve this issue?

👍1

[![@dillon-nidoai](https://avatars.githubusercontent.com/u/189019555?v=4)](https://github.com/dillon-nidoai)

[dillon-nidoai](https://github.com/dillon-nidoai) [Dec 11, 2024](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11528224)

edited

I don't think so. Since state updates only when you return the state from my experience. So you would have to update state before entering a conditional edge then return the node you want to route to.

I was more wondering if you could branch and run branches in parallel with independent instances of state with Command. For example, I was playing with a conditional \[Send("update\_node") for s in state\["value"\]\] to another conditional (update\_node, router) which returned the node to go to. But I wasn't able to continue down these branches and would have to reduce. So I wonder with Command if I can maintain and run those independent instances then reduce later. (Sorry I know this wasn't really part of the question lol)

[![@samgoos7](https://avatars.githubusercontent.com/u/139918151?v=4)](https://github.com/samgoos7)

[samgoos7](https://github.com/samgoos7) [Dec 11, 2024](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11529777)

[@gbaian10](https://github.com/gbaian10) yeah at least that is my use case. For example retrieving tool content message from messages state and updating the state, and go to the next node based on that update. Previously you had to do that with different steps (update state node + router node for conditional edge) and now you can do this simoultaneously with Command

👍1

[![@vbarda](https://avatars.githubusercontent.com/u/19161700?u=e76bcd472b51c9f07befd2654783d0a381f49005&v=4)](https://github.com/vbarda)

[vbarda](https://github.com/vbarda) [Dec 11, 2024](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11538267)

Collaborator

`Command` was primarily introduced to allow combining control flow (edges) and state updates (which as folks pointed out was a common problem with conditional edges). it is NOT meant to replace `Send` but you can use it with `Send` as well, we'll add examples

[![@DotCSanova](https://avatars.githubusercontent.com/u/177200921?u=535f16dc3707ad10b0487c9327de58bcdb9682f7&v=4)](https://github.com/DotCSanova)

[DotCSanova](https://github.com/DotCSanova) [13 days ago](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-12350127)

Hello, have you already added examples of how to use Command() with Send()? Thank you!

[![@Saisiva123](https://avatars.githubusercontent.com/u/36258631?v=4)Saisiva123](https://github.com/Saisiva123) [Dec 19, 2024](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11620792)

I think here the output should be {'foo': 'ab'} right? because inside the node A the graph state will get updated to {'foo': 'a'} and then it will navigate to b where the state gets updated to {'foo': 'ab'}.

1

1 reply

[![@Saisiva123](https://avatars.githubusercontent.com/u/36258631?v=4)](https://github.com/Saisiva123)

[Saisiva123](https://github.com/Saisiva123) [Dec 19, 2024](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11622848)

Got confused because inside the node A, it would have been better if we have choosen 'b' and 'c'. random.choice(\["b", "c"\]).

But the output for the above code should look something like this.

Called A

{'node\_a': {'foo': 'a'}}

Called B

{'node\_b': {'foo': 'ab'}}

* * *

Called A

{'node\_a': {'foo': 'b'}}

Called C

{'node\_c': {'foo': 'bc'}}

[![@sctrmn](https://avatars.githubusercontent.com/u/113985831?v=4)sctrmn](https://github.com/sctrmn) [Jan 3](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11726258)

How a ToolNode should use Command?

1

1 reply

[![@Simon-U](https://avatars.githubusercontent.com/u/68547634?v=4)](https://github.com/Simon-U)

[Simon-U](https://github.com/Simon-U) [Jan 9](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11787133)

I tried it, and it seems to work just fine with tools using the Command

[![@Blaqadonis](https://avatars.githubusercontent.com/u/100685852?u=a167c4620e191951f757bf0fa06377df0536c3ca&v=4)Blaqadonis](https://github.com/Blaqadonis) [Jan 11](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11808218)

Could you do a tutorial for an assistant that prompt's a user's feedback many times in the workflow and at different nodes?

1

0 replies

[![@Blaqadonis](https://avatars.githubusercontent.com/u/100685852?u=a167c4620e191951f757bf0fa06377df0536c3ca&v=4)Blaqadonis](https://github.com/Blaqadonis) [Jan 11](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11808317)

Nodes b and c can also be written like this right?

def node\_b(state: State):

print("Called B")

return Command(

update={"foo": state\["foo"\] + "b"}

)

def node\_c(state: State):

print("Called C")

return Command(

update={"foo": state\["foo"\] + "c"}

)

1

0 replies

[![@ajeeth-b](https://avatars.githubusercontent.com/u/33338813?u=819475f200b9df6079df64d7da5dcf915a262a5b&v=4)ajeeth-b](https://github.com/ajeeth-b) [Jan 16](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11851220)

edited

# Unable to See Edges with Class-Based Nodes using `Command` and get see edges in graph.get\_graph(xray=True)

I was trying a class based node, but unable to see edges when I do `graph.get_graph(xray=True)`

this is my class based node definition

```
class MyNode(AbastractClassWithRunMethodOnly)
    def run(self, state, *args) -> Command[Literal['node2', END]]:
         # my logic
         return Command(goto='node2')

# has graph obj
my_node_obj = MyNode()
graph.add_node(my_node_obj.run)
```

this way I'm not able to see the edges .

is there any work around or I'm doing something wrong?

1

1 reply

[![@ajeeth-b](https://avatars.githubusercontent.com/u/33338813?u=819475f200b9df6079df64d7da5dcf915a262a5b&v=4)](https://github.com/ajeeth-b)

[ajeeth-b](https://github.com/ajeeth-b) [Jan 17](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11862744)

edited

resolved above issue in this release few hours ago

[https://github.com/langchain-ai/langgraph/releases/tag/0.2.63](https://github.com/langchain-ai/langgraph/releases/tag/0.2.63)

[![@scardonal](https://avatars.githubusercontent.com/u/72363847?u=7f5d0e92693c75aa12eb319d263e6dfb4c0335c8&v=4)scardonal](https://github.com/scardonal) [Jan 22](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11922432)

edited

Hi all. Can I use a Command in this way?

```notranslate
 if relevance_response.relevance == "not_relevant":
    # Drop the last AI message
    delete_messages = [RemoveMessage(id=m.id) for m in messages[-1]]
    return Command(update={"messages": delete_messages}, goto="rewrite_question")
else:
    if len(messages) > 6:
        return Command(goto="summarize_messages")
    else:
        return Command(goto=END)

```

The goal is to apply an if-else condition where if relevance = "not\_relevant," delete the last message and go to the rewrite\_question node. But if the relevance = "is\_relevant," then check the number of messages in the chat history and apply other if-else conditions that could summarize the chat or go to the END node.

1

1 reply

[![@vbarda](https://avatars.githubusercontent.com/u/19161700?u=e76bcd472b51c9f07befd2654783d0a381f49005&v=4)](https://github.com/vbarda)

[vbarda](https://github.com/vbarda) [Jan 22](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-11922550)

Collaborator

yes! you don't even need the the last `else` branch -- if you don't include it the graph will just halt, e.g. this part can be dropped

```notranslate
else:
        return Command(goto=END)

```

👍1

[![@nick-youngblut](https://avatars.githubusercontent.com/u/2468572?u=257f896c1ce6dca97e0a7d840725cbc023a71839&v=4)nick-youngblut](https://github.com/nick-youngblut) [Feb 2](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-12034731)

It appears that `Command` cannot handle a goto to the tool-calling agent, which is useful when the agent calls the wrong goto agent, so you want the calling agent to try again:

```
if agent_name not in available_agents:
    error_message = f"Agent {agent_name} is not available. Choose one of: {', '.join(available_agents)}",
    return Command(
       goto="AGENT_THAT_CALLED_THIS_TOOL",
       update={"messages": [AIMessage(content=error_message)]},
    )
```

The error is: `KeyError: 'branch:tools:__self__:AGENT_THAT_CALLED_THIS_TOOL`

1

0 replies

[![@cnummer1](https://avatars.githubusercontent.com/u/134398318?v=4)cnummer1](https://github.com/cnummer1) [19 days ago](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-12283300)

Is it possible to navigate up more than one parent graph. I have a double nested subgraph and want to goto a node in the most outer parent graph. If it is not currently possible, is there any anticipation of it becoming available in the future?

1

0 replies

[![@Vikramank](https://avatars.githubusercontent.com/u/8142239?u=a4fc34b90db0dde9e19f2aa952f06953b2961745&v=4)Vikramank](https://github.com/Vikramank) [16 days ago](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-12312489)

Hi,

I am trying to implement a sequential flow of agents and routing based on a condition. Which would be better: using Command or conditional\_edge?

1

1 reply

[![@hinthornw](https://avatars.githubusercontent.com/u/13333726?u=82ebf1e0eb0663ebd49ba66f67a43f51bbf11442&v=4)](https://github.com/hinthornw)

[hinthornw](https://github.com/hinthornw) [2 days ago](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-12467851)

Contributor

They both do the same. Command may be slightly more concise.

[![@corps3d](https://avatars.githubusercontent.com/u/157398894?v=4)corps3d](https://github.com/corps3d) [2 days ago](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-12466948)

_This comment was deleted._

1

1 reply

[![@hinthornw](https://avatars.githubusercontent.com/u/13333726?u=82ebf1e0eb0663ebd49ba66f67a43f51bbf11442&v=4)](https://github.com/hinthornw)

[hinthornw](https://github.com/hinthornw) [2 days ago](https://github.com/langchain-ai/langgraph/discussions/2654#discussioncomment-12467850)

Contributor

Share code if you want help. At a glance it seems like you may be _also_ defining edges, which would still run even if you return a Command in the node. LangGraph the framework doesn't hallucinate

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fhow-tos%2Fcommand%2F)