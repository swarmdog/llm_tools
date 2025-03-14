[Skip to content](https://langchain-ai.github.io/langgraph/concepts/double_texting/#double-texting)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/double_texting.md "Edit this page")

# Double Texting [¶](https://langchain-ai.github.io/langgraph/concepts/double_texting/\#double-texting "Permanent link")

Prerequisites

- [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)

Many times users might interact with your graph in unintended ways.
For instance, a user may send one message and before the graph has finished running send a second message.
More generally, users may invoke the graph a second time before the first run has finished.
We call this "double texting".

Currently, LangGraph only addresses this as part of [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/), not in the open source.
The reason for this is that in order to handle this we need to know how the graph is deployed, and since LangGraph Platform deals with deployment the logic needs to live there.
If you do not want to use LangGraph Platform, we describe the options we have implemented in detail below.

![](https://langchain-ai.github.io/langgraph/concepts/img/double_texting.png)

## Reject [¶](https://langchain-ai.github.io/langgraph/concepts/double_texting/\#reject "Permanent link")

This is the simplest option, this just rejects any follow-up runs and does not allow double texting.
See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/reject_concurrent/) for configuring the reject double text option.

## Enqueue [¶](https://langchain-ai.github.io/langgraph/concepts/double_texting/\#enqueue "Permanent link")

This is a relatively simple option which continues the first run until it completes the whole run, then sends the new input as a separate run.
See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/enqueue_concurrent/) for configuring the enqueue double text option.

## Interrupt [¶](https://langchain-ai.github.io/langgraph/concepts/double_texting/\#interrupt "Permanent link")

This option interrupts the current execution but saves all the work done up until that point.
It then inserts the user input and continues from there.

If you enable this option, your graph should be able to handle weird edge cases that may arise.
For example, you could have called a tool but not yet gotten back a result from running that tool.
You may need to remove that tool call in order to not have a dangling tool call.

See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/) for configuring the interrupt double text option.

## Rollback [¶](https://langchain-ai.github.io/langgraph/concepts/double_texting/\#rollback "Permanent link")

This option interrupts the current execution AND rolls back all work done up until that point, including the original run input. It then sends the new user input in, basically as if it was the original input.

See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/) for configuring the rollback double text option.

## Comments

giscus

#### 0 reactions

#### 0 comments

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fconcepts%2Fdouble_texting%2F)