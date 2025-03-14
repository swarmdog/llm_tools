[Skip to content](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/#stateless-runs)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/stateless_runs.md "Edit this page")

# Stateless Runs [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/\#stateless-runs "Permanent link")

Most of the time, you provide a `thread_id` to your client when you run your graph in order to keep track of prior runs through the persistent state implemented in LangGraph Cloud. However, if you don't need to persist the runs you don't need to use the built in persistent state and can create stateless runs.

## Setup [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/\#setup "Permanent link")

First, let's setup our client:

[Python](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/#__tabbed_1_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/#__tabbed_1_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/#__tabbed_1_3)

```md-code__content
from langgraph_sdk import get_client

client = get_client(url=<DEPLOYMENT_URL>)
# Using the graph deployed with the name "agent"
assistant_id = "agent"
# create thread
thread = await client.threads.create()

```

```md-code__content
import { Client } from "@langchain/langgraph-sdk";

const client = new Client({ apiUrl: <DEPLOYMENT_URL> });
// Using the graph deployed with the name "agent"
const assistantId = "agent";
// create thread
const thread = await client.threads.create();

```

```md-code__content
curl --request POST \
    --url <DEPLOYMENT_URL>/assistants/search \
    --header 'Content-Type: application/json' \
    --data '{
        "limit": 10,
        "offset": 0
    }' | jq -c 'map(select(.config == null or .config == {})) | .[0].graph_id' && \
curl --request POST \
    --url <DEPLOYMENT_URL>/threads \
    --header 'Content-Type: application/json' \
    --data '{}'

```

## Stateless streaming [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/\#stateless-streaming "Permanent link")

We can stream the results of a stateless run in an almost identical fashion to how we stream from a run with the state attribute, but instead of passing a value to the `thread_id` parameter, we pass `None`:

[Python](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/#__tabbed_2_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/#__tabbed_2_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/#__tabbed_2_3)

```md-code__content
input = {
    "messages": [\
        {"role": "user", "content": "Hello! My name is Bagatur and I am 26 years old."}\
    ]
}

async for chunk in client.runs.stream(
    # Don't pass in a thread_id and the stream will be stateless
    None,
    assistant_id,
    input=input,
    stream_mode="updates",
):
    if chunk.data and "run_id" not in chunk.data:
        print(chunk.data)

```

```md-code__content
let input = {
  messages: [\
    { role: "user", content: "Hello! My name is Bagatur and I am 26 years old." }\
  ]
};

const streamResponse = client.runs.stream(
  // Don't pass in a thread_id and the stream will be stateless
  null,
  assistantId,
  {
    input,
    streamMode: "updates"
  }
);
for await (const chunk of streamResponse) {
  if (chunk.data && !("run_id" in chunk.data)) {
    console.log(chunk.data);
  }
}

```

```md-code__content
curl --request POST \
    --url <DEPLOYMENT_URL>/runs/stream \
    --header 'Content-Type: application/json' \
    --data "{
        \"assistant_id\": \"agent\",
        \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"Hello! My name is Bagatur and I am 26 years old.\"}]},
        \"stream_mode\": [\
            \"updates\"\
        ]
    }" | jq -c 'select(.data and (.data | has("run_id") | not)) | .data'

```

Output:

```
{'agent': {'messages': [{'content': "Hello Bagatur! It's nice to meet you. Thank you for introducing yourself and sharing your age. Is there anything specific you'd like to know or discuss? I'm here to help with any questions or topics you're interested in.", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-489ec573-1645-4ce2-a3b8-91b391d50a71', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}

```

## Waiting for stateless results [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/\#waiting-for-stateless-results "Permanent link")

In addition to streaming, you can also wait for a stateless result by using the `.wait` function like follows:

[Python](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/#__tabbed_3_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/#__tabbed_3_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/#__tabbed_3_3)

```md-code__content
stateless_run_result = await client.runs.wait(
    None,
    assistant_id,
    input=input,
)
print(stateless_run_result)

```

```md-code__content
let statelessRunResult = await client.runs.wait(
  null,
  assistantId,
  { input: input }
);
console.log(statelessRunResult);

```

```md-code__content
curl --request POST \
    --url <DEPLOYMENT_URL>/runs/wait \
    --header 'Content-Type: application/json' \
    --data '{
        "assistant_id": <ASSISTANT_IDD>,
    }'

```

Output:

```
{
    'messages': [\
        {\
            'content': 'Hello! My name is Bagatur and I am 26 years old.',\
            'additional_kwargs': {},\
            'response_metadata': {},\
            'type': 'human',\
            'name': None,\
            'id': '5e088543-62c2-43de-9d95-6086ad7f8b48',\
            'example': False}\
        ,\
        {\
            'content': "Hello Bagatur! It's nice to meet you. Thank you for introducing yourself and sharing your age. Is there anything specific you'd like to know or discuss? I'm here to help with any questions or topics you'd like to explore.",\
            'additional_kwargs': {},\
            'response_metadata': {},\
            'type': 'ai',\
            'name': None,\
            'id': 'run-d6361e8d-4d4c-45bd-ba47-39520257f773',\
            'example': False,\
            'tool_calls': [],\
            'invalid_tool_calls': [],\
            'usage_metadata': None\
        }\
    ]
}

```

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Please help us improve this page by adding to the discussion below.


## Comments

[iframe](https://giscus.app/en/widget?origin=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fhow-tos%2Fstateless_runs%2F&session=&theme=preferred_color_scheme&reactionsEnabled=1&emitMetadata=0&inputPosition=bottom&repo=langchain-ai%2Flanggraph&repoId=R_kgDOKFU0lQ&category=Discussions&categoryId=DIC_kwDOKFU0lc4CfZgA&strict=0&description=Build+language+agents+as+graphs&backLink=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fhow-tos%2Fstateless_runs%2F&term=langgraph%2Fcloud%2Fhow-tos%2Fstateless_runs%2F)

Back to top