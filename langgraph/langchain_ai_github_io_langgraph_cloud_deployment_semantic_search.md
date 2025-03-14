[Skip to content](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/#how-to-add-semantic-search-to-your-langgraph-deployment)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/deployment/semantic_search.md "Edit this page")

# How to add semantic search to your LangGraph deployment [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/\#how-to-add-semantic-search-to-your-langgraph-deployment "Permanent link")

This guide explains how to add semantic search to your LangGraph deployment's cross-thread [store](https://langchain-ai.github.io/langgraph/concepts/persistence/#memory-store), so that your agent can search for memories and other documents by semantic similarity.

## Prerequisites [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/\#prerequisites "Permanent link")

- A LangGraph deployment (see [how to deploy](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_pyproject/))
- API keys for your embedding provider (in this case, OpenAI)
- `langchain >= 0.3.8` (if you specify using the string format below)

## Steps [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/\#steps "Permanent link")

1. Update your `langgraph.json` configuration file to include the store configuration:

```md-code__content
{
    ...
    "store": {
        "index": {
            "embed": "openai:text-embedding-3-small",
            "dims": 1536,
            "fields": ["$"]
        }
    }
}

```

This configuration:

- Uses OpenAI's text-embedding-3-small model for generating embeddings
- Sets the embedding dimension to 1536 (matching the model's output)
- Indexes all fields in your stored data ( `["$"]` means index everything, or specify specific fields like `["text", "metadata.title"]`)

- To use the string embedding format above, make sure your dependencies include `langchain >= 0.3.8`:


```md-code__content
# In pyproject.toml
[project]
dependencies = [\
    "langchain>=0.3.8"\
]

```

Or if using requirements.txt:

```md-code__content
langchain>=0.3.8

```

## Usage [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/\#usage "Permanent link")

Once configured, you can use semantic search in your LangGraph nodes. The store requires a namespace tuple to organize memories:

```md-code__content
def search_memory(state: State, *, store: BaseStore):
    # Search the store using semantic similarity
    # The namespace tuple helps organize different types of memories
    # e.g., ("user_facts", "preferences") or ("conversation", "summaries")
    results = store.search(
        namespace=("memory", "facts"),  # Organize memories by type
        query="your search query",
        limit=3  # number of results to return
    )
    return results

```

## Custom Embeddings [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/\#custom-embeddings "Permanent link")

If you want to use custom embeddings, you can pass a path to a custom embedding function:

```md-code__content
{
    ...
    "store": {
        "index": {
            "embed": "path/to/embedding_function.py:embed",
            "dims": 1536,
            "fields": ["$"]
        }
    }
}

```

The deployment will look for the function in the specified path. The function must be async and accept a list of strings:

```md-code__content
# path/to/embedding_function.py
from openai import AsyncOpenAI

client = AsyncOpenAI()

async def aembed_texts(texts: list[str]) -> list[list[float]]:
    """Custom embedding function that must:
    1. Be async
    2. Accept a list of strings
    3. Return a list of float arrays (embeddings)
    """
    response = await client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [e.embedding for e in response.data]

```

## Querying via the API [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/\#querying-via-the-api "Permanent link")

You can also query the store using the LangGraph SDK. Since the SDK uses async operations:

```md-code__content
from langgraph_sdk import get_client

async def search_store():
    client = get_client()
    results = await client.store.search_items(
        ("memory", "facts"),
        query="your search query",
        limit=3  # number of results to return
    )
    return results

# Use in an async context
results = await search_store()

```

## Comments

giscus

#### [0 reactions](https://github.com/langchain-ai/langgraph/discussions/2657)

#### [1 comment](https://github.com/langchain-ai/langgraph/discussions/2657)

#### ·

#### 1 reply

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@WesGBrooks](https://avatars.githubusercontent.com/u/2110932?u=cee9eda6d45b2ffdeb3d970507e2df49fc83c75b&v=4)WesGBrooks](https://github.com/WesGBrooks) [Dec 5, 2024](https://github.com/langchain-ai/langgraph/discussions/2657#discussioncomment-11476739)

This is very cool!! But one question... this seems to point to an advantage for some memories being stored in a structured way (i.e. via Postgres), and potentially others being stored in an unstructured way that enables semantic search -- especially as more memories are stored, where some memories are likely more permanent (i.e. a more concrete, less changable user profile) and some are more ephemeral (i.e. the agent learned you like swiss cheese better than provolone).

Does this mean you'll be adding support for splitting types of long-term memory storage between traditional stores (like in-memory/postgres) and storage methods more suited for embeddings, like vector dbs such as Chroma or Pinecone?

1

👍1

1 reply

[![@hinthornw](https://avatars.githubusercontent.com/u/13333726?u=82ebf1e0eb0663ebd49ba66f67a43f51bbf11442&v=4)](https://github.com/hinthornw)

[hinthornw](https://github.com/hinthornw) [Dec 5, 2024](https://github.com/langchain-ai/langgraph/discussions/2657#discussioncomment-11476878)

Contributor

edited

Good question. I don't view the two as mutually exclusive. The BaseStore lets you pick how you organize information (as namespaces, or can be mostly flat. Each item can be a single string or have more structure and fields), and the you can query using mixtures of filters and semantic search.

For context, the semantic search right now is powered by a vector store (pgvector in the OSS postgres store case). If you wanted to create a store instance that offloaded the search functionality to a dedicated vector DB, elastic, or mix of storage providers, you could do so.

While we don't intend langgraph to become the "integrations" package, there is potentially a world where we have more first-class support for all the langchain vectorstores by default

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fdeployment%2Fsemantic_search%2F)