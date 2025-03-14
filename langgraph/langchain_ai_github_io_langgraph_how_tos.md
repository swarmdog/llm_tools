[Skip to content](https://langchain-ai.github.io/langgraph/how-tos/#how-to-guides)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/index.md "Edit this page")

# How-to Guides [¶](https://langchain-ai.github.io/langgraph/how-tos/\#how-to-guides "Permanent link")

Here you’ll find answers to “How do I...?” types of questions. These guides are **goal-oriented** and concrete; they're meant to help you complete a specific task. For conceptual explanations see the [Conceptual guide](https://langchain-ai.github.io/langgraph/concepts/). For end-to-end walk-throughs see [Tutorials](https://langchain-ai.github.io/langgraph/tutorials/). For comprehensive descriptions of every class and function see the [API Reference](https://langchain-ai.github.io/langgraph/reference/).

## LangGraph [¶](https://langchain-ai.github.io/langgraph/how-tos/\#langgraph "Permanent link")

### Graph API Basics [¶](https://langchain-ai.github.io/langgraph/how-tos/\#graph-api-basics "Permanent link")

- [How to update graph state from nodes](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/)
- [How to create a sequence of steps](https://langchain-ai.github.io/langgraph/how-tos/sequence/)
- [How to create branches for parallel execution](https://langchain-ai.github.io/langgraph/how-tos/branching/)
- [How to create and control loops with recursion limits](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/)
- [How to visualize your graph](https://langchain-ai.github.io/langgraph/how-tos/visualization/)

### Fine-grained Control [¶](https://langchain-ai.github.io/langgraph/how-tos/\#fine-grained-control "Permanent link")

These guides demonstrate LangGraph features that grant fine-grained control over the
execution of your graph.

- [How to create map-reduce branches for parallel execution](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/)
- [How to update state and jump to nodes in graphs and subgraphs](https://langchain-ai.github.io/langgraph/how-tos/command/)
- [How to add runtime configuration to your graph](https://langchain-ai.github.io/langgraph/how-tos/configuration/)
- [How to add node retries](https://langchain-ai.github.io/langgraph/how-tos/node-retries/)
- [How to return state before hitting recursion limit](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/)

### Persistence [¶](https://langchain-ai.github.io/langgraph/how-tos/\#persistence "Permanent link")

[LangGraph Persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/) makes it easy to persist state across graph runs (per-thread persistence) and across threads (cross-thread persistence). These how-to guides show how to add persistence to your graph.

- [How to add thread-level persistence to your graph](https://langchain-ai.github.io/langgraph/how-tos/persistence/)
- [How to add thread-level persistence to a subgraph](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/)
- [How to add cross-thread persistence to your graph](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/)
- [How to use Postgres checkpointer for persistence](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/)
- [How to use MongoDB checkpointer for persistence](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/)
- [How to create a custom checkpointer using Redis](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/)

See the below guides for how-to add persistence to your workflow using the [Functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api/):

- [How to add thread-level persistence (functional API)](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/)
- [How to add cross-thread persistence (functional API)](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/)

### Memory [¶](https://langchain-ai.github.io/langgraph/how-tos/\#memory "Permanent link")

LangGraph makes it easy to manage conversation [memory](https://langchain-ai.github.io/langgraph/concepts/memory/) in your graph. These how-to guides show how to implement different strategies for that.

- [How to manage conversation history](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/)
- [How to delete messages](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/)
- [How to add summary conversation memory](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/)
- [How to add long-term memory (cross-thread)](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/)
- [How to use semantic search for long-term memory](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/)

### Human-in-the-loop [¶](https://langchain-ai.github.io/langgraph/how-tos/\#human-in-the-loop "Permanent link")

[Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) functionality allows
you to involve humans in the decision-making process of your graph. These how-to guides show how to implement human-in-the-loop workflows in your graph.

Key workflows:

- [How to wait for user input](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/): A basic example that shows how to implement a human-in-the-loop workflow in your graph using the `interrupt` function.
- [How to review tool calls](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/): Incorporate human-in-the-loop for reviewing/editing/accepting tool call requests before they executed using the `interrupt` function.

Other methods:

- [How to add static breakpoints](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/): Use for debugging purposes. For [**human-in-the-loop**](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) workflows, we recommend the [`interrupt` function](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) instead.
- [How to edit graph state](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/): Edit graph state using `graph.update_state` method. Use this if implementing a **human-in-the-loop** workflow via **static breakpoints**.
- [How to add dynamic breakpoints with `NodeInterrupt`](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/dynamic_breakpoints/): **Not recommended**: Use the [`interrupt` function](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) instead.

See the below guides for how-to implement human-in-the-loop workflows with the
[Functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api/):

- [How to wait for user input (Functional API)](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/)
- [How to review tool calls (Functional API)](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/)

### Time Travel [¶](https://langchain-ai.github.io/langgraph/how-tos/\#time-travel "Permanent link")

[Time travel](https://langchain-ai.github.io/langgraph/concepts/time-travel/) allows you to replay past actions in your LangGraph application to explore alternative paths and debug issues. These how-to guides show how to use time travel in your graph.

- [How to view and update past graph state](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/)

### Streaming [¶](https://langchain-ai.github.io/langgraph/how-tos/\#streaming "Permanent link")

[Streaming](https://langchain-ai.github.io/langgraph/concepts/streaming/) is crucial for enhancing the responsiveness of applications built on LLMs. By displaying output progressively, even before a complete response is ready, streaming significantly improves user experience (UX), particularly when dealing with the latency of LLMs.

- [How to stream](https://langchain-ai.github.io/langgraph/how-tos/streaming/)
- [How to stream LLM tokens](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/)
- [How to stream LLM tokens from specific nodes](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/)
- [How to stream data from within a tool](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/)
- [How to stream from subgraphs](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/)
- [How to disable streaming for models that don't support it](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/)

### Tool calling [¶](https://langchain-ai.github.io/langgraph/how-tos/\#tool-calling "Permanent link")

[Tool calling](https://python.langchain.com/docs/concepts/tool_calling/) is a type of
[chat model](https://python.langchain.com/docs/concepts/chat_models/) API that accepts
tool schemas, along with messages, as input and returns invocations of those tools as
part of the output message.

These how-to guides show common patterns for tool calling with LangGraph:

- [How to call tools using ToolNode](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/)
- [How to handle tool calling errors](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/)
- [How to pass runtime values to tools](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/)
- [How to pass config to tools](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/)
- [How to update graph state from tools](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/)
- [How to handle large numbers of tools](https://langchain-ai.github.io/langgraph/how-tos/many-tools/)

### Subgraphs [¶](https://langchain-ai.github.io/langgraph/how-tos/\#subgraphs "Permanent link")

[Subgraphs](https://langchain-ai.github.io/langgraph/concepts/low_level/#subgraphs) allow you to reuse an existing graph from another graph. These how-to guides show how to use subgraphs:

- [How to use subgraphs](https://langchain-ai.github.io/langgraph/how-tos/subgraph/)
- [How to view and update state in subgraphs](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/)
- [How to transform inputs and outputs of a subgraph](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/)

### Multi-agent [¶](https://langchain-ai.github.io/langgraph/how-tos/\#multi-agent "Permanent link")

[Multi-agent systems](https://langchain-ai.github.io/langgraph/concepts/multi_agent/) are useful to break down complex LLM applications into multiple agents, each responsible for a different part of the application. These how-to guides show how to implement multi-agent systems in LangGraph:

- [How to implement handoffs between agents](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/)
- [How to build a multi-agent network](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/)
- [How to add multi-turn conversation in a multi-agent application](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/)

See the [multi-agent tutorials](https://langchain-ai.github.io/langgraph/tutorials/#multi-agent-systems) for implementations of other multi-agent architectures.

See the below guides for how to implement multi-agent workflows with the [Functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api/):

- [How to build a multi-agent network (functional API)](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/)
- [How to add multi-turn conversation in a multi-agent application (functional API)](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/)

### State Management [¶](https://langchain-ai.github.io/langgraph/how-tos/\#state-management "Permanent link")

- [How to use Pydantic model as graph state](https://langchain-ai.github.io/langgraph/how-tos/state-model/)
- [How to define input/output schema for your graph](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/)
- [How to pass private state between nodes inside the graph](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/)

### Other [¶](https://langchain-ai.github.io/langgraph/how-tos/\#other "Permanent link")

- [How to run graph asynchronously](https://langchain-ai.github.io/langgraph/how-tos/async/)
- [How to force tool-calling agent to structure output](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/)
- [How to pass custom LangSmith run ID for graph runs](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/)
- [How to integrate LangGraph with AutoGen, CrewAI, and other frameworks](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/)

See the below guide for how to integrate with other frameworks using the [Functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api/):

- [How to integrate LangGraph (functional API) with AutoGen, CrewAI, and other frameworks](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration-functional/)

### Prebuilt ReAct Agent [¶](https://langchain-ai.github.io/langgraph/how-tos/\#prebuilt-react-agent "Permanent link")

The LangGraph [prebuilt ReAct agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) is pre-built implementation of a [tool calling agent](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling-agent).

One of the big benefits of LangGraph is that you can easily create your own agent architectures. So while it's fine to start here to build an agent quickly, we would strongly recommend learning how to build your own agent so that you can take full advantage of LangGraph.

These guides show how to use the prebuilt ReAct agent:

- [How to use the pre-built ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/)
- [How to add thread-level memory to a ReAct Agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/)
- [How to add a custom system prompt to a ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-system-prompt/)
- [How to add human-in-the-loop processes to a ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/)
- [How to return structured output from a ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/)
- [How to add semantic search for long-term memory to a ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/#using-in-create-react-agent)

Interested in further customizing the ReAct agent? This guide provides an
overview of its underlying implementation to help you customize for your own needs:

- [How to create prebuilt ReAct agent from scratch](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/)

See the below guide for how-to build ReAct agents with the [Functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api/):

- [How to create a ReAct agent from scratch (Functional API)](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/)

## LangGraph Platform [¶](https://langchain-ai.github.io/langgraph/how-tos/\#langgraph-platform "Permanent link")

This section includes how-to guides for LangGraph Platform.

LangGraph Platform is a commercial solution for deploying agentic applications in production, built on the open-source LangGraph framework.

The LangGraph Platform offers a few different deployment options described in the [deployment options guide](https://langchain-ai.github.io/langgraph/concepts/deployment_options/).

Tip

- LangGraph is an MIT-licensed open-source library, which we are committed to maintaining and growing for the community.
- You can always deploy LangGraph applications on your own infrastructure using the open-source LangGraph project without using LangGraph Platform.

### Application Structure [¶](https://langchain-ai.github.io/langgraph/how-tos/\#application-structure "Permanent link")

Learn how to set up your app for deployment to LangGraph Platform:

- [How to set up app for deployment (requirements.txt)](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/)
- [How to set up app for deployment (pyproject.toml)](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_pyproject/)
- [How to set up app for deployment (JavaScript)](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/)
- [How to add semantic search](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/)
- [How to customize Dockerfile](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/)
- [How to test locally](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/)
- [How to rebuild graph at runtime](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/)
- [How to use LangGraph Platform to deploy CrewAI, AutoGen, and other frameworks](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/)

### Deployment [¶](https://langchain-ai.github.io/langgraph/how-tos/\#deployment "Permanent link")

LangGraph applications can be deployed using LangGraph Cloud, which provides a range of services to help you deploy, manage, and scale your applications.

- [How to deploy to LangGraph cloud](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/)
- [How to deploy to a self-hosted environment](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/)
- [How to interact with the deployment using RemoteGraph](https://langchain-ai.github.io/langgraph/how-tos/use-remote-graph/)

### Authentication & Access Control [¶](https://langchain-ai.github.io/langgraph/how-tos/\#authentication-access-control "Permanent link")

- [How to add custom authentication](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/)
- [How to update the security schema of your OpenAPI spec](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/)

### Modifying the API [¶](https://langchain-ai.github.io/langgraph/how-tos/\#modifying-the-api "Permanent link")

- [How to add custom routes](https://langchain-ai.github.io/langgraph/how-tos/http/custom_routes/)
- [How to add custom middleware](https://langchain-ai.github.io/langgraph/how-tos/http/custom_middleware/)
- [How to add custom lifespan events](https://langchain-ai.github.io/langgraph/how-tos/http/custom_lifespan/)

### Assistants [¶](https://langchain-ai.github.io/langgraph/how-tos/\#assistants "Permanent link")

[Assistants](https://langchain-ai.github.io/langgraph/concepts/assistants/) is a configured instance of a template.

See [SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/#langgraph_sdk.client.AssistantsClient)
for supported endpoints and other details.

- [How to configure agents](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/)
- [How to version assistants](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/)

### Threads [¶](https://langchain-ai.github.io/langgraph/how-tos/\#threads "Permanent link")

See [SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/#langgraph_sdk.client.ThreadsClient)
for supported endpoints and other details.

- [How to copy threads](https://langchain-ai.github.io/langgraph/cloud/how-tos/copy_threads/)
- [How to check status of your threads](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/)

### Runs [¶](https://langchain-ai.github.io/langgraph/how-tos/\#runs "Permanent link")

LangGraph Platform supports multiple types of runs besides streaming runs.

- [How to run an agent in the background](https://langchain-ai.github.io/langgraph/cloud/how-tos/background_run/)
- [How to run multiple agents in the same thread](https://langchain-ai.github.io/langgraph/cloud/how-tos/same-thread/)
- [How to create cron jobs](https://langchain-ai.github.io/langgraph/cloud/how-tos/cron_jobs/)
- [How to create stateless runs](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/)

### Streaming [¶](https://langchain-ai.github.io/langgraph/how-tos/\#streaming_1 "Permanent link")

Streaming the results of your LLM application is vital for ensuring a good user experience, especially when your graph may call multiple models and take a long time to fully complete a run. Read about how to stream values from your graph in these how to guides:

- [How to stream values](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/)
- [How to stream updates](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_updates/)
- [How to stream messages](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_messages/)
- [How to stream events](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_events/)
- [How to stream in debug mode](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_debug/)
- [How to stream multiple modes](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_multiple/)

### Frontend and Generative UI [¶](https://langchain-ai.github.io/langgraph/how-tos/\#frontend-and-generative-ui "Permanent link")

With LangGraph Platform you can integrate LangGraph agents into your React applications and colocate UI components with your agent code.

- [How to integrate LangGraph into your React application](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/)
- [How to implement Generative User Interfaces with LangGraph](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/)

### Human-in-the-loop [¶](https://langchain-ai.github.io/langgraph/how-tos/\#human-in-the-loop_1 "Permanent link")

When designing complex graphs, relying entirely on the LLM for decision-making can be risky, particularly when it involves tools that interact with files, APIs, or databases. These interactions may lead to unintended data access or modifications, depending on the use case. To mitigate these risks, LangGraph allows you to integrate human-in-the-loop behavior, ensuring your LLM applications operate as intended without undesirable outcomes.

- [How to add a breakpoint](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/)
- [How to wait for user input](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_user_input/)
- [How to edit graph state](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_edit_state/)
- [How to replay and branch from prior states](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/)
- [How to review tool calls](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_review_tool_calls/)

### Double-texting [¶](https://langchain-ai.github.io/langgraph/how-tos/\#double-texting "Permanent link")

Graph execution can take a while, and sometimes users may change their mind about the input they wanted to send before their original input has finished running. For example, a user might notice a typo in their original request and will edit the prompt and resend it. Deciding what to do in these cases is important for ensuring a smooth user experience and preventing your graphs from behaving in unexpected ways.

- [How to use the interrupt option](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/)
- [How to use the rollback option](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/)
- [How to use the reject option](https://langchain-ai.github.io/langgraph/cloud/how-tos/reject_concurrent/)
- [How to use the enqueue option](https://langchain-ai.github.io/langgraph/cloud/how-tos/enqueue_concurrent/)

### Webhooks [¶](https://langchain-ai.github.io/langgraph/how-tos/\#webhooks "Permanent link")

- [How to integrate webhooks](https://langchain-ai.github.io/langgraph/cloud/how-tos/webhooks/)

### Cron Jobs [¶](https://langchain-ai.github.io/langgraph/how-tos/\#cron-jobs "Permanent link")

- [How to create cron jobs](https://langchain-ai.github.io/langgraph/cloud/how-tos/cron_jobs/)

### LangGraph Studio [¶](https://langchain-ai.github.io/langgraph/how-tos/\#langgraph-studio "Permanent link")

LangGraph Studio is a built-in UI for visualizing, testing, and debugging your agents.

- [How to connect to a LangGraph Platform deployment](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_deployment/)
- [How to connect to a local dev server](https://langchain-ai.github.io/langgraph/how-tos/local-studio/)
- [How to connect to a local deployment (Docker)](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/)
- [How to interact with threads in LangGraph Studio](https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/)
- [How to add nodes as dataset examples in LangGraph Studio](https://langchain-ai.github.io/langgraph/cloud/how-tos/datasets_studio/)
- [How to engineer prompts in LangGraph Studio](https://langchain-ai.github.io/langgraph/cloud/how-tos/iterate_graph_studio/)

## Troubleshooting [¶](https://langchain-ai.github.io/langgraph/how-tos/\#troubleshooting "Permanent link")

These are the guides for resolving common errors you may find while building with LangGraph. Errors referenced below will have an `lc_error_code` property corresponding to one of the below codes when they are thrown in code.

- [GRAPH\_RECURSION\_LIMIT](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/)
- [INVALID\_CONCURRENT\_GRAPH\_UPDATE](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/)
- [INVALID\_GRAPH\_NODE\_RETURN\_VALUE](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/)
- [MULTIPLE\_SUBGRAPHS](https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/)
- [INVALID\_CHAT\_HISTORY](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/)

### LangGraph Platform Troubleshooting [¶](https://langchain-ai.github.io/langgraph/how-tos/\#langgraph-platform-troubleshooting "Permanent link")

These guides provide troubleshooting information for errors that are specific to the LangGraph Platform.

- [INVALID\_LICENSE](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/)

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Please help us improve this page by adding to the discussion below.


## Comments

[iframe](https://giscus.app/en/widget?origin=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fhow-tos%2F&session=&theme=preferred_color_scheme&reactionsEnabled=1&emitMetadata=0&inputPosition=bottom&repo=langchain-ai%2Flanggraph&repoId=R_kgDOKFU0lQ&category=Discussions&categoryId=DIC_kwDOKFU0lc4CfZgA&strict=0&description=How+to+accomplish+common+tasks+in+LangGraph&backLink=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fhow-tos%2F&term=langgraph%2Fhow-tos%2F)

Back to top