[Skip to content](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#breakpoints)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/breakpoints.md "Edit this page")

# Breakpoints [¶](https://langchain-ai.github.io/langgraph/concepts/breakpoints/\#breakpoints "Permanent link")

Breakpoints pause graph execution at specific points and enable stepping through execution step by step. Breakpoints are powered by LangGraph's [**persistence layer**](https://langchain-ai.github.io/langgraph/concepts/persistence/), which saves the state after each graph step. Breakpoints can also be used to enable [**human-in-the-loop**](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) workflows, though we recommend using the [`interrupt` function](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#interrupt) for this purpose.

## Requirements [¶](https://langchain-ai.github.io/langgraph/concepts/breakpoints/\#requirements "Permanent link")

To use breakpoints, you will need to:

1. [**Specify a checkpointer**](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints) to save the graph state after each step.
2. [**Set breakpoints**](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#setting-breakpoints) to specify where execution should pause.
3. **Run the graph** with a [**thread ID**](https://langchain-ai.github.io/langgraph/concepts/persistence/#threads) to pause execution at the breakpoint.
4. **Resume execution** using `invoke`/ `ainvoke`/ `stream`/ `astream` (see [**The `Command` primitive**](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#the-command-primitive)).

## Setting breakpoints [¶](https://langchain-ai.github.io/langgraph/concepts/breakpoints/\#setting-breakpoints "Permanent link")

There are two places where you can set breakpoints:

1. **Before** or **after** a node executes by setting breakpoints at **compile time** or **run time**. We call these [**static breakpoints**](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#static-breakpoints).
2. **Inside** a node using the [`NodeInterrupt` exception](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#nodeinterrupt-exception).

### Static breakpoints [¶](https://langchain-ai.github.io/langgraph/concepts/breakpoints/\#static-breakpoints "Permanent link")

Static breakpoints are triggered either **before** or **after** a node executes. You can set static breakpoints by specifying `interrupt_before` and `interrupt_after` at **"compile" time** or **run time**.

[Compile time](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__tabbed_1_1)[Run time](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__tabbed_1_2)

```md-code__content
graph = graph_builder.compile(
    interrupt_before=["node_a"],
    interrupt_after=["node_b", "node_c"],
    checkpointer=..., # Specify a checkpointer
)

thread_config = {
    "configurable": {
        "thread_id": "some_thread"
    }
}

# Run the graph until the breakpoint
graph.invoke(inputs, config=thread_config)

# Optionally update the graph state based on user input
graph.update_state(update, config=thread_config)

# Resume the graph
graph.invoke(None, config=thread_config)

```

```md-code__content
graph.invoke(
    inputs,
    config={"configurable": {"thread_id": "some_thread"}},
    interrupt_before=["node_a"],
    interrupt_after=["node_b", "node_c"]
)

thread_config = {
    "configurable": {
        "thread_id": "some_thread"
    }
}

# Run the graph until the breakpoint
graph.invoke(inputs, config=thread_config)

# Optionally update the graph state based on user input
graph.update_state(update, config=thread_config)

# Resume the graph
graph.invoke(None, config=thread_config)

```

Note

You cannot set static breakpoints at runtime for **sub-graphs**.
If you have a sub-graph, you must set the breakpoints at compilation time.

Static breakpoints can be especially useful for debugging if you want to step through the graph execution one
node at a time or if you want to pause the graph execution at specific nodes.

### `NodeInterrupt` exception [¶](https://langchain-ai.github.io/langgraph/concepts/breakpoints/\#nodeinterrupt-exception "Permanent link")

We recommend that you [**use the `interrupt` function instead**](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) of the `NodeInterrupt` exception if you're trying to implement
[human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) workflows. The `interrupt` function is easier to use and more flexible.

`NodeInterrupt` exception

The developer can define some _condition_ that must be met for a breakpoint to be triggered. This concept of _dynamic breakpoints_ is useful when the developer wants to halt the graph under _a particular condition_. This uses a `NodeInterrupt`, which is a special type of exception that can be raised from within a node based upon some condition. As an example, we can define a dynamic breakpoint that triggers when the `input` is longer than 5 characters.

```md-code__content
def my_node(state: State) -> State:
    if len(state['input']) > 5:
        raise NodeInterrupt(f"Received input that is longer than 5 characters: {state['input']}")

    return state

```

Let's assume we run the graph with an input that triggers the dynamic breakpoint and then attempt to resume the graph execution simply by passing in `None` for the input.

```md-code__content
# Attempt to continue the graph execution with no change to state after we hit the dynamic breakpoint
for event in graph.stream(None, thread_config, stream_mode="values"):
    print(event)

```

The graph will _interrupt_ again because this node will be _re-run_ with the same graph state. We need to change the graph state such that the condition that triggers the dynamic breakpoint is no longer met. So, we can simply edit the graph state to an input that meets the condition of our dynamic breakpoint (< 5 characters) and re-run the node.

```md-code__content
# Update the state to pass the dynamic breakpoint
graph.update_state(config=thread_config, values={"input": "foo"})
for event in graph.stream(None, thread_config, stream_mode="values"):
    print(event)

```

Alternatively, what if we want to keep our current input and skip the node ( `my_node`) that performs the check? To do this, we can simply perform the graph update with `as_node="my_node"` and pass in `None` for the values. This will make no update the graph state, but run the update as `my_node`, effectively skipping the node and bypassing the dynamic breakpoint.

```md-code__content
# This update will skip the node `my_node` altogether
graph.update_state(config=thread_config, values=None, as_node="my_node")
for event in graph.stream(None, thread_config, stream_mode="values"):
    print(event)

```

## Additional Resources 📚 [¶](https://langchain-ai.github.io/langgraph/concepts/breakpoints/\#additional-resources "Permanent link")

- [**Conceptual Guide: Persistence**](https://langchain-ai.github.io/langgraph/concepts/persistence/): Read the persistence guide for more context about persistence.
- [**Conceptual Guide: Human-in-the-loop**](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/): Read the human-in-the-loop guide for more context on integrating human feedback into LangGraph applications using breakpoints.
- [**How to View and Update Past Graph State**](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/): Step-by-step instructions for working with graph state that demonstrate the **replay** and **fork** actions.

## Comments

giscus

#### 0 reactions

#### 0 comments

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fconcepts%2Fbreakpoints%2F)