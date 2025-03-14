[Skip to content](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/#langgraph-platform)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/langgraph_platform.md "Edit this page")

# LangGraph Platform [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/\#langgraph-platform "Permanent link")

## Overview [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/\#overview "Permanent link")

LangGraph Platform is a commercial solution for deploying agentic applications to production, built on the open-source [LangGraph framework](https://langchain-ai.github.io/langgraph/concepts/high_level/).

The LangGraph Platform consists of several components that work together to support the development, deployment, debugging, and monitoring of LangGraph applications:

- [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/): The server defines an opinionated API and architecture that incorporates best practices for deploying agentic applications, allowing you to focus on building your agent logic rather than developing server infrastructure.
- [LangGraph Studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/): LangGraph Studio is a specialized IDE that can connect to a LangGraph Server to enable visualization, interaction, and debugging of the application locally.
- [LangGraph CLI](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/): LangGraph CLI is a command-line interface that helps to interact with a local LangGraph
- [Python/JS SDK](https://langchain-ai.github.io/langgraph/concepts/sdk/): The Python/JS SDK provides a programmatic way to interact with deployed LangGraph Applications.
- [Remote Graph](https://langchain-ai.github.io/langgraph/how-tos/use-remote-graph/): A RemoteGraph allows you to interact with any deployed LangGraph application as though it were running locally.

![](https://langchain-ai.github.io/langgraph/concepts/img/lg_platform.png)

The LangGraph Platform offers a few different deployment options described in the [deployment options guide](https://langchain-ai.github.io/langgraph/concepts/deployment_options/).

## Why Use LangGraph Platform? [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/\#why-use-langgraph-platform "Permanent link")

**LangGraph Platform** handles common issues that arise when deploying LLM applications to production, allowing you to focus on agent logic instead of managing server infrastructure.

- **[Streaming Support](https://langchain-ai.github.io/langgraph/concepts/streaming/)**: As agents grow more sophisticated, they often benefit from streaming both token outputs and intermediate states back to the user. Without this, users are left waiting for potentially long operations with no feedback. LangGraph Server provides [multiple streaming modes](https://langchain-ai.github.io/langgraph/concepts/streaming/) optimized for various application needs.

- **Background Runs**: For agents that take longer to process (e.g., hours), maintaining an open connection can be impractical. The LangGraph Server supports launching agent runs in the background and provides both polling endpoints and webhooks to monitor run status effectively.

- **Support for long runs**: Vanilla server setups often encounter timeouts or disruptions when handling requests that take a long time to complete. LangGraph Server’s API provides robust support for these tasks by sending regular heartbeat signals, preventing unexpected connection closures during prolonged processes.

- **Handling Burstiness**: Certain applications, especially those with real-time user interaction, may experience "bursty" request loads where numerous requests hit the server simultaneously. LangGraph Server includes a task queue, ensuring requests are handled consistently without loss, even under heavy loads.

- **[Double Texting](https://langchain-ai.github.io/langgraph/concepts/double_texting/)**: In user-driven applications, it’s common for users to send multiple messages rapidly. This “double texting” can disrupt agent flows if not handled properly. LangGraph Server offers built-in strategies to address and manage such interactions.

- **[Checkpointers and Memory Management](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints)**: For agents needing persistence (e.g., conversation memory), deploying a robust storage solution can be complex. LangGraph Platform includes optimized [checkpointers](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints) and a [memory store](https://langchain-ai.github.io/langgraph/concepts/persistence/#memory-store), managing state across sessions without the need for custom solutions.

- **[Human-in-the-loop Support](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)**: In many applications, users require a way to intervene in agent processes. LangGraph Server provides specialized endpoints for human-in-the-loop scenarios, simplifying the integration of manual oversight into agent workflows.


By using LangGraph Platform, you gain access to a robust, scalable deployment solution that mitigates these challenges, saving you the effort of implementing and maintaining them manually. This allows you to focus more on building effective agent behavior and less on solving deployment infrastructure issues.

## Comments

giscus

#### [1 reaction](https://github.com/langchain-ai/langgraph/discussions/2287)

👍1

#### [2 comments](https://github.com/langchain-ai/langgraph/discussions/2287)

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@vinay-gatech](https://avatars.githubusercontent.com/u/184368402?v=4)vinay-gatech](https://github.com/vinay-gatech) [Nov 1, 2024](https://github.com/langchain-ai/langgraph/discussions/2287#discussioncomment-11118649)

This is a fantastic development in the space of agentic applications!

This will undoubtedly accelerate the adoption of agentic systems in production, allowing engineers to focus on crafting sophisticated agent logic without getting bogged down by infrastructure hurdles. LangGraph is truly pushing the envelope for scalable, interactive AI applications!

1

0 replies

[![@datAgent77](https://avatars.githubusercontent.com/u/39218822?v=4)datAgent77](https://github.com/datAgent77) [Jan 14](https://github.com/langchain-ai/langgraph/discussions/2287#discussioncomment-11827807)

That is very fantastic development for focusing only logic of business.

1

0 replies

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fconcepts%2Flanggraph_platform%2F)