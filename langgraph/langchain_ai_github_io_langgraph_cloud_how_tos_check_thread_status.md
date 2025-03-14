[Skip to content](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#check-the-status-of-your-threads)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/check_thread_status.md "Edit this page")

# Check the Status of your Threads [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/\#check-the-status-of-your-threads "Permanent link")

## Setup [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/\#setup "Permanent link")

To start, we can setup our client with whatever URL you are hosting your graph from:

### SDK initialization [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/\#sdk-initialization "Permanent link")

First, we need to setup our client so that we can communicate with our hosted graph:

[Python](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_1_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_1_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_1_3)

```md-code__content
from langgraph_sdk import get_client
client = get_client(url=<DEPLOYMENT_URL>)
# Using the graph deployed with the name "agent"
assistant_id = "agent"
thread = await client.threads.create()

```

```md-code__content
import { Client } from "@langchain/langgraph-sdk";

const client = new Client({ apiUrl: <DEPLOYMENT_URL> });
// Using the graph deployed with the name "agent"
const assistantId = "agent";
const thread = await client.threads.create();

```

```md-code__content
curl --request POST \
  --url <DEPLOYMENT_URL>/threads \
  --header 'Content-Type: application/json' \
  --data '{}'

```

## Find idle threads [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/\#find-idle-threads "Permanent link")

We can use the following commands to find threads that are idle, which means that all runs executed on the thread have finished running:

[Python](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_2_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_2_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_2_3)

```md-code__content
print(await client.threads.search(status="idle",limit=1))

```

```md-code__content
console.log(await client.threads.search({ status: "idle", limit: 1 }));

```

```md-code__content
curl --request POST \
--url <DEPLOYMENT_URL>/threads/search \
--header 'Content-Type: application/json' \
--data '{"status": "idle", "limit": 1}'

```

Output:

```
[{'thread_id': 'cacf79bb-4248-4d01-aabc-938dbd60ed2c',\
'created_at': '2024-08-14T17:36:38.921660+00:00',\
'updated_at': '2024-08-14T17:36:38.921660+00:00',\
'metadata': {'graph_id': 'agent'},\
'status': 'idle',\
'config': {'configurable': {}}}]

```

## Find interrupted threads [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/\#find-interrupted-threads "Permanent link")

We can use the following commands to find threads that have been interrupted in the middle of a run, which could either mean an error occurred before the run finished or a human-in-the-loop breakpoint was reached and the run is waiting to continue:

[Python](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_3_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_3_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_3_3)

```md-code__content
print(await client.threads.search(status="interrupted",limit=1))

```

```md-code__content
console.log(await client.threads.search({ status: "interrupted", limit: 1 }));

```

```md-code__content
curl --request POST \
--url <DEPLOYMENT_URL>/threads/search \
--header 'Content-Type: application/json' \
--data '{"status": "interrupted", "limit": 1}'

```

Output:

```
[{'thread_id': '0d282b22-bbd5-4d95-9c61-04dcc2e302a5',\
'created_at': '2024-08-14T17:41:50.235455+00:00',\
'updated_at': '2024-08-14T17:41:50.235455+00:00',\
'metadata': {'graph_id': 'agent'},\
'status': 'interrupted',\
'config': {'configurable': {}}}]

```

## Find busy threads [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/\#find-busy-threads "Permanent link")

We can use the following commands to find threads that are busy, meaning they are currently handling the execution of a run:

[Python](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_4_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_4_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_4_3)

```md-code__content
print(await client.threads.search(status="busy",limit=1))

```

```md-code__content
console.log(await client.threads.search({ status: "busy", limit: 1 }));

```

```md-code__content
curl --request POST \
--url <DEPLOYMENT_URL>/threads/search \
--header 'Content-Type: application/json' \
--data '{"status": "busy", "limit": 1}'

```

Output:

```
[{'thread_id': '0d282b22-bbd5-4d95-9c61-04dcc2e302a5',\
'created_at': '2024-08-14T17:41:50.235455+00:00',\
'updated_at': '2024-08-14T17:41:50.235455+00:00',\
'metadata': {'graph_id': 'agent'},\
'status': 'busy',\
'config': {'configurable': {}}}]

```

## Find specific threads [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/\#find-specific-threads "Permanent link")

You may also want to check the status of specific threads, which you can do in a few ways:

### Find by ID [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/\#find-by-id "Permanent link")

You can use the `get` function to find the status of a specific thread, as long as you have the ID saved

[Python](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_5_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_5_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_5_3)

```md-code__content
print((await client.threads.get(<THREAD_ID>))['status'])

```

```md-code__content
console.log((await client.threads.get(<THREAD_ID>)).status);

```

```md-code__content
curl --request GET \
--url <DEPLOYMENT_URL>/threads/<THREAD_ID> \
--header 'Content-Type: application/json' | jq -r '.status'

```

Output:

```
'idle'

```

### Find by metadata [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/\#find-by-metadata "Permanent link")

The search endpoint for threads also allows you to filter on metadata, which can be helpful if you use metadata to tag threads in order to keep them organized:

[Python](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_6_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_6_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__tabbed_6_3)

```md-code__content
print((await client.threads.search(metadata={"foo":"bar"},limit=1))[0]['status'])

```

```md-code__content
console.log((await client.threads.search({ metadata: { "foo": "bar" }, limit: 1 }))[0].status);

```

```md-code__content
curl --request POST \
--url <DEPLOYMENT_URL>/threads/search \
--header 'Content-Type: application/json' \
--data '{"metadata": {"foo":"bar"}, "limit": 1}' | jq -r '.[0].status'

```

Output:

```
'idle'

```

## Comments

giscus

#### 0 reactions

#### 0 comments

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fhow-tos%2Fcheck_thread_status%2F)