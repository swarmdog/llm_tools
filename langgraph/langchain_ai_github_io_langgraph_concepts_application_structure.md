[Skip to content](https://langchain-ai.github.io/langgraph/concepts/application_structure/#application-structure)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/application_structure.md "Edit this page")

# Application Structure [¶](https://langchain-ai.github.io/langgraph/concepts/application_structure/\#application-structure "Permanent link")

Prerequisites

- [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)
- [LangGraph Glossary](https://langchain-ai.github.io/langgraph/concepts/low_level/)

## Overview [¶](https://langchain-ai.github.io/langgraph/concepts/application_structure/\#overview "Permanent link")

A LangGraph application consists of one or more graphs, a LangGraph API Configuration file ( `langgraph.json`), a file that specifies dependencies, and an optional .env file that specifies environment variables.

This guide shows a typical structure for a LangGraph application and shows how the required information to deploy a LangGraph application using the LangGraph Platform is specified.

## Key Concepts [¶](https://langchain-ai.github.io/langgraph/concepts/application_structure/\#key-concepts "Permanent link")

To deploy using the LangGraph Platform, the following information should be provided:

1. A [LangGraph API Configuration file](https://langchain-ai.github.io/langgraph/concepts/application_structure/#configuration-file) ( `langgraph.json`) that specifies the dependencies, graphs, environment variables to use for the application.
2. The [graphs](https://langchain-ai.github.io/langgraph/concepts/application_structure/#graphs) that implement the logic of the application.
3. A file that specifies [dependencies](https://langchain-ai.github.io/langgraph/concepts/application_structure/#dependencies) required to run the application.
4. [Environment variable](https://langchain-ai.github.io/langgraph/concepts/application_structure/#environment-variables) that are required for the application to run.

## File Structure [¶](https://langchain-ai.github.io/langgraph/concepts/application_structure/\#file-structure "Permanent link")

Below are examples of directory structures for Python and JavaScript applications:

[Python (requirements.txt)](https://langchain-ai.github.io/langgraph/concepts/application_structure/#__tabbed_1_1)[Python (pyproject.toml)](https://langchain-ai.github.io/langgraph/concepts/application_structure/#__tabbed_1_2)[JS (package.json)](https://langchain-ai.github.io/langgraph/concepts/application_structure/#__tabbed_1_3)

```md-code__content
my-app/
├── my_agent # all project code lies within here
│   ├── utils # utilities for your graph
│   │   ├── __init__.py
│   │   ├── tools.py # tools for your graph
│   │   ├── nodes.py # node functions for you graph
│   │   └── state.py # state definition of your graph
│   ├── __init__.py
│   └── agent.py # code for constructing your graph
├── .env # environment variables
├── requirements.txt # package dependencies
└── langgraph.json # configuration file for LangGraph

```

```md-code__content
my-app/
├── my_agent # all project code lies within here
│   ├── utils # utilities for your graph
│   │   ├── __init__.py
│   │   ├── tools.py # tools for your graph
│   │   ├── nodes.py # node functions for you graph
│   │   └── state.py # state definition of your graph
│   ├── __init__.py
│   └── agent.py # code for constructing your graph
├── .env # environment variables
├── langgraph.json  # configuration file for LangGraph
└── pyproject.toml # dependencies for your project

```

```md-code__content
my-app/
├── src # all project code lies within here
│   ├── utils # optional utilities for your graph
│   │   ├── tools.ts # tools for your graph
│   │   ├── nodes.ts # node functions for you graph
│   │   └── state.ts # state definition of your graph
│   └── agent.ts # code for constructing your graph
├── package.json # package dependencies
├── .env # environment variables
└── langgraph.json # configuration file for LangGraph

```

Note

The directory structure of a LangGraph application can vary depending on the programming language and the package manager used.

## Configuration File [¶](https://langchain-ai.github.io/langgraph/concepts/application_structure/\#configuration-file "Permanent link")

The `langgraph.json` file is a JSON file that specifies the dependencies, graphs, environment variables, and other settings required to deploy a LangGraph application.

The file supports specification of the following information:

| Key | Description |
| --- | --- |
| `dependencies` | **Required**. Array of dependencies for LangGraph API server. Dependencies can be one of the following: (1) `"."`, which will look for local Python packages, (2) `pyproject.toml`, `setup.py` or `requirements.txt` in the app directory `"./local_package"`, or (3) a package name. |
| `graphs` | **Required**. Mapping from graph ID to path where the compiled graph or a function that makes a graph is defined. Example: <br>- `./your_package/your_file.py:variable`, where `variable` is an instance of `langgraph.graph.state.CompiledStateGraph`<br>- `./your_package/your_file.py:make_graph`, where `make_graph` is a function that takes a config dictionary ( `langchain_core.runnables.RunnableConfig`) and creates an instance of `langgraph.graph.state.StateGraph` / `langgraph.graph.state.CompiledStateGraph`. |
| `env` | Path to `.env` file or a mapping from environment variable to its value. |
| `python_version` | `3.11` or `3.12`. Defaults to `3.11`. |
| `pip_config_file` | Path to `pip` config file. |
| `dockerfile_lines` | Array of additional lines to add to Dockerfile following the import from parent image. |

Tip

The LangGraph CLI defaults to using the configuration file **langgraph.json** in the current directory.

### Examples [¶](https://langchain-ai.github.io/langgraph/concepts/application_structure/\#examples "Permanent link")

[Python](https://langchain-ai.github.io/langgraph/concepts/application_structure/#__tabbed_2_1)[JavaScript](https://langchain-ai.github.io/langgraph/concepts/application_structure/#__tabbed_2_2)

- The dependencies involve a custom local package and the `langchain_openai` package.
- A single graph will be loaded from the file `./your_package/your_file.py` with the variable `variable`.
- The environment variables are loaded from the `.env` file.

```md-code__content
{
    "dependencies": [\
        "langchain_openai",\
        "./your_package"\
    ],
    "graphs": {
        "my_agent": "./your_package/your_file.py:agent"
    },
    "env": "./.env"
}

```

- The dependencies will be loaded from a dependency file in the local directory (e.g., `package.json`).
- A single graph will be loaded from the file `./your_package/your_file.js` with the function `agent`.
- The environment variable `OPENAI_API_KEY` is set inline.

```md-code__content
{
    "dependencies": [\
        "."\
    ],
    "graphs": {
        "my_agent": "./your_package/your_file.js:agent"
    },
    "env": {
        "OPENAI_API_KEY": "secret-key"
    }
}

```

## Dependencies [¶](https://langchain-ai.github.io/langgraph/concepts/application_structure/\#dependencies "Permanent link")

A LangGraph application may depend on other Python packages or JavaScript libraries (depending on the programming language in which the application is written).

You will generally need to specify the following information for dependencies to be set up correctly:

1. A file in the directory that specifies the dependencies (e.g., `requirements.txt`, `pyproject.toml`, or `package.json`).
2. A `dependencies` key in the [LangGraph configuration file](https://langchain-ai.github.io/langgraph/concepts/application_structure/#configuration-file) that specifies the dependencies required to run the LangGraph application.
3. Any additional binaries or system libraries can be specified using `dockerfile_lines` key in the [LangGraph configuration file](https://langchain-ai.github.io/langgraph/concepts/application_structure/#configuration-file).

## Graphs [¶](https://langchain-ai.github.io/langgraph/concepts/application_structure/\#graphs "Permanent link")

Use the `graphs` key in the [LangGraph configuration file](https://langchain-ai.github.io/langgraph/concepts/application_structure/#configuration-file) to specify which graphs will be available in the deployed LangGraph application.

You can specify one or more graphs in the configuration file. Each graph is identified by a name (which should be unique) and a path for either: (1) the compiled graph or (2) a function that makes a graph is defined.

## Environment Variables [¶](https://langchain-ai.github.io/langgraph/concepts/application_structure/\#environment-variables "Permanent link")

If you're working with a deployed LangGraph application locally, you can configure environment variables in the `env` key of the [LangGraph configuration file](https://langchain-ai.github.io/langgraph/concepts/application_structure/#configuration-file).

For a production deployment, you will typically want to configure the environment variables in the deployment environment.

## Related [¶](https://langchain-ai.github.io/langgraph/concepts/application_structure/\#related "Permanent link")

Please see the following resources for more information:

- How-to guides for [Application Structure](https://langchain-ai.github.io/langgraph/how-tos/#application-structure).

## Comments

giscus

#### [2 reactions](https://github.com/langchain-ai/langgraph/discussions/2509)

👍2

#### [4 comments](https://github.com/langchain-ai/langgraph/discussions/2509)

#### ·

#### 8 replies

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@120215727](https://avatars.githubusercontent.com/u/70314281?v=4)120215727](https://github.com/120215727) [Nov 22, 2024](https://github.com/langchain-ai/langgraph/discussions/2509#discussioncomment-11345938)

great!

1

0 replies

[![@ajakes1](https://avatars.githubusercontent.com/u/33096463?v=4)ajakes1](https://github.com/ajakes1) [Nov 28, 2024](https://github.com/langchain-ai/langgraph/discussions/2509#discussioncomment-11400229)

Is there a way to exclude certain files/directories from being included in the docker image that gets built. For example an excludes field as well as a depdencies field in the LangGraph configuration file?

1

1 reply

[![@Juanchote](https://avatars.githubusercontent.com/u/5665529?u=62434aacaf552bba7974aa9ca17b4be0c0b0b408&v=4)](https://github.com/Juanchote)

[Juanchote](https://github.com/Juanchote) [Dec 8, 2024](https://github.com/langchain-ai/langgraph/discussions/2509#discussioncomment-11497975)

have you tried to add .dockerignore file to the root folder?

[![@grega913](https://avatars.githubusercontent.com/u/12794627?u=e14d1ef7bc33ce6ffbed5b4445f52aa0f3e6014e&v=4)grega913](https://github.com/grega913) [Jan 3](https://github.com/langchain-ai/langgraph/discussions/2509#discussioncomment-11727643)

Hi, I am on Windows 10. Did go through all the necessary steps mentioned in langchain-academy in this video: [https://www.youtube.com/watch?v=o9CT5ohRHzY&t=149s&ab\_channel=LangChain](https://www.youtube.com/watch?v=o9CT5ohRHzY&t=149s&ab_channel=LangChain)

I am in folder "langchain-academy/module-1/studio" and did pip install "langgraph-cli\["inmen" g==0.1.55".\
\
When I run "langraph dev" the app starts and I am redirected to the "https://smith.langchain.com/studio/thread/...blablabla...baseUrl=http%3A%2F%2F127.0.0.1%3A2024" and see the graph and pretty happy here. But when I submit something through input field - I get this error:\
\
Traceback (most recent call last):\
\
File "c:\\Users\\gs\\Documents\\AI24\\LangChain\_202409\\langchain-academy.venv\\Lib\\site-packages\\uvicorn\\protocols\\http\\httptools\_impl.py", line 409, in run\_asgi\
\
result = await app( # type: ignore\[func-returns-value\]\
\
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
\
File "c:\\Users\\gs\\Documents\\AI24\\LangChain\_202409\\langchain-academy.venv\\Lib\\site-packages\\uvicorn\\middleware\\proxy\_headers.py", line 60, in **call**\
\
return await self.app(scope, receive, send)\
\
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
\
File "c:\\Users\\gs\\Documents\\AI24\\LangChain\_202409\\langchain-academy.venv\\Lib\\site-packages\\starlette\\applications.py", line 112, in **call**\
\
await self.middleware\_stack(scope, receive, send)\
\
File "c:\\Users\\gs\\Documents\\AI24\\LangChain\_202409\\langchain-academy.venv\\Lib\\site-packages\\starlette\\middleware\\errors.py", line 187, in **call**\
\
raise exc\
\
File "c:\\Users\\gs\\Documents\\AI24\\LangChain\_202409\\langchain-academy.venv\\Lib\\site-packages\\starlette\\middleware\\errors.py", line 165, in **call**\
\
await self.app(scope, receive, \_send)\
\
File "c:\\Users\\gs\\Documents\\AI24\\LangChain\_202409\\langchain-academy.venv\\Lib\\site-packages\\starlette\\middleware\\cors.py", line 93, in **call**\
\
await self.simple\_response(scope, receive, send, request\_headers=headers)\
\
File "c:\\Users\\gs\\Documents\\AI24\\LangChain\_202409\\langchain-academy.venv\\Lib\\site-packages\\starlette\\middleware\\cors.py", line 144, in simple\_response\
\
await self.app(scope, receive, send)\
\
File "c:\\Users\\gs\\Documents\\AI24\\LangChain\_202409\\langchain-academy.venv\\Lib\\site-packages\\starlette\\middleware\\base.py", line 176, in **call**\
\
with recv\_stream, send\_stream, collapse\_excgroups():\
\
File "C:\\Python312\\Lib\\contextlib.py", line 158, in **exit**\
\
self.gen.throw(value)\
\
File "c:\\Users\\gs\\Documents\\AI24\\LangChain\_202409\\langchain-academy.venv\\Lib\\site-packages\\starlette\_utils.py", line 82, in collapse\_excgroups\
\
raise exc\
\
File "c:\\Users\\gs\\Documents\\AI24\\LangChain\_202409\\langchain-academy.venv\\Lib\\site-packages\\langgraph\_api\\base\\shared\\sse.py", line 36, in **call**\
\
task\_group.start\_soon(wrap, self.listen\_for\_exit\_signal)\
\
^^^^^^^^^^^^^^^^^^^^^^^^^^^\
\
AttributeError: 'EventSourceResponse' object has no attribute 'listen\_for\_exit\_signal'. Did you mean: '\_listen\_for\_exit\_signal'?\
\
Do you have any idea what is the problem?\
\
2\
\
1 reply\
\
[![@grega913](https://avatars.githubusercontent.com/u/12794627?u=e14d1ef7bc33ce6ffbed5b4445f52aa0f3e6014e&v=4)](https://github.com/grega913)\
\
[grega913](https://github.com/grega913) [Jan 3](https://github.com/langchain-ai/langgraph/discussions/2509#discussioncomment-11727776)\
\
OK, I solved this by modifying 2 lines in .venv\\Lib\\site-packages\\langgraph\_api\\base\\shared\\sse.py:\
\
line 36: task\_group.start\_soon(wrap, self.listen\_for\_exit\_signal) -> task\_group.start\_soon(wrap, self.\_listen\_for\_exit\_signal)\
\
line 41: await wrap(partial(self.listen\_for\_disconnect, receive)) -> await wrap(partial(self.\_listen\_for\_disconnect, receive))\
\
this solved it for me\
\
[![@martinobettucci](https://avatars.githubusercontent.com/u/19490374?u=5ae0113e9348bf2bc0851c804bc4b3ddbf84c1c4&v=4)martinobettucci](https://github.com/martinobettucci) [Jan 7](https://github.com/langchain-ai/langgraph/discussions/2509#discussioncomment-11761178)\
\
I am sorry but this nukes completely the usefulness this way for researchers:\
\
first of all, how am I supposed to know what's the content of the json? why do I have to create a nth-way of declaring dependencies when I already have my environment? why do I have to specify the dependencies at all again? why my graphs are required to be a python script? Could it not run like an IPython instance inside my already running environment? I can't test run my jupyter notebooks this way, I can't use conda environment.. anyway, this is completely useless the way it is for anyone wanting to do scientific LLM as plain python script is simply not the reality.\
\
1\
\
6 replies\
\
Show 1 previous reply\
\
[![@martinobettucci](https://avatars.githubusercontent.com/u/19490374?u=5ae0113e9348bf2bc0851c804bc4b3ddbf84c1c4&v=4)](https://github.com/martinobettucci)\
\
[martinobettucci](https://github.com/martinobettucci) [Jan 9](https://github.com/langchain-ai/langgraph/discussions/2509#discussioncomment-11788445)\
\
First of all, thank you for answering and trying to help. good vibes to you Juanchote.\
\
So, I would like to try to launch langraph studio webui to debug an instance of a graph I built inside a notebook and because it asks to create a langraph.json file to run the langgraph dev... tipycally to launch a studio dev or built a docker for the studio to run, you have to provide a langraph.json (unless the doc is as broken as usual) like this:\
\
{\
\
"dependencies": \[\
\
"."\
\
\],\
\
"graphs": {\
\
"invoke\_chat": "./invoke\_chat.py:invoke\_chat"\
\
},\
\
"env": ".env"\
\
}\
\
where "invoke\_chat" is the name of the compiled graph that should be contained in some .py file.\
\
The problemS are (there is at least one problem per line required), I DON'T HAVE a .env file because my vars are declared inside my jupyter environment or inside the secret enclave of the python interpreter which you know, I DON'T WANT to export. I DON'T HAVE the graph in a dedicate python script because my agents are spread in multiple cells all around the notebook and there is no easy way to compile a stand alone python script without copy/paste back and forth between my notebook and the file which is error prone completely nuking the usefulness of debugging. I DON'T have a dependency list because the IPythons environments depends by the python server which are pre-built most of the time.\
\
If you have any idea, I'm open ears of course! :)\
\
[![@hinthornw](https://avatars.githubusercontent.com/u/13333726?u=82ebf1e0eb0663ebd49ba66f67a43f51bbf11442&v=4)](https://github.com/hinthornw)\
\
[hinthornw](https://github.com/hinthornw) [Jan 9](https://github.com/langchain-ai/langgraph/discussions/2509#discussioncomment-11788572)\
\
Contributor\
\
> The problemS are (there is at least one problem per line required), I DON'T HAVE a .env file because my vars are declared inside my jupyter environment or inside the secret enclave of the python interpreter which you know, I DON'T WANT to export.\
\
1. If you are just running locally with `langgraph dev`, you can omit the env line. It will use your interpreter environment. The `env` config is used if you are running in docker.\
\
> I DON'T HAVE the graph in a dedicate python script because my agents are spread in multiple cells all around the notebook and there is no easy way to compile a stand alone python script without copy/paste back and forth between my notebook and the file which is error prone completely nuking the usefulness of debugging.\
\
2. You could use `nbconvert` or jupytext to export to a python file, though you would want to remove extraneous calls. This is a server environment so it's not that common to run from a notebook. Are there other production web server frameworks that you've found work well in notebooks that you'd suggest we study?\
\
> I DON'T have a dependency list because the IPythons environments depends by the python server which are pre-built most of the time.\
\
3. (same as in (1) Deps in `langgraph dev` in-mem server just use your local environment. Deps are used for docker and production deployment.\
\
[![@Juanchote](https://avatars.githubusercontent.com/u/5665529?u=62434aacaf552bba7974aa9ca17b4be0c0b0b408&v=4)](https://github.com/Juanchote)\
\
[Juanchote](https://github.com/Juanchote) [Jan 9](https://github.com/langchain-ai/langgraph/discussions/2509#discussioncomment-11788606)\
\
I see, let me explain to you what my workflow looks like, I see we mostly use the same tools but in a very different way. My background is webdevelopment, mostly backend/devops so I guess I am more familiar with some of the toolings related to the langgraph platform itself. I am not saying here you need to change your way of working in your development environment, just sharing how I do it which seems to be more aligned with langgraph team than your way.\
\
I don't think having env vars hardcoded in your JN are a good practice, specially if at some point you plan to share the JN with someone, I use python-dotenv and I have in the first cell of my JN this:\
\
```notranslate\
from dotenv import load_dotenv\
load_dotenv(override=True)\
\
```\
\
now I share the same .env between my webserver and JN without exposing the variables in case I want to push my project to github.\
\
I think the main issue here is the mix of JN and a webserver. a webserver doesn't work with JN, JN are for experimenting fast but you cannot deploy JN to a webserver and expect an API to use the code in there. The code needs to be in python files if you want the webserver to be able to read and use the code, that is how webservers work, and it is what langgraph cli does, spins up a set of dockers with a webserver with an api for you to use.\
\
in my case, I use jupyter notebook for assembling my workflows, classes, code, etc, so I can iterate faster the logic, once I have a workflow that works, I move the code to their py files, and they are ready for e2e testing or deployment to the cloud, but the JN are for fast local development.\
\
What langgraph cli is doing under the hood is creating a docker container with your code in it, but in order to work, it needs to recreate your venv inside the container and the only way to do that is by a requirement.txt because is the best practice when working with docker container. It is a package manager with isolated system. It is like a VM.\
\
At leat in conda you can do\
\
`conda list -e > requirements.txt `\
\
and it will create the requirements.txt based on the actual env, so not a big deal, just remember to run that from time to time whenever you add new dependencies.\
\
Now, to be fair, I tried the langraph server and I don't like it because I found it too green and rigid and not good enough for the stuff I need to do and I just use my own fastapi server to run the agents.\
\
[![@martinobettucci](https://avatars.githubusercontent.com/u/19490374?u=5ae0113e9348bf2bc0851c804bc4b3ddbf84c1c4&v=4)](https://github.com/martinobettucci)\
\
[martinobettucci](https://github.com/martinobettucci) [Jan 9](https://github.com/langchain-ai/langgraph/discussions/2509#discussioncomment-11788735)\
\
Thank you Juanchote, thank you hinthornw.\
\
I get that for production you want to have an isolated environment, we also deploy in dockerized apps but during development, it is a very common and convenient way to develop your agents and llm inside notebook. The studio requires a production compliant environment, I get it, simply this is impractical because the studio is for debugging AFAIK.\
\
Cool for the environment variables, nice to know: that should be added in the doc of course.\
\
As per the exporting the notebook, this is also impractical, what would be great is for the studio to be integrated into the running IPython instance so we can change the code and update the references between the notebook, add breakpoints, .... while observing the graph responding in the convenient Studio UI.\
\
What we do, for now, we implemented the listener at the langchain layer and we output everything in a file (like a logger). It works but...it is a pity a Studio Dev environment exists and do not use the dev environment.\
\
my 2ct\
\
[![@martinobettucci](https://avatars.githubusercontent.com/u/19490374?u=5ae0113e9348bf2bc0851c804bc4b3ddbf84c1c4&v=4)](https://github.com/martinobettucci)\
\
[martinobettucci](https://github.com/martinobettucci) [Jan 9](https://github.com/langchain-ai/langgraph/discussions/2509#discussioncomment-11792071)\
\
Ok, I've managed to make it work but it is a mess: the studio framework is a mess, honestly.\
\
I've retrospected the code starting from the graph name using ASTOS and exported dynamically the code to a python script which is updated from my IPython execution engine via a listener added to the zero-mq that runs the commands between the notebook and the python instance server (this is the way jupyter actually works). In simple words, when I execute the code on the notebook and if the code is used by my graph detected by an acyclic reference of symbol extracted from the running abstract syntax tree of executed cells, it updates the python script accordingly. I generate dynamically a project folder with the **init**.py (another important info the doc failed to pass on _how_ the dev server loads the graph referenced in the json. About the requirements.txt, I use the pip module api to retrieve the packages with their version to generate a file and for the .env is not required because I confirm current environment work but I have to run the langraph dev inside the notebook kernel.. but it works so its fine for this.\
\
After that, I have wrote a flask server managing à ngrok proxy because it is IMPOSSIBLE thanks to the CORS to connect a https page like smith.langchain.com to a http pointing to local resources like 127.0.0.1 !\
\
The flask server add the cors policy and proxy all requests back to the local langraph studio dev instance which handle the calls.\
\
I am sure there is a better way like, letting the studio be self hosted for exemple instead of forcing to use the [https://smith.langchain.com/](https://smith.langchain.com/) instance. Also a self hosted solution could "catch" the zero-mq method directly as to runs live code instead of static code from a file.\
\
WritePreview\
\
[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")\
\
[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fconcepts%2Fapplication_structure%2F)