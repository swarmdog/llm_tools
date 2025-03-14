[Skip to content](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#how-to-test-a-langgraph-app-locally)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/deployment/test_locally.md "Edit this page")

# How to test a LangGraph app locally [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/\#how-to-test-a-langgraph-app-locally "Permanent link")

This guide assumes you have a LangGraph app correctly set up with a proper configuration file and a corresponding compiled graph, and that you have a proper LangChain API key.

Testing locally ensures that there are no errors or conflicts with Python dependencies and confirms that the configuration file is specified correctly.

## Setup [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/\#setup "Permanent link")

Install the LangGraph CLI package:

```md-code__content
pip install -U "langgraph-cli[inmem]"

```

Ensure you have an API key, which you can create from the [LangSmith UI](https://smith.langchain.com/) (Settings > API Keys). This is required to authenticate that you have LangGraph Cloud access. After you have saved the key to a safe place, place the following line in your `.env` file:

```md-code__content
LANGSMITH_API_KEY = *********

```

## Start the API server [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/\#start-the-api-server "Permanent link")

Once you have installed the CLI, you can run the following command to start the API server for local testing:

```md-code__content
langgraph dev

```

This will start up the LangGraph API server locally. If this runs successfully, you should see something like:

> Ready!
>
> - API: [http://localhost:2024](http://localhost:2024/)
>
> - Docs: [http://localhost:2024/docs](http://localhost:2024/docs)
>
> - LangGraph Studio Web UI: [https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024](https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024)

In-Memory Mode

The `langgraph dev` command starts LangGraph Server in an in-memory mode. This mode is suitable for development and testing purposes. For production use, you should deploy LangGraph Server with access to a persistent storage backend.

If you want to test your application with a persistent storage backend, you can use the `langgraph up` command instead of `langgraph dev`. You will
need to have `docker` installed on your machine to use this command.

### Interact with the server [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/\#interact-with-the-server "Permanent link")

We can now interact with the API server using the LangGraph SDK. First, we need to start our client, select our assistant (in this case a graph we called "agent", make sure to select the proper assistant you wish to test).

You can either initialize by passing authentication or by setting an environment variable.

#### Initialize with authentication [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/\#initialize-with-authentication "Permanent link")

[Python](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__tabbed_1_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__tabbed_1_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__tabbed_1_3)

```md-code__content
from langgraph_sdk import get_client

# only pass the url argument to get_client() if you changed the default port when calling langgraph dev
client = get_client(url=<DEPLOYMENT_URL>,api_key=<LANGSMITH_API_KEY>)
# Using the graph deployed with the name "agent"
assistant_id = "agent"
thread = await client.threads.create()

```

```md-code__content
import { Client } from "@langchain/langgraph-sdk";

// only set the apiUrl if you changed the default port when calling langgraph dev
const client = new Client({ apiUrl: <DEPLOYMENT_URL>, apiKey: <LANGSMITH_API_KEY> });
// Using the graph deployed with the name "agent"
const assistantId = "agent";
const thread = await client.threads.create();

```

```md-code__content
curl --request POST \
  --url <DEPLOYMENT_URL>/threads \
  --header 'Content-Type: application/json'
  --header 'x-api-key: <LANGSMITH_API_KEY>'

```

#### Initialize with environment variables [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/\#initialize-with-environment-variables "Permanent link")

If you have a `LANGSMITH_API_KEY` set in your environment, you do not need to explicitly pass authentication to the client

[Python](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__tabbed_2_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__tabbed_2_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__tabbed_2_3)

```md-code__content
from langgraph_sdk import get_client

# only pass the url argument to get_client() if you changed the default port when calling langgraph dev
client = get_client()
# Using the graph deployed with the name "agent"
assistant_id = "agent"
thread = await client.threads.create()

```

```md-code__content
import { Client } from "@langchain/langgraph-sdk";

// only set the apiUrl if you changed the default port when calling langgraph dev
const client = new Client();
// Using the graph deployed with the name "agent"
const assistantId = "agent";
const thread = await client.threads.create();

```

```md-code__content
curl --request POST \
  --url <DEPLOYMENT_URL>/threads \
  --header 'Content-Type: application/json'

```

Now we can invoke our graph to ensure it is working. Make sure to change the input to match the proper schema for your graph.

[Python](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__tabbed_3_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__tabbed_3_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__tabbed_3_3)

```md-code__content
input = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
async for chunk in client.runs.stream(
    thread["thread_id"],
    assistant_id,
    input=input,
    stream_mode="updates",
):
    print(f"Receiving new event of type: {chunk.event}...")
    print(chunk.data)
    print("\n\n")

```

```md-code__content
const input = { "messages": [{ "role": "user", "content": "what's the weather in sf"}] }

const streamResponse = client.runs.stream(
  thread["thread_id"],
  assistantId,
  {
    input: input,
    streamMode: "updates",
  }
);
for await (const chunk of streamResponse) {
  console.log(`Receiving new event of type: ${chunk.event}...`);
  console.log(chunk.data);
  console.log("\n\n");
}

```

```md-code__content
curl --request POST \
 --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream \
 --header 'Content-Type: application/json' \
 --data "{
   \"assistant_id\": \"agent\",
   \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what's the weather in sf\"}]},
   \"stream_mode\": [\
     \"events\"\
   ]
 }" | \
 sed 's/\r$//' | \
 awk '
 /^event:/ {
     if (data_content != "") {
         print data_content "\n"
     }
     sub(/^event: /, "Receiving event of type: ", $0)
     printf "%s...\n", $0
     data_content = ""
 }
 /^data:/ {
     sub(/^data: /, "", $0)
     data_content = $0
 }
 END {
     if (data_content != "") {
         print data_content "\n"
     }
 }
 '

```

If your graph works correctly, you should see your graph output displayed in the console. Of course, there are many more ways you might need to test your graph, for a full list of commands you can send with the SDK, see the [Python](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/) and [JS/TS](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/) references.

## Comments

giscus

#### 0 reactions

#### 0 comments

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fdeployment%2Ftest_locally%2F)