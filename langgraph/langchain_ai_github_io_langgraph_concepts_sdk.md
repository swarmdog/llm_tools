[Skip to content](https://langchain-ai.github.io/langgraph/concepts/sdk/#langgraph-sdk)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/sdk.md "Edit this page")

# LangGraph SDK [¶](https://langchain-ai.github.io/langgraph/concepts/sdk/\#langgraph-sdk "Permanent link")

Prerequisites

- [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
- [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)

The LangGraph Platform provides both a Python and JS SDK for interacting with the [LangGraph Server API](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/).

## Installation [¶](https://langchain-ai.github.io/langgraph/concepts/sdk/\#installation "Permanent link")

You can install the packages using the appropriate package manager for your language.

[Python](https://langchain-ai.github.io/langgraph/concepts/sdk/#__tabbed_1_1)[JS](https://langchain-ai.github.io/langgraph/concepts/sdk/#__tabbed_1_2)

```md-code__content
pip install langgraph-sdk

```

```md-code__content
yarn add @langchain/langgraph-sdk

```

## API Reference [¶](https://langchain-ai.github.io/langgraph/concepts/sdk/\#api-reference "Permanent link")

You can find the API reference for the SDKs here:

- [Python SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/)
- [JS/TS SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)

## Python Sync vs. Async [¶](https://langchain-ai.github.io/langgraph/concepts/sdk/\#python-sync-vs-async "Permanent link")

The Python SDK provides both synchronous ( `get_sync_client`) and asynchronous ( `get_client`) clients for interacting with the LangGraph Server API.

[Async](https://langchain-ai.github.io/langgraph/concepts/sdk/#__tabbed_2_1)[Sync](https://langchain-ai.github.io/langgraph/concepts/sdk/#__tabbed_2_2)

```md-code__content
from langgraph_sdk import get_client

client = get_client(url=..., api_key=...)
await client.assistants.search()

```

```md-code__content
from langgraph_sdk import get_sync_client

client = get_sync_client(url=..., api_key=...)
client.assistants.search()

```

## Related [¶](https://langchain-ai.github.io/langgraph/concepts/sdk/\#related "Permanent link")

- [LangGraph CLI API Reference](https://langchain-ai.github.io/langgraph/cloud/reference/cli/)
- [Python SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/)
- [JS/TS SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)

## Comments

giscus

#### 0 reactions

#### 0 comments

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fconcepts%2Fsdk%2F)