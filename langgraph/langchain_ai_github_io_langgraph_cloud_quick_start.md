[Skip to content](https://langchain-ai.github.io/langgraph/cloud/quick_start/#quickstart-deploy-on-langgraph-cloud)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/quick_start.md "Edit this page")

# Quickstart: Deploy on LangGraph Cloud [¶](https://langchain-ai.github.io/langgraph/cloud/quick_start/\#quickstart-deploy-on-langgraph-cloud "Permanent link")

Prerequisites

Before you begin, ensure you have the following:

- [GitHub account](https://github.com/)
- [LangSmith account](https://smith.langchain.com/)

## Create a repository on GitHub [¶](https://langchain-ai.github.io/langgraph/cloud/quick_start/\#create-a-repository-on-github "Permanent link")

To deploy a LangGraph application to **LangGraph Cloud**, your application code must reside in a GitHub repository. Both public and private repositories are supported.

You can deploy any [LangGraph Application](https://langchain-ai.github.io/langgraph/concepts/application_structure/) to LangGraph Cloud.

For this guide, we'll use the pre-built Python [**ReAct Agent**](https://github.com/langchain-ai/react-agent) template.

Get Required API Keys for the ReAct Agent template

This **ReAct Agent** application requires an API key from [Anthropic](https://console.anthropic.com/) and [Tavily](https://app.tavily.com/). You can get these API keys by signing up on their respective websites.

**Alternative**: If you'd prefer a scaffold application that doesn't require API keys, use the [**New LangGraph Project**](https://github.com/langchain-ai/new-langgraph-project) template instead of the **ReAct Agent** template.

1. Go to the [ReAct Agent](https://github.com/langchain-ai/react-agent) repository.
2. Fork the repository to your GitHub account by clicking the `Fork` button in the top right corner.

## Deploy to LangGraph Cloud [¶](https://langchain-ai.github.io/langgraph/cloud/quick_start/\#deploy-to-langgraph-cloud "Permanent link")

1\. Log in to [LangSmith](https://smith.langchain.com/)

[![Login to LangSmith](https://langchain-ai.github.io/langgraph/cloud/deployment/img/01_login.png)](https://langchain-ai.github.io/langgraph/cloud/deployment/img/01_login.png)
Go to [LangSmith](https://smith.langchain.com/) and log in. If you don't have an account, you can sign up for free.

2\. Click on _LangGraph Platform_ (the left sidebar)

[![Login to LangSmith](https://langchain-ai.github.io/langgraph/cloud/deployment/img/02_langgraph_platform.png)](https://langchain-ai.github.io/langgraph/cloud/deployment/img/02_langgraph_platform.png)
Select **LangGraph Platform** from the left sidebar.

3\. Click on + New Deployment (top right corner)

[![Login to LangSmith](https://langchain-ai.github.io/langgraph/cloud/deployment/img/03_deployments_page.png)](https://langchain-ai.github.io/langgraph/cloud/deployment/img/03_deployments_page.png)
Click on **\+ New Deployment** to create a new deployment. This button is located in the top right corner.
It'll open a new modal where you can fill out the required fields.

4\. Click on Import from GitHub (first time users)

[![image](https://langchain-ai.github.io/langgraph/cloud/deployment/img/04_create_new_deployment.png)](https://langchain-ai.github.io/langgraph/cloud/deployment/img/04_create_new_deployment.png)
Click on **Import from GitHub** and follow the instructions to connect your GitHub account. This step is needed for **first-time users** or to add private repositories that haven't been connected before.

5\. Select the repository, configure ENV vars etc

[![image](https://langchain-ai.github.io/langgraph/cloud/deployment/img/05_configure_deployment.png)](https://langchain-ai.github.io/langgraph/cloud/deployment/img/05_configure_deployment.png)
Select the **repository**, add env variables and secrets, and set other configuration options.

- **Repository**: Select the repository you forked earlier (or any other repository you want to deploy).
- Set the secrets and environment variables required by your application. For the **ReAct Agent** template, you need to set the following secrets:
  - **ANTHROPIC\_API\_KEY**: Get an API key from [Anthropic](https://console.anthropic.com/).
  - **TAVILY\_API\_KEY**: Get an API key on the [Tavily website](https://app.tavily.com/).

6\. Click Submit to Deploy!

[![image](https://langchain-ai.github.io/langgraph/cloud/deployment/img/05_configure_deployment.png)](https://langchain-ai.github.io/langgraph/cloud/deployment/img/05_configure_deployment.png)
Please note that this step may ~15 minutes to complete. You can check the status of your deployment in the **Deployments** view.
Click the **Submit** button at the top right corner to deploy your application.

## LangGraph Studio Web UI [¶](https://langchain-ai.github.io/langgraph/cloud/quick_start/\#langgraph-studio-web-ui "Permanent link")

Once your application is deployed, you can test it in **LangGraph Studio**.

1\. Click on an existing deployment

[![image](https://langchain-ai.github.io/langgraph/cloud/deployment/img/07_deployments_page.png)](https://langchain-ai.github.io/langgraph/cloud/deployment/img/07_deployments_page.png)
Click on the deployment you just created to view more details.

2\. Click on LangGraph Studio

[![image](https://langchain-ai.github.io/langgraph/cloud/deployment/img/08_deployment_view.png)](https://langchain-ai.github.io/langgraph/cloud/deployment/img/08_deployment_view.png)
Click on the **LangGraph Studio** button to open LangGraph Studio.

[![image](https://langchain-ai.github.io/langgraph/cloud/deployment/img/09_langgraph_studio.png)](https://langchain-ai.github.io/langgraph/cloud/deployment/img/09_langgraph_studio.png)

Sample graph run in LangGraph Studio.

## Test the API [¶](https://langchain-ai.github.io/langgraph/cloud/quick_start/\#test-the-api "Permanent link")

Note

The API calls below are for the **ReAct Agent** template. If you're deploying a different application, you may need to adjust the API calls accordingly.

Before using, you need to get the `URL` of your LangGraph deployment. You can find this in the `Deployment` view. Click the `URL` to copy it to the clipboard.

You also need to make sure you have set up your API key properly, so you can authenticate with LangGraph Cloud.

```md-code__content
export LANGSMITH_API_KEY=...

```

[Python SDK (Async)](https://langchain-ai.github.io/langgraph/cloud/quick_start/#__tabbed_1_1)[Python SDK (Sync)](https://langchain-ai.github.io/langgraph/cloud/quick_start/#__tabbed_1_2)[Javascript SDK](https://langchain-ai.github.io/langgraph/cloud/quick_start/#__tabbed_1_3)[Rest API](https://langchain-ai.github.io/langgraph/cloud/quick_start/#__tabbed_1_4)

**Install the LangGraph Python SDK**

```md-code__content
pip install langgraph-sdk

```

**Send a message to the assistant (threadless run)**

```md-code__content
from langgraph_sdk import get_client

client = get_client(url="your-deployment-url", api_key="your-langsmith-api-key")

async for chunk in client.runs.stream(
    None,  # Threadless run
    "agent", # Name of assistant. Defined in langgraph.json.
    input={
        "messages": [{\
            "role": "human",\
            "content": "What is LangGraph?",\
        }],
    },
    stream_mode="updates",
):
    print(f"Receiving new event of type: {chunk.event}...")
    print(chunk.data)
    print("\n\n")

```

**Install the LangGraph Python SDK**

```md-code__content
pip install langgraph-sdk

```

**Send a message to the assistant (threadless run)**

```md-code__content
from langgraph_sdk import get_sync_client

client = get_sync_client(url="your-deployment-url", api_key="your-langsmith-api-key")

for chunk in client.runs.stream(
    None,  # Threadless run
    "agent", # Name of assistant. Defined in langgraph.json.
    input={
        "messages": [{\
            "role": "human",\
            "content": "What is LangGraph?",\
        }],
    },
    stream_mode="updates",
):
    print(f"Receiving new event of type: {chunk.event}...")
    print(chunk.data)
    print("\n\n")

```

**Install the LangGraph JS SDK**

```md-code__content
npm install @langchain/langgraph-sdk

```

**Send a message to the assistant (threadless run)**

```md-code__content
const { Client } = await import("@langchain/langgraph-sdk");

const client = new Client({ apiUrl: "your-deployment-url", apiKey: "your-langsmith-api-key" });

const streamResponse = client.runs.stream(
    null, // Threadless run
    "agent", // Assistant ID
    {
        input: {
            "messages": [\
                { "role": "user", "content": "What is LangGraph?"}\
            ]
        },
        streamMode: "messages",
    }
);

for await (const chunk of streamResponse) {
    console.log(`Receiving new event of type: ${chunk.event}...`);
    console.log(JSON.stringify(chunk.data));
    console.log("\n\n");
}

```

```md-code__content
curl -s --request POST \
    --url <DEPLOYMENT_URL> \
    --header 'Content-Type: application/json' \
    --data "{
        \"assistant_id\": \"agent\",
        \"input\": {
            \"messages\": [\
                {\
                    \"role\": \"human\",\
                    \"content\": \"What is LangGraph?\"\
                }\
            ]
        },
        \"stream_mode\": \"updates\"
    }"

```

## Next Steps [¶](https://langchain-ai.github.io/langgraph/cloud/quick_start/\#next-steps "Permanent link")

Congratulations! If you've worked your way through this tutorial you are well on your way to becoming a LangGraph Cloud expert. Here are some other resources to check out to help you out on the path to expertise:

### LangGraph Framework [¶](https://langchain-ai.github.io/langgraph/cloud/quick_start/\#langgraph-framework "Permanent link")

- **[LangGraph Tutorial](https://langchain-ai.github.io/langgraph/tutorials/introduction/)**: Get started with LangGraph framework.
- **[LangGraph Concepts](https://langchain-ai.github.io/langgraph/concepts/)**: Learn the foundational concepts of LangGraph.
- **[LangGraph How-to Guides](https://langchain-ai.github.io/langgraph/how-tos/)**: Guides for common tasks with LangGraph.

### 📚 Learn More about LangGraph Platform [¶](https://langchain-ai.github.io/langgraph/cloud/quick_start/\#learn-more-about-langgraph-platform "Permanent link")

Expand your knowledge with these resources:

- **[LangGraph Platform Concepts](https://langchain-ai.github.io/langgraph/concepts/#langgraph-platform)**: Understand the foundational concepts of the LangGraph Platform.
- **[LangGraph Platform How-to Guides](https://langchain-ai.github.io/langgraph/how-tos/#langgraph-platform)**: Discover step-by-step guides to build and deploy applications.
- **[Launch Local LangGraph Server](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/)**: This quick start guide shows how to start a LangGraph Server locally for the **ReAct Agent** template. The steps are similar for other templates.

## Comments

giscus

#### [6 reactions](https://github.com/langchain-ai/langgraph/discussions/866)

🚀6

#### [11 comments](https://github.com/langchain-ai/langgraph/discussions/866)

#### ·

#### 23 replies

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@Jaid844](https://avatars.githubusercontent.com/u/112820053?u=8eda894440421e180bc58e14696a4dc9b423dd81&v=4)Jaid844](https://github.com/Jaid844) [Jun 29, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-9910575)

Let's goo yeahh!!

2

0 replies

[![@DhavalThkkar](https://avatars.githubusercontent.com/u/16734921?u=0806ac526d123c4f364578bf128022b8a4772783&v=4)DhavalThkkar](https://github.com/DhavalThkkar) [Jul 1, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-9928781)

Contributor

So there'll be no way to deploy this using Langserve locally?

Can I get it working without LangSmith?

1

3 replies

[![@hinthornw](https://avatars.githubusercontent.com/u/13333726?u=82ebf1e0eb0663ebd49ba66f67a43f51bbf11442&v=4)](https://github.com/hinthornw)

[hinthornw](https://github.com/hinthornw) [Jul 1, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-9929843)

Contributor

You can use langserve or your own fastAPI endpoint - it just won't get the additional cloud features we've built in

[![@DhavalThkkar](https://avatars.githubusercontent.com/u/16734921?u=0806ac526d123c4f364578bf128022b8a4772783&v=4)](https://github.com/DhavalThkkar)

[DhavalThkkar](https://github.com/DhavalThkkar) [Jul 2, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-9935307)

Contributor

Any samples that you'd recommend? There seems to be little to no documentation available for that and since there is state management in langgraph, integrating with langserve becomes equally challenging

[![@vbarda](https://avatars.githubusercontent.com/u/19161700?u=e76bcd472b51c9f07befd2654783d0a381f49005&v=4)](https://github.com/vbarda)

[vbarda](https://github.com/vbarda) [Oct 31, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11114488)

Collaborator

[@DhavalThkkar](https://github.com/DhavalThkkar) we just added more deployment options for LangGraph Platform (formerly LangGraph Cloud), including "Self-hosted Lite" - a limited **free** version. It is available to anyone with a **free** (developer) [LangSmith account](https://giscus.app/en/smith.langchain.com). Please check out the documentation to learn more: [https://langchain-ai.github.io/langgraph/concepts/deployment\_options/#self-hosted-lite](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-lite). let me know if you have any questions!

[![@damianoneill](https://avatars.githubusercontent.com/u/15426674?v=4)damianoneill](https://github.com/damianoneill) [Aug 30, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-10500291)

[@hinthornw](https://github.com/hinthornw) can you provide an example of integrating with langserve?

1

3 replies

[![@eyurtsev](https://avatars.githubusercontent.com/u/3205522?v=4)](https://github.com/eyurtsev)

[eyurtsev](https://github.com/eyurtsev) [Nov 19, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11312402)

Contributor

LangServe does not officially support LangGraph and we recommend that users use LangGraph Platform for deployment. ( [https://github.com/langchain-ai/langserve/discussions/790](https://github.com/langchain-ai/langserve/discussions/790))

[![@ryang420](https://avatars.githubusercontent.com/u/9249372?u=5b35c83798a024f1a5ae40c9e8d2bc7b9e2580f2&v=4)](https://github.com/ryang420)

[ryang420](https://github.com/ryang420) [Jan 4](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11732725)

Hi [@eyurtsev](https://github.com/eyurtsev),

In my LangSmith account, there isn't a "deployment" button on the "LangGraph Platform" page. I can only see the "Option Studio" there. Is it because of my beta user license?

[![@SharoMonk](https://avatars.githubusercontent.com/u/108334523?v=4)](https://github.com/SharoMonk)

[SharoMonk](https://github.com/SharoMonk) [Jan 6](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11745758)

I am having the same problem. i cant see the New Deployment button, Why?

[![@rogerthatdev](https://avatars.githubusercontent.com/u/31829545?u=9a3e62c278e840f87a15b3f66f8fbc11b3816f5d&v=4)rogerthatdev](https://github.com/rogerthatdev) [Sep 12, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-10630868)

Hi!

When accessing our agent via the SDK, we're not seeing the same object returned that's in these docs.

```notranslate
{'agent': {'messages': [{'content': "Hi Bagatur! It's nice to meet you. How can I assist you today?", 'additional_kwargs': {}, 'response_metadata': {'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_9cb5d38cf7'}, 'type': 'ai', 'name': None, 'id': 'run-c89118b7-1b1e-42b9-a85d-c43fe99881cd', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}

```

by any chance, are these docs up to date? Are there additional SDK docs for Javascript?

1

0 replies

[![@lvyoudashuju](https://avatars.githubusercontent.com/u/22024581?v=4)lvyoudashuju](https://github.com/lvyoudashuju) [Sep 18, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-10679419)

[@hinthornw](https://github.com/hinthornw) can you provide an example of integrating with langserve or?

or can you provide an example of own fastAPI endpoint?

1

3 replies

[![@fletchertyler914](https://avatars.githubusercontent.com/u/3344498?u=be6f2ff193f913fb9b7ad2c9c1c98b6f8eaf93f4&v=4)](https://github.com/fletchertyler914)

[fletchertyler914](https://github.com/fletchertyler914) [Sep 24, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-10743755)

Here's my current solution to streaming events from langgraph via a langserve project. You could simplify it a lot more, as im dealing with multiple tools in a ReAct style graph now. I originally used langserve with pure LCEL before langgraph came out, and ended up converting to langgraph ad use SSE to stream all LLM and tool tokens. Here's an overview of the API side:

```notranslate
# Load environment variables from .env file before importing any other modules
from dotenv import load_dotenv
load_dotenv(override=True)  # noqa

from fastapi import APIRouter, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, StreamingResponse

from api.models.api import GraphRequest

# Create a router for all /api routes
router = APIRouter()

# Redirect the root to the documentation
@router.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/api/docs")

@router.get("/health-check")
def readiness_probe():
    return Response(status_code=200, content="API is healthy")

@router.post("/v1/chat")
async def chat_stream(
    request: Request,
    body: GraphRequest
):
    try:
        # Get the server config from the request (per user)
        server_config = await per_req_config_modifier({}, request)
        # print("Chat Req Server Config:", server_config)

        return StreamingResponse(
            generate_chat_events(
                message=body.message,
                config=server_config,
            ),
            media_type="text/event-stream"
        )
    except Exception as e:
        return StreamingResponse(
            content=f"event: error\ndata: {str(e)}\n\n",
            status_code=500,
            media_type="text/event-stream"
        )

# Create the FastAPI app
app = FastAPI(
    title="API Server",
    version="1.0",
    description="API server for LangGraph",
    root_path="/api"
)

# Mount the router under the /api prefix
app.include_router(router)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001,
        proxy_headers=True,
        forwarded_allow_ips="*"
    )

```

where my `generate_chat_events` is essentially a middleware to customize/filter the event stream. It looks like this:

```notranslate
async def generate_chat_events(message: str, config: RunnableConfig):
    # print("Generating Chat Events", message, config)
    async for event in graph.astream_events(
        input=format_user_input(message),
        config=config,
        version="v2",
    ):
        kind = event["event"]
        tags = event.get("tags", [])

        # Graph Stream
        if kind == "on_chat_model_stream" and "chat_node" in tags:
            # Check if the chunk has content
            chunk = event["data"]["chunk"]

            if chunk.content:
                # Serialize the chunk content
                chunk_content = serialize_ai_message_chunk(chunk)

                # Yield the formatted SSE content
                yield build_response_message(
                    chunk_content=chunk_content,
                    config=config
                )

       # Here I have tool calls that I want to yield events to show a 'status' update in the UI. This is optional, only if you have tools and want to know when they stop/start.

        # Start Tool Status
        elif kind == "on_tool_start":
            if event["name"] == "guest_search_tool":
                yield build_response_message(
                    chunk_content="\nFinding Matching Guest... ",
                    config=config
                )
            elif event["name"] == "guest_sample_tool":
                yield build_response_message(
                    chunk_content="\n\nGetting Guest Sample... ",
                    # reset the guest sample
                    guest_sample=[],
                    config=config
                )

        # End Tool Status
        elif kind == "on_tool_end":
            if event["name"] == "guest_search_tool":
                yield build_response_message(
                    # chunk_content="Done!\n\n",
                    chunk_content="✅\n\n",
                    config=config
                )
            elif event["name"] == "guest_sample_tool":
                # Get the guest sample from the event data
                event_data = event["data"]["output"]
                # print(event_data)
                guest_sample = event_data.artifact

                yield build_response_message(
                    # chunk_content="Done!\n",
                    chunk_content="✅\n\n",
                    guest_sample=guest_sample,
                    config=config
                )

```

here are the helper functions:

```notranslate

def serialize_ai_message_chunk(chunk):
    """
    Custom serializer for AIMessageChunk objects.
    Convert the AIMessageChunk object to a serializable format.
    """
    if isinstance(chunk, AIMessageChunk):
        return chunk.content
    else:
        raise TypeError(
            f"Object of type {type(chunk).__name__} is not correctly formatted for serialization"
        )

def format_user_input(content: str):
    return {
        "messages": [\
            HumanMessage(content)\
        ]
    }

def build_response_message(
        config: RunnableConfig,
        chunk_content: str = None,
        guest_sample=None,
        messages=None,
):
    # yield the current state after each event
    graph_state = graph.get_state(config).values
    messages = graph_state.get("messages", [])

    # convert the messages to a serializable format
    messages = [\
        {\
            "role": message.type,\
            "content": message.content\
        }\
        for message in messages\
    ]

    # Properly format the content for SSE
   # This is my custom response type, you can return whatever you want here, or only the chunk_content!
    data = json.dumps({
        "content": chunk_content,
        "guest_sample": guest_sample,
        "messages": messages,
    })
    # Format the event message
    return f"event: message\ndata: {data}\n\n"

```

You can just return the graph stream or stream\_events, but its helpful to format/filter the stream events in the api side so your frontend only gets the events you want displayed. I may put a simple repo up to show this in action.

👍1❤️1

[![@think-circle](https://avatars.githubusercontent.com/u/69625090?v=4)](https://github.com/think-circle)

[think-circle](https://github.com/think-circle) [Oct 14, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-10941153)

Has anyone got it working on langserve both from python backend and react js front end ?

[![@eyurtsev](https://avatars.githubusercontent.com/u/3205522?v=4)](https://github.com/eyurtsev)

[eyurtsev](https://github.com/eyurtsev) [Nov 19, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11312422)

Contributor

If you have a very simple application, you can wrap it yourself in a Fast API server. If you need more support for long-running tasks, built-in memory, double texting etc. consider using LangGraph Platform. We're officially recommending that new applications be deployed using LangGraph Platform instead of LangServe.

More information is here:

- [https://langchain-ai.github.io/langgraph/concepts/#langgraph-platform](https://langchain-ai.github.io/langgraph/concepts/#langgraph-platform)
- [https://github.com/langchain-ai/langserve/discussions/790](https://github.com/langchain-ai/langserve/discussions/790)

[![@vbarda](https://avatars.githubusercontent.com/u/19161700?u=e76bcd472b51c9f07befd2654783d0a381f49005&v=4)vbarda](https://github.com/vbarda) [Oct 31, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11114498)

Collaborator

Hi folks! We just added more deployment options for LangGraph Platform (formerly LangGraph Cloud), including "Self-hosted Lite" - a limited **free** version. It is available to anyone with a **free** (developer) [LangSmith account](https://giscus.app/en/smith.langchain.com). Please check out the documentation to learn more: [https://langchain-ai.github.io/langgraph/concepts/deployment\_options/#self-hosted-lite](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-lite). let me know if you have any questions!

1

4 replies

[![@mger1608](https://avatars.githubusercontent.com/u/59756802?v=4)](https://github.com/mger1608)

[mger1608](https://github.com/mger1608) [Nov 19, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11304624)

I've had some trouble getting this guide you created to work on Windows 11 machine. Particularly when it comes to working with the docker container. It appears that I can build the container but not much beyond that.

[![@eyurtsev](https://avatars.githubusercontent.com/u/3205522?v=4)](https://github.com/eyurtsev)

[eyurtsev](https://github.com/eyurtsev) [Nov 19, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11312396)

Contributor

Could you open an issue describing the issue that you're seeing (including stack trace etc)

[![@mger1608](https://avatars.githubusercontent.com/u/59756802?v=4)](https://github.com/mger1608)

[mger1608](https://github.com/mger1608) [Nov 20, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11328195)

I think I finally got it sorted out but none of the documentation online makes it clear what the best procedure should be for local hosting. I was able to spin up a local server that connected to LangStudio via this video created yesterday: [https://www.youtube.com/watch?v=o9CT5ohRHzY](https://www.youtube.com/watch?v=o9CT5ohRHzY)

IMHO I would recommend all users to this lightweight deployment. Everything else tends to muck up the deployment process. I spent ~6 hours trying to debug paths, environment variables, etc. The referenced video took 15 minutes and worked great.

Thank you for all the work you all are doing!! Can't wait to keep building.

❤️1

[![@aklos](https://avatars.githubusercontent.com/u/8189043?u=f5d41a275ad325afe41c7bb4bd4cc441a8772089&v=4)](https://github.com/aklos)

[aklos](https://github.com/aklos) [Jan 11](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11805437)

edited

What does 1 million nodes executed mean? In a single graph run? In total? Per month? I'm trying to figure out if Self-Hosted Lite is right for my projects, but it feels like I have to lock-in and find out the hard way instead of finding any relevant information in the docs.

Assuming it's a cumulative total: Why is the only other option to then pay for Enterprise? It seems like I can run a crappy little chatbot for 100 users for a few months before hitting the limit and then I have to probably fork out hundreds/thousands of dollars to continue. If that's the case, why would I use this? I'd very much rather implement my own task orchestration, vector database, and REST API.

[![@michaelwwn](https://avatars.githubusercontent.com/u/115132168?u=202bdad645197f412e86159c25702a75ef6c72fe&v=4)michaelwwn](https://github.com/michaelwwn) [Nov 24, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11364270)

Hi, is there an option to access the database hosted on langgraph cloud?

1

1 reply

[![@eyurtsev](https://avatars.githubusercontent.com/u/3205522?v=4)](https://github.com/eyurtsev)

[eyurtsev](https://github.com/eyurtsev) [Dec 20, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11630193)

Contributor

Not directly, but you can interact with it via the API [https://langchain-ai.github.io/langgraph/cloud/reference/api/api\_ref.html](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html)

[![@emiliansiemsia](https://avatars.githubusercontent.com/u/13001416?u=4f2dfe972f8fc5a6b920e2aaa55bfc85f459ffa2&v=4)emiliansiemsia](https://github.com/emiliansiemsia) [Dec 1, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11428159)

I don't see the '+ New Deployment' option on the LangGraph Studio page; I can only connect to the local LangGraph.

1

3 replies

[![@Jeffy-Fung](https://avatars.githubusercontent.com/u/92999261?v=4)](https://github.com/Jeffy-Fung)

[Jeffy-Fung](https://github.com/Jeffy-Fung) [Dec 13, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11551462)

Hi, do I need to do anything to store chat history in the database? For example: implement checkpointer?

[![@eyurtsev](https://avatars.githubusercontent.com/u/3205522?v=4)](https://github.com/eyurtsev)

[eyurtsev](https://github.com/eyurtsev) [Dec 13, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11551523)

Contributor

Review this part of the tutorial for how to add memory for a chat bot: [https://langchain-ai.github.io/langgraph/tutorials/introduction/#part-3-adding-memory-to-the-chatbot](https://langchain-ai.github.io/langgraph/tutorials/introduction/#part-3-adding-memory-to-the-chatbot)

You do not need to implement a checkpointer, but you do need to make sure that the graph is compiled w/ a checkpointer when launching it locally. When you deploy it with langgraph cloud, a checkpointer will be automatically configured for it (LangGraph cloud will deploy a postgres instance together with your server).

❤️1

[![@Jeffy-Fung](https://avatars.githubusercontent.com/u/92999261?v=4)](https://github.com/Jeffy-Fung)

[Jeffy-Fung](https://github.com/Jeffy-Fung) [Dec 22, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11640630)

edited

Thanks for answering!

And yes, I have already read about the usage of a checkpointer.

To clarify, so what we need to do is just make sure we use the provided checkpointer for postresql db, and the configuration, i.e.: `thread_id` will be handled automatically, with LangGraph cloud?

If so, may I know is there way for me to retrieve the chat history?

And furthermore, is it possible for me to customised the configuration? Say I want to resume the previous `thread_id`?

As I cannot customize the configuration triggered by `.invoke(...)` or `.stream(...)`, when using LangGraph cloud.

Thanks for your response 💯 🙏🏼

[![@abhaychandavar](https://avatars.githubusercontent.com/u/45521259?v=4)abhaychandavar](https://github.com/abhaychandavar) [Dec 19, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11617732)

I couldn't find '+ New Deployment' option on the LangGraph Studio page. How do I access it?

1

👍3

5 replies

[![@eyurtsev](https://avatars.githubusercontent.com/u/3205522?v=4)](https://github.com/eyurtsev)

[eyurtsev](https://github.com/eyurtsev) [Dec 20, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11630185)

Contributor

Do you have a LangGraph Platform option on the left hand sidebar? (Step 2: [https://langchain-ai.github.io/langgraph/cloud/quick\_start/#deploy-to-langgraph-cloud](https://langchain-ai.github.io/langgraph/cloud/quick_start/#deploy-to-langgraph-cloud))

[![@anilmuppalla](https://avatars.githubusercontent.com/u/321785?u=32cc177ee6b96c8601f14930a40154d1d7441d0b&v=4)](https://github.com/anilmuppalla)

[anilmuppalla](https://github.com/anilmuppalla) [Dec 27, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11673875)

I don't have LangGraph Studio, since I am on linux, not sure if that is relevant.

I can see the LangGraph platfrom option on the left sidebar, however I don't see the option to create a new deployment. All I see is this note:

```notranslate

```

👍1

[![@anilmuppalla](https://avatars.githubusercontent.com/u/321785?u=32cc177ee6b96c8601f14930a40154d1d7441d0b&v=4)](https://github.com/anilmuppalla)

[anilmuppalla](https://github.com/anilmuppalla) [Dec 27, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11673876)

this is the note I see:

All LangSmith users on Plus, Premier, Startup, or Enterprise plans can now access LangGraph Platform for free in its beta.

[![@eyurtsev](https://avatars.githubusercontent.com/u/3205522?v=4)](https://github.com/eyurtsev)

[eyurtsev](https://github.com/eyurtsev) [Dec 27, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11678203)

Contributor

edited

Are you on a paid plan? Cloud is free while in beta for LangSmith users that are on one of the paid plans.

[![@anilmuppalla](https://avatars.githubusercontent.com/u/321785?u=32cc177ee6b96c8601f14930a40154d1d7441d0b&v=4)](https://github.com/anilmuppalla)

[anilmuppalla](https://github.com/anilmuppalla) [Dec 27, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11679992)

edited

it was not clear from the website that only paid users of langsmith can use cloud, you've to login to see the note. Perhaps you can make this explicit on the platfrom pricing page

👍1

[![@grupocopa](https://avatars.githubusercontent.com/u/124201144?u=ae107f233c8927c9532a0eb9d67582449a01faa1&v=4)grupocopa](https://github.com/grupocopa) [Dec 28, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11687796)

I am having the same [@anilmuppalla](https://github.com/anilmuppalla) issue. It's not opened the deployment for the ''Developer'' plan, it's only for paid users? Because it's really not clear

1

1 reply

[![@anilmuppalla](https://avatars.githubusercontent.com/u/321785?u=32cc177ee6b96c8601f14930a40154d1d7441d0b&v=4)](https://github.com/anilmuppalla)

[anilmuppalla](https://github.com/anilmuppalla) [Dec 29, 2024](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11687800)

I use Pydantic AI now, it fits my needs pretty well

[![@flan02](https://avatars.githubusercontent.com/u/51976743?u=2f867ca14398d32f5165345e00d3308d1ab5e999&v=4)flan02](https://github.com/flan02) [Jan 6](https://github.com/langchain-ai/langgraph/discussions/866#discussioncomment-11743293)

I'm using langchain to build more robust AI agents, it is a great tool! I recommend it!

1

0 replies

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fquick_start%2F)