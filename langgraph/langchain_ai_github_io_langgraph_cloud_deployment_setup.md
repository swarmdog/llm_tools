[Skip to content](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#how-to-set-up-a-langgraph-application-for-deployment)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/deployment/setup.md "Edit this page")

# How to Set Up a LangGraph Application for Deployment [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/\#how-to-set-up-a-langgraph-application-for-deployment "Permanent link")

A LangGraph application must be configured with a [LangGraph API configuration file](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file) in order to be deployed to LangGraph Cloud (or to be self-hosted). This how-to guide discusses the basic steps to setup a LangGraph application for deployment using `requirements.txt` to specify project dependencies.

This walkthrough is based on [this repository](https://github.com/langchain-ai/langgraph-example), which you can play around with to learn more about how to setup your LangGraph application for deployment.

Setup with pyproject.toml

If you prefer using poetry for dependency management, check out [this how-to guide](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_pyproject/) on using `pyproject.toml` for LangGraph Cloud.

Setup with a Monorepo

If you are interested in deploying a graph located inside a monorepo, take a look at [this](https://github.com/langchain-ai/langgraph-example-monorepo) repository for an example of how to do so.

The final repo structure will look something like this:

```md-code__content
my-app/
├── my_agent # all project code lies within here
│   ├── utils # utilities for your graph
│   │   ├── __init__.py
│   │   ├── tools.py # tools for your graph
│   │   ├── nodes.py # node functions for you graph
│   │   └── state.py # state definition of your graph
│   ├── requirements.txt # package dependencies
│   ├── __init__.py
│   └── agent.py # code for constructing your graph
├── .env # environment variables
└── langgraph.json # configuration file for LangGraph

```

After each step, an example file directory is provided to demonstrate how code can be organized.

## Specify Dependencies [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/\#specify-dependencies "Permanent link")

Dependencies can optionally be specified in one of the following files: `pyproject.toml`, `setup.py`, or `requirements.txt`. If none of these files is created, then dependencies can be specified later in the [LangGraph API configuration file](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#create-langgraph-api-config).

The dependencies below will be included in the image, you can also use them in your code, as long as with a compatible version range:

```md-code__content
langgraph>=0.2.56,<0.4.0
langgraph-sdk>=0.1.53
langgraph-checkpoint>=2.0.15,<3.0
langchain-core>=0.2.38,<0.4.0
langsmith>=0.1.63
orjson>=3.9.7
httpx>=0.25.0
tenacity>=8.0.0
uvicorn>=0.26.0
sse-starlette>=2.1.0,<2.2.0
uvloop>=0.18.0
httptools>=0.5.0
jsonschema-rs>=0.20.0
structlog>=23.1.0

```

Example `requirements.txt` file:

```md-code__content
langgraph
langchain_anthropic
tavily-python
langchain_community
langchain_openai

```

Example file directory:

```md-code__content
my-app/
├── my_agent # all project code lies within here
│   └── requirements.txt # package dependencies

```

## Specify Environment Variables [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/\#specify-environment-variables "Permanent link")

Environment variables can optionally be specified in a file (e.g. `.env`). See the [Environment Variables reference](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/) to configure additional variables for a deployment.

Example `.env` file:

```md-code__content
MY_ENV_VAR_1=foo
MY_ENV_VAR_2=bar
OPENAI_API_KEY=key

```

Example file directory:

```md-code__content
my-app/
├── my_agent # all project code lies within here
│   └── requirements.txt # package dependencies
└── .env # environment variables

```

## Define Graphs [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/\#define-graphs "Permanent link")

Implement your graphs! Graphs can be defined in a single file or multiple files. Make note of the variable names of each [CompiledGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.graph.CompiledGraph) to be included in the LangGraph application. The variable names will be used later when creating the [LangGraph API configuration file](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file).

Example `agent.py` file, which shows how to import from other modules you define (code for the modules is not shown here, please see [this repo](https://github.com/langchain-ai/langgraph-example) to see their implementation):

```md-code__content
# my_agent/agent.py
from typing import Literal
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, END, START
from my_agent.utils.nodes import call_model, should_continue, tool_node # import nodes
from my_agent.utils.state import AgentState # import state

# Define the config
class GraphConfig(TypedDict):
    model_name: Literal["anthropic", "openai"]

workflow = StateGraph(AgentState, config_schema=GraphConfig)
workflow.add_node("agent", call_model)
workflow.add_node("action", tool_node)
workflow.add_edge(START, "agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "action",
        "end": END,
    },
)
workflow.add_edge("action", "agent")

graph = workflow.compile()

```

API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) \| [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) \| [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

Assign `CompiledGraph` to Variable

The build process for LangGraph Cloud requires that the `CompiledGraph` object be assigned to a variable at the top-level of a Python module (alternatively, you can provide [a function that creates a graph](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/)).

Example file directory:

```md-code__content
my-app/
├── my_agent # all project code lies within here
│   ├── utils # utilities for your graph
│   │   ├── __init__.py
│   │   ├── tools.py # tools for your graph
│   │   ├── nodes.py # node functions for you graph
│   │   └── state.py # state definition of your graph
│   ├── requirements.txt # package dependencies
│   ├── __init__.py
│   └── agent.py # code for constructing your graph
└── .env # environment variables

```

## Create LangGraph API Config [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/\#create-langgraph-api-config "Permanent link")

Create a [LangGraph API configuration file](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file) called `langgraph.json`. See the [LangGraph CLI reference](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file) for detailed explanations of each key in the JSON object of the configuration file.

Example `langgraph.json` file:

```md-code__content
{
  "dependencies": ["./my_agent"],
  "graphs": {
    "agent": "./my_agent/agent.py:graph"
  },
  "env": ".env"
}

```

Note that the variable name of the `CompiledGraph` appears at the end of the value of each subkey in the top-level `graphs` key (i.e. `:<variable_name>`).

Configuration Location

The LangGraph API configuration file must be placed in a directory that is at the same level or higher than the Python files that contain compiled graphs and associated dependencies.

Example file directory:

```md-code__content
my-app/
├── my_agent # all project code lies within here
│   ├── utils # utilities for your graph
│   │   ├── __init__.py
│   │   ├── tools.py # tools for your graph
│   │   ├── nodes.py # node functions for you graph
│   │   └── state.py # state definition of your graph
│   ├── requirements.txt # package dependencies
│   ├── __init__.py
│   └── agent.py # code for constructing your graph
├── .env # environment variables
└── langgraph.json # configuration file for LangGraph

```

## Next [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/\#next "Permanent link")

After you setup your project and place it in a github repo, it's time to [deploy your app](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/).

## Comments

giscus

#### [0 reactions](https://github.com/langchain-ai/langgraph/discussions/1235)

#### [4 comments](https://github.com/langchain-ai/langgraph/discussions/1235)

#### ·

#### 5 replies

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@shanngray](https://avatars.githubusercontent.com/u/161181753?u=5d8f6323bb72ac4f661b3b05b4d6f4a5864d5ff5&v=4)shanngray](https://github.com/shanngray) [Aug 6, 2024](https://github.com/langchain-ai/langgraph/discussions/1235#discussioncomment-10256918)

I'm trying to setup my project to use LangGraph Studio, but I currently have the State, graph and compiled graph all in separate files and and LangGraph Studio keeps exiting with code 3 and the log says it is unable to find the module where the uncompiled graph is located.

1

3 replies

[![@hwchase17](https://avatars.githubusercontent.com/u/11986836?u=f4c4f21a82b2af6c9f91e1f1d99ea40062f7a101&v=4)](https://github.com/hwchase17)

[hwchase17](https://github.com/hwchase17) [Aug 6, 2024](https://github.com/langchain-ai/langgraph/discussions/1235#discussioncomment-10257135)

Contributor

can you share your laggraph.json and a more complete error message?

👍1

[![@shanngray](https://avatars.githubusercontent.com/u/161181753?u=5d8f6323bb72ac4f661b3b05b4d6f4a5864d5ff5&v=4)](https://github.com/shanngray)

[shanngray](https://github.com/shanngray) [Aug 6, 2024](https://github.com/langchain-ai/langgraph/discussions/1235#discussioncomment-10257807)

Thanks for the quick reply! The uncompiled graph is named 'workflow' and is in build\_graph.py this is imported into main.py and compiled into the variable 'app'.

## langgraph.json:

{

"python\_version": "3.11",

"dockerfile\_lines": \[\],

"dependencies": \[\
\
"./"\
\
\],

"graphs": {

"app": "./baa\_black\_sheep/main.py:app"

},

"env": "./baa\_black\_sheep/.env"

}

## Log:

langgraph-api-1 \| 2024-08-06T20:38:19.788024Z \[error \] Traceback (most recent call last):

langgraph-api-1 \| File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 732, in lifespan

langgraph-api-1 \| async with self.lifespan\_context(app) as maybe\_state:

langgraph-api-1 \| File "/usr/local/lib/python3.11/contextlib.py", line 210, in **aenter**

langgraph-api-1 \| return await anext(self.gen)

langgraph-api-1 \| ^^^^^^^^^^^^^^^^^^^^^

langgraph-api-1 \| File "/api/langgraph\_api/lifespan.py", line 22, in lifespan

langgraph-api-1 \| File "/api/langgraph\_api/shared/graph.py", line 116, in collect\_graphs\_from\_env

langgraph-api-1 \| File "/usr/local/lib/python3.11/site-packages/langchain\_core/runnables/config.py", line 620, in run\_in\_executor

langgraph-api-1 \| return await asyncio.get\_running\_loop().run\_in\_executor(

langgraph-api-1 \| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

langgraph-api-1 \| File "/usr/local/lib/python3.11/concurrent/futures/thread.py", line 58, in run

langgraph-api-1 \| result = self.fn(\*self.args, \*\*self.kwargs)

langgraph-api-1 \| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

langgraph-api-1 \| File "/usr/local/lib/python3.11/site-packages/langchain\_core/runnables/config.py", line 611, in wrapper

langgraph-api-1 \| return func(\*args, \*\*kwargs)

langgraph-api-1 \| ^^^^^^^^^^^^^^^^^^^^^

langgraph-api-1 \| File "/api/langgraph\_api/shared/graph.py", line 140, in \_graph\_from\_spec

langgraph-api-1 \| File "/api/langgraph\_api/shared/graph.py", line 137, in \_graph\_from\_spec

langgraph-api-1 \| File "", line 940, in exec\_module

langgraph-api-1 \| File "", line 241, in \_call\_with\_frames\_removed

langgraph-api-1 \| File "/deps/baa\_black\_sheep/baa\_black\_sheep/main.py", line 24, in

langgraph-api-1 \| from build\_graph import workflow

langgraph-api-1 \| ModuleNotFoundError: No module named 'build\_graph'

langgraph-api-1 \| Could not import python module for graph: GraphSpec(id='app', path='/deps/baa\_black\_sheep/baa\_black\_sheep/main.py', module=None, variable='app')

langgraph-api-1 \| \[uvicorn.error\] api\_revision=11efdb7 api\_variant=licensed desktop=0.0.11 filename=on.py func\_name=send lineno=121

langgraph-api-1 \| 2024-08-06T20:38:19.788364Z \[error \] Application startup failed. Exiting. \[uvicorn.error\] api\_revision=11efdb7 api\_variant=licensed desktop=0.0.11 filename=on.py func\_name=startup lineno=59

langgraph-api-1 exited with code 3

[![@isahers1](https://avatars.githubusercontent.com/u/78627776?u=7fd9922950b898ab502666f2cea155cf0200fe5f&v=4)](https://github.com/isahers1)

[isahers1](https://github.com/isahers1) [Aug 8, 2024](https://github.com/langchain-ai/langgraph/discussions/1235#discussioncomment-10269875)

Contributor

Is this repo any help: [https://github.com/langchain-ai/langgraph-example-monorepo](https://github.com/langchain-ai/langgraph-example-monorepo)?

[![@antoremin](https://avatars.githubusercontent.com/u/6918736?v=4)antoremin](https://github.com/antoremin) [Sep 24, 2024](https://github.com/langchain-ai/langgraph/discussions/1235#discussioncomment-10742573)

When I open my app in LG Studio, it puts out logs below and doesn't run. Any advice?

Running "docker pull langchain/langgraph-api:3.11"

Running "docker image prune -f --filter label=com.docker.compose.project=search\_agent-2ce896732568f73d28c957e4ca0372808bfd8db733483301b04654c5ed44cb02"

Saved file tree to doc-filelist.js

Copied JS to doc-script.js

Compiled CSS to doc-style.css

Running "docker container prune -f --filter label=com.docker.compose.project=search\_agent-2ce896732568f73d28c957e4ca0372808bfd8db733483301b04654c5ed44cb02"

Saved file tree to doc-filelist.js

Copied JS to doc-script.js

Compiled CSS to doc-style.css

Running "docker compose --project-directory /Users/antoneremin/workspace/abinbev/search\_agent --project-name search\_agent-2ce896732568f73d28c957e4ca0372808bfd8db733483301b04654c5ed44cb02 -f - up --remove-orphans"

Saved file tree to doc-filelist.js

Copied JS to doc-script.js

Compiled CSS to doc-style.css

Saved file tree to doc-filelist.js

Copied JS to doc-script.js

Compiled CSS to doc-style.css

1

0 replies

[![@TimChild](https://avatars.githubusercontent.com/u/48571510?u=461c39272e0c2fff29afc5ecc5957267f2f7aca9&v=4)TimChild](https://github.com/TimChild) [Sep 25, 2024](https://github.com/langchain-ai/langgraph/discussions/1235#discussioncomment-10755595)

Is there any concept of `lifespan` that we can use to run setup/teardown in?

For example, something like initializing a connection pool to a database so that all nodes that need data from the database can get a session from the pool.

Or just running any other startup/shutdown tasks. It would be really nice to be able to specify a path to (an async) lifespan function in the `langgraph.json` for example.

If I've missed something in the docs, sorry about that, but I have not yet found anything.

3

👍1

1 reply

[![@pkrs](https://avatars.githubusercontent.com/u/454860?u=2da352a0c1e765dc444d99ac46ce49c4e00b8a84&v=4)](https://github.com/pkrs)

[pkrs](https://github.com/pkrs) [Oct 22, 2024](https://github.com/langchain-ai/langgraph/discussions/1235#discussioncomment-11021567)

+1 to this. Having trouble setting up langgraph studio alogside a production project that needs this kind of a capability

[![@EricJayHartman](https://avatars.githubusercontent.com/u/9259499?u=7e58cc7ec0cd3e85b27aec33656aa0f6612706dd&v=4)EricJayHartman](https://github.com/EricJayHartman) [Oct 26, 2024](https://github.com/langchain-ai/langgraph/discussions/1235#discussioncomment-11060484)

Would love to see an example that shows multiple agents, and how they can interact; it seems LangGraph Studio currently treats Agents independently by only allowing the user to select one at a time. However, importantly, the user may want to create agents as sub-graphs, which call and are called by other agents (graphs).

I've also had some trouble getting LangGraph studio and UV working together nicely.

Here is an illustration of a more complicated example that would be nice to illustrate in these documents.

my-app/

├── agent\_ceo # calls sub-graphs, like agent\_cfo

│ ├── ...

├── agent\_cfo # an agent, but also a sub-graph

│ ├── ...

├── agent\_analyst # called by agent\_cfo

│ ├── ...

├── .env

└── langgraph.json

├── uv.lock # support for UV

└── pyproject.toml # support for toml leveraging uv

1

👍1

1 reply

[![@sarick-story](https://avatars.githubusercontent.com/u/194532771?v=4)](https://github.com/sarick-story)

[sarick-story](https://github.com/sarick-story) [Jan 16](https://github.com/langchain-ai/langgraph/discussions/1235#discussioncomment-11849151)

@HartmanAnalytics were u able to get uv working with langgraph?

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fdeployment%2Fsetup%2F)