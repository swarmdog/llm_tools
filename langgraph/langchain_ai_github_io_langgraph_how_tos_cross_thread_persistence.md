[Skip to content](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#how-to-add-cross-thread-persistence-to-your-graph)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/cross-thread-persistence.ipynb "Edit this page")

# How to add cross-thread persistence to your graph [¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/\#how-to-add-cross-thread-persistence-to-your-graph "Permanent link")

Prerequisites

This guide assumes familiarity with the following:


- [Persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/)
- [Memory](https://langchain-ai.github.io/langgraph/concepts/memory/)
- [Chat Models](https://python.langchain.com/docs/concepts/#chat-models/)

In the [previous guide](https://langchain-ai.github.io/langgraph/how-tos/persistence/) you learned how to persist graph state across multiple interactions on a single [thread](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/). LangGraph also allows you to persist data across **multiple threads**. For instance, you can store information about users (their names or preferences) in a shared memory and reuse them in the new conversational threads.

In this guide, we will show how to construct and use a graph that has a shared memory implemented using the [Store](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) interface.

Note

Support for the `Store` API that is used in this guide was added in LangGraph `v0.2.32`.


Support for **index** and **query** arguments of the `Store` API that is used in this guide was added in LangGraph `v0.2.54`.


## Setup [¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/\#setup "Permanent link")

First, let's install the required packages and set our API keys

```md-code__content
%%capture --no-stderr
%pip install -U langchain_openai langgraph

```

```md-code__content
import getpass
import os

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("ANTHROPIC_API_KEY")
_set_env("OPENAI_API_KEY")

```

Set up [LangSmith](https://smith.langchain.com/) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com/)

## Define store [¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/\#define-store "Permanent link")

In this example we will create a graph that will be able to retrieve information about a user's preferences. We will do so by defining an `InMemoryStore` \- an object that can store data in memory and query that data. We will then pass the store object when compiling the graph. This allows each node in the graph to access the store: when you define node functions, you can define `store` keyword argument, and LangGraph will automatically pass the store object you compiled the graph with.

When storing objects using the `Store` interface you define two things:

- the namespace for the object, a tuple (similar to directories)
- the object key (similar to filenames)

In our example, we'll be using `("memories", <user_id>)` as namespace and random UUID as key for each new memory.

Importantly, to determine the user, we will be passing `user_id` via the config keyword argument of the node function.

Let's first define an `InMemoryStore` already populated with some memories about the users.

```md-code__content
from langgraph.store.memory import InMemoryStore
from langchain_openai import OpenAIEmbeddings

in_memory_store = InMemoryStore(
    index={
        "embed": OpenAIEmbeddings(model="text-embedding-3-small"),
        "dims": 1536,
    }
)

```

API Reference: [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html)

## Create graph [¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/\#create-graph "Permanent link")

```md-code__content
import uuid
from typing import Annotated
from typing_extensions import TypedDict

from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.checkpoint.memory import MemorySaver
from langgraph.store.base import BaseStore

model = ChatAnthropic(model="claude-3-5-sonnet-20240620")

# NOTE: we're passing the Store param to the node --
# this is the Store we compile the graph with
def call_model(state: MessagesState, config: RunnableConfig, *, store: BaseStore):
    user_id = config["configurable"]["user_id"]
    namespace = ("memories", user_id)
    memories = store.search(namespace, query=str(state["messages"][-1].content))
    info = "\n".join([d.value["data"] for d in memories])
    system_msg = f"You are a helpful assistant talking to the user. User info: {info}"

    # Store new memories if the user asks the model to remember
    last_message = state["messages"][-1]
    if "remember" in last_message.content.lower():
        memory = "User name is Bob"
        store.put(namespace, str(uuid.uuid4()), {"data": memory})

    response = model.invoke(
        [{"role": "system", "content": system_msg}] + state["messages"]
    )
    return {"messages": response}

builder = StateGraph(MessagesState)
builder.add_node("call_model", call_model)
builder.add_edge(START, "call_model")

# NOTE: we're passing the store object here when compiling the graph
graph = builder.compile(checkpointer=MemorySaver(), store=in_memory_store)
# If you're using LangGraph Cloud or LangGraph Studio, you don't need to pass the store or checkpointer when compiling the graph, since it's done automatically.

```

API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) \| [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html) \| [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) \| [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) \| [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

Note

If you're using LangGraph Cloud or LangGraph Studio, you **don't need** to pass store when compiling the graph, since it's done automatically.


## Run the graph! [¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/\#run-the-graph "Permanent link")

Now let's specify a user ID in the config and tell the model our name:

```md-code__content
config = {"configurable": {"thread_id": "1", "user_id": "1"}}
input_message = {"role": "user", "content": "Hi! Remember: my name is Bob"}
for chunk in graph.stream({"messages": [input_message]}, config, stream_mode="values"):
    chunk["messages"][-1].pretty_print()

```

```md-code__content
================================[1m Human Message [0m=================================\
\
Hi! Remember: my name is Bob\
==================================[1m Ai Message [0m==================================\
\
Hello Bob! It's nice to meet you. I'll remember that your name is Bob. How can I assist you today?\
\
```\
\
```md-code__content\
config = {"configurable": {"thread_id": "2", "user_id": "1"}}\
input_message = {"role": "user", "content": "what is my name?"}\
for chunk in graph.stream({"messages": [input_message]}, config, stream_mode="values"):\
    chunk["messages"][-1].pretty_print()\
\
```\
\
```md-code__content\
================================[1m Human Message [0m=================================\
\
what is my name?\
==================================[1m Ai Message [0m==================================\
\
Your name is Bob.\
\
```\
\
We can now inspect our in-memory store and verify that we have in fact saved the memories for the user:\
\
```md-code__content\
for memory in in_memory_store.search(("memories", "1")):\
    print(memory.value)\
\
```\
\
```md-code__content\
{'data': 'User name is Bob'}\
\
```\
\
Let's now run the graph for another user to verify that the memories about the first user are self contained:\
\
```md-code__content\
config = {"configurable": {"thread_id": "3", "user_id": "2"}}\
input_message = {"role": "user", "content": "what is my name?"}\
for chunk in graph.stream({"messages": [input_message]}, config, stream_mode="values"):\
    chunk["messages"][-1].pretty_print()\
\
```\
\
```md-code__content\
================================[1m Human Message [0m=================================\
\
what is my name?\
==================================[1m Ai Message [0m==================================\
\
I apologize, but I don't have any information about your name. As an AI assistant, I don't have access to personal information about users unless it has been specifically shared in our conversation. If you'd like, you can tell me your name and I'll be happy to use it in our discussion.\
\
```\
\
## Comments\
\
giscus\
\
#### [4 reactions](https://github.com/langchain-ai/langgraph/discussions/2086)\
\
👍1❤️3\
\
#### [7 comments](https://github.com/langchain-ai/langgraph/discussions/2086)\
\
#### ·\
\
#### 5 replies\
\
_– powered by [giscus](https://giscus.app/)_\
\
- Oldest\
- Newest\
\
[![@ITSAIDI](https://avatars.githubusercontent.com/u/131054654?u=441b938293329ce10372967ab9718edc1c5548b2&v=4)ITSAIDI](https://github.com/ITSAIDI) [Oct 11, 2024](https://github.com/langchain-ai/langgraph/discussions/2086#discussioncomment-10918858)\
\
It's better if we can store this Memory in such as local file. I use a .py file and with this code, every time i run the .py the memory gets initialized so I lost the information stored in previous runs !\
\
1\
\
1 reply\
\
[![@Denis-root](https://avatars.githubusercontent.com/u/64244017?v=4)](https://github.com/Denis-root)\
\
[Denis-root](https://github.com/Denis-root) [11 days ago](https://github.com/langchain-ai/langgraph/discussions/2086#discussioncomment-12363359)\
\
Te entiendo, solo para agregar al parecer estos ejemplos son pruebas de concepto y creo que su uso son como para entornos de jupyter Notebook o Google collabs\
\
[![@cividanieltorres](https://avatars.githubusercontent.com/u/177919571?u=2ced288569411ea9c695bcd078af0053c2b4233b&v=4)cividanieltorres](https://github.com/cividanieltorres) [Oct 13, 2024](https://github.com/langchain-ai/langgraph/discussions/2086#discussioncomment-10927930)\
\
Hello,\
\
I think you are getting this behaviour because the memory store used here is InMemoryStore. This means that every time you rerun, the memory would initiate from scratch, losing all previous information. If you want to have real persistence, I believe the appropriate way of implementing this right now would be with PostgresStore. This would allow you to setup a Postgres where you could connect every time you rerun your graph.\
\
Remember these are just examples for testing purposes, not for production environments.\
\
Hope this helps.\
\
1\
\
👍3\
\
1 reply\
\
[![@hinthornw](https://avatars.githubusercontent.com/u/13333726?u=82ebf1e0eb0663ebd49ba66f67a43f51bbf11442&v=4)](https://github.com/hinthornw)\
\
[hinthornw](https://github.com/hinthornw) [Dec 5, 2024](https://github.com/langchain-ai/langgraph/discussions/2086#discussioncomment-11478501)\
\
Contributor\
\
Yupp! As the name suggests, this is "in memory" - desigend to be run ephemerally in a single session. For prod use cases we recommend one of hte other stores (such as the postgres one)\
\
If you want to add some light persistence to it:\
\
```\
from collections import defaultdict\
from typing import Any, Optional, Dict, Tuple\
from langgraph.checkpoint.memory import PersistentDict\
from langgraph.store.memory import InMemoryStore\
\
class PersistentMemoryStore:\
    def __init__(\
        self,\
        data_file: str = "store_data.pkl",\
        vector_file: str = "store_vectors.pkl",\
        index: Optional[Dict[str, Any]] = None\
    ) -> None:\
        # Create the underlying InMemoryStore for operations\
        self.store = InMemoryStore(index=index)\
\
        # Create persistent dictionaries for data and vectors\
        self.data_dict = PersistentDict(filename=data_file)\
        self.vector_dict = PersistentDict(filename=vector_file)\
\
        # Load existing data if available\
        self._load_persistent_data()\
\
        # Replace store's in-memory dicts with our persistent ones\
        self.store._data = self.data_dict\
        self.store._vectors = self.vector_dict\
\
    def _load_persistent_data(self) -> None:\
        """Load data from persistent storage files"""\
        for container, name in [(self.data_dict, "data"), (self.vector_dict, "vectors")]:\
            try:\
                container.load()\
            except FileNotFoundError:\
                # It's okay if file doesn't exist yet\
                pass\
            except (EOFError, ValueError) as e:\
                raise RuntimeError(\
                    f"Failed to load store {name} from {container.filename}. "\
                    "This may be due to changes in the stored data structure."\
                ) from e\
            except Exception as e:\
                raise RuntimeError(\
                    f"Unexpected error loading store {name} from {container.filename}: {str(e)}"\
                ) from e\
\
    def __enter__(self):\
        return self.store\
\
    def __exit__(self, exc_type, exc_val, exc_tb):\
        self.close()\
\
    def close(self) -> None:\
        """Close and sync the persistent dictionaries"""\
        self.data_dict.close()\
        self.vector_dict.close()\
```\
\
```\
# Create a persistent store that automatically handles file I/O\
with PersistentMemoryStore(\
    data_file="my_store_data.pkl",\
    vector_file="my_store_vectors.pkl"\
) as store:\
    # Use the store as a regular InMemoryStore\
    store.put(("users",), "user1", {"name": "Alice"})\
    store.put(("users",), "user2", {"name": "Bob"})\
\
    # Data will be automatically saved when the context exits\
```\
\
👍2\
\
[![@ITSAIDI](https://avatars.githubusercontent.com/u/131054654?u=441b938293329ce10372967ab9718edc1c5548b2&v=4)ITSAIDI](https://github.com/ITSAIDI) [Oct 13, 2024](https://github.com/langchain-ai/langgraph/discussions/2086#discussioncomment-10928084)\
\
Thanks [@cividanieltorres](https://github.com/cividanieltorres) , is There Any Tuto to use PostgresStore with LangGraph ?\
\
1\
\
👍1\
\
1 reply\
\
[![@RollsChris](https://avatars.githubusercontent.com/u/6059035?u=77d34db2b6e695402704cc1cb8ea3022467d444d&v=4)](https://github.com/RollsChris)\
\
[RollsChris](https://github.com/RollsChris) [Oct 15, 2024](https://github.com/langchain-ai/langgraph/discussions/2086#discussioncomment-10948958)\
\
[https://langchain-ai.github.io/langgraph/how-tos/persistence\_postgres/](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/)\
\
❤️3\
\
[![@lakshaytalkstomachines](https://avatars.githubusercontent.com/u/38259381?u=c32bd533ee3f00d899ec906c6878f3a5a4fd91d5&v=4)lakshaytalkstomachines](https://github.com/lakshaytalkstomachines) [Nov 5, 2024](https://github.com/langchain-ai/langgraph/discussions/2086#discussioncomment-11159953)\
\
Why Can't this be just a node in graph that queries the db and loads the user data into State?\
\
2\
\
1 reply\
\
[![@hinthornw](https://avatars.githubusercontent.com/u/13333726?u=82ebf1e0eb0663ebd49ba66f67a43f51bbf11442&v=4)](https://github.com/hinthornw)\
\
[hinthornw](https://github.com/hinthornw) [Dec 5, 2024](https://github.com/langchain-ai/langgraph/discussions/2086#discussioncomment-11478512)\
\
Contributor\
\
Are you asking why this is in the same node as the llm vs. in two nodes?\
\
Your suggestion also works, we just didn't see the need to create a separate node for a how-to\
\
[![@KartikeyShaurya36](https://avatars.githubusercontent.com/u/175841267?v=4)KartikeyShaurya36](https://github.com/KartikeyShaurya36) [Nov 27, 2024](https://github.com/langchain-ai/langgraph/discussions/2086#discussioncomment-11391356)\
\
hi everyone , do anybody know how to clear the history of a thread\
\
1\
\
1 reply\
\
[![@edisonwd](https://avatars.githubusercontent.com/u/25941671?v=4)](https://github.com/edisonwd)\
\
[edisonwd](https://github.com/edisonwd) [Dec 5, 2024](https://github.com/langchain-ai/langgraph/discussions/2086#discussioncomment-11469389)\
\
[https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/)\
\
[![@himaniMaxHive](https://avatars.githubusercontent.com/u/172501999?v=4)himaniMaxHive](https://github.com/himaniMaxHive) [Jan 3](https://github.com/langchain-ai/langgraph/discussions/2086#discussioncomment-11724505)\
\
If there is any example, using PostgresStore, it will be very helpful.\
\
1\
\
👍1\
\
0 replies\
\
[![@siddg97](https://avatars.githubusercontent.com/u/39356356?u=cc942c17635b7846155ba1b8d28bbcbf79d3fd61&v=4)siddg97](https://github.com/siddg97) [Jan 5](https://github.com/langchain-ai/langgraph/discussions/2086#discussioncomment-11741316)\
\
Is there a store with some other DB than Postgres? E.g. MongoDB, DynamoDB etc.\
\
1\
\
👍3\
\
0 replies\
\
WritePreview\
\
[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")\
\
[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fhow-tos%2Fcross-thread-persistence%2F)