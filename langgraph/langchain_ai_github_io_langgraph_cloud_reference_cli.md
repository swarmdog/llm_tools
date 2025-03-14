[Skip to content](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#langgraph-cli)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/reference/cli.md "Edit this page")

# LangGraph CLI [¶](https://langchain-ai.github.io/langgraph/cloud/reference/cli/\#langgraph-cli "Permanent link")

The LangGraph command line interface includes commands to build and run a LangGraph Cloud API server locally in [Docker](https://www.docker.com/). For development and testing, you can use the CLI to deploy a local API server.

## Installation [¶](https://langchain-ai.github.io/langgraph/cloud/reference/cli/\#installation "Permanent link")

1. Ensure that Docker is installed (e.g. `docker --version`).
2. Install the CLI package:



[Python](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_1_1)[JS](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_1_2)









```md-code__content
pip install langgraph-cli

# Install via Homebrew
brew install langgraph-cli

```











```md-code__content
npx @langchain/langgraph-cli

# Install globally, will be available as `langgraphjs`
npm install -g @langchain/langgraph-cli

```

3. Run the command `langgraph --help` or `npx @langchain/langgraph-cli --help` to confirm that the CLI is working correctly.


## Configuration File [¶](https://langchain-ai.github.io/langgraph/cloud/reference/cli/\#configuration-file "Permanent link")

The LangGraph CLI requires a JSON configuration file with the following keys:

Note

The LangGraph CLI defaults to using the configuration file **langgraph.json** in the current directory.


[Python](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_2_1)[JS](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_2_2)

| Key | Description |
| --- | --- |
| `dependencies` | **Required**. Array of dependencies for LangGraph Cloud API server. Dependencies can be one of the following: (1) `"."`, which will look for local Python packages, (2) `pyproject.toml`, `setup.py` or `requirements.txt` in the app directory `"./local_package"`, or (3) a package name. |
| `graphs` | **Required**. Mapping from graph ID to path where the compiled graph or a function that makes a graph is defined. Example: <br>- `./your_package/your_file.py:variable`, where `variable` is an instance of `langgraph.graph.state.CompiledStateGraph`<br>- `./your_package/your_file.py:make_graph`, where `make_graph` is a function that takes a config dictionary ( `langchain_core.runnables.RunnableConfig`) and creates an instance of `langgraph.graph.state.StateGraph` / `langgraph.graph.state.CompiledStateGraph`. |
| `auth` | _(Added in v0.0.11)_ Auth configuration containing the path to your authentication handler. Example: `./your_package/auth.py:auth`, where `auth` is an instance of `langgraph_sdk.Auth`. See [authentication guide](https://langchain-ai.github.io/langgraph/concepts/auth/) for details. |
| `env` | Path to `.env` file or a mapping from environment variable to its value. |
| `store` | Configuration for adding semantic search to the BaseStore. Contains the following fields: <br>- `index`: Configuration for semantic search indexing with fields:<br>  - `embed`: Embedding provider (e.g., "openai:text-embedding-3-small") or path to custom embedding function<br>  - `dims`: Dimension size of the embedding model. Used to initialize the vector table.<br>  - `fields` (optional): List of fields to index. Defaults to `["$"]`, which means to index entire documents. Can be specific fields like `["text", "summary", "some.value"]` |
| `python_version` | `3.11` or `3.12`. Defaults to `3.11`. |
| `node_version` | Specify `node_version: 20` to use LangGraph.js. |
| `pip_config_file` | Path to `pip` config file. |
| `dockerfile_lines` | Array of additional lines to add to Dockerfile following the import from parent image. |
| `http` | HTTP server configuration with the following fields: <br>- `app`: Path to custom Starlette/FastAPI app (e.g., `"./src/agent/webapp.py:app"`). See [custom routes guide](https://langchain-ai.github.io/langgraph/how-tos/http/custom_routes/).<br>- `disable_assistants`: Disable `/assistants` routes<br>- `disable_threads`: Disable `/threads` routes<br>- `disable_runs`: Disable `/runs` routes<br>- `disable_store`: Disable `/store` routes<br>- `disable_meta`: Disable `/ok`, `/info`, `/metrics`, and `/docs` routes<br>- `cors`: CORS configuration with fields for `allow_origins`, `allow_methods`, `allow_headers`, etc. |

| Key | Description |
| --- | --- |
| `graphs` | **Required**. Mapping from graph ID to path where the compiled graph or a function that makes a graph is defined. Example: <br>- `./src/graph.ts:variable`, where `variable` is an instance of `CompiledStateGraph`<br>- `./src/graph.ts:makeGraph`, where `makeGraph` is a function that takes a config dictionary ( `LangGraphRunnableConfig`) and creates an instance of `StateGraph` / `CompiledStateGraph`. |
| `env` | Path to `.env` file or a mapping from environment variable to its value. |
| `store` | Configuration for adding semantic search to the BaseStore. Contains the following fields: <br>- `index`: Configuration for semantic search indexing with fields:<br>  - `embed`: Embedding provider (e.g., "openai:text-embedding-3-small") or path to custom embedding function<br>  - `dims`: Dimension size of the embedding model. Used to initialize the vector table.<br>  - `fields` (optional): List of fields to index. Defaults to `["$"]`, which means to index entire documents. Can be specific fields like `["text", "summary", "some.value"]` |
| `node_version` | Specify `node_version: 20` to use LangGraph.js. |
| `dockerfile_lines` | Array of additional lines to add to Dockerfile following the import from parent image. |

### Examples [¶](https://langchain-ai.github.io/langgraph/cloud/reference/cli/\#examples "Permanent link")

[Python](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_3_1)[JS](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_3_2)

#### Basic Configuration [¶](https://langchain-ai.github.io/langgraph/cloud/reference/cli/\#basic-configuration "Permanent link")

```md-code__content
{
  "dependencies": ["."],
  "graphs": {
    "chat": "./chat/graph.py:graph"
  }
}

```

#### Adding semantic search to the store [¶](https://langchain-ai.github.io/langgraph/cloud/reference/cli/\#adding-semantic-search-to-the-store "Permanent link")

All deployments come with a DB-backed BaseStore. Adding an "index" configuration to your `langgraph.json` will enable [semantic search](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/) within the BaseStore of your deployment.

The `fields` configuration determines which parts of your documents to embed:

- If omitted or set to `["$"]`, the entire document will be embedded
- To embed specific fields, use JSON path notation: `["metadata.title", "content.text"]`
- Documents missing specified fields will still be stored but won't have embeddings for those fields
- You can still override which fields to embed on a specific item at `put` time using the `index` parameter

```md-code__content
{
  "dependencies": ["."],
  "graphs": {
    "memory_agent": "./agent/graph.py:graph"
  },
  "store": {
    "index": {
      "embed": "openai:text-embedding-3-small",
      "dims": 1536,
      "fields": ["$"]
    }
  }
}

```

Common model dimensions

- `openai:text-embedding-3-large`: 3072
- `openai:text-embedding-3-small`: 1536
- `openai:text-embedding-ada-002`: 1536
- `cohere:embed-english-v3.0`: 1024
- `cohere:embed-english-light-v3.0`: 384
- `cohere:embed-multilingual-v3.0`: 1024
- `cohere:embed-multilingual-light-v3.0`: 384

#### Semantic search with a custom embedding function [¶](https://langchain-ai.github.io/langgraph/cloud/reference/cli/\#semantic-search-with-a-custom-embedding-function "Permanent link")

If you want to use semantic search with a custom embedding function, you can pass a path to a custom embedding function:

```md-code__content
{
  "dependencies": ["."],
  "graphs": {
    "memory_agent": "./agent/graph.py:graph"
  },
  "store": {
    "index": {
      "embed": "./embeddings.py:embed_texts",
      "dims": 768,
      "fields": ["text", "summary"]
    }
  }
}

```

The `embed` field in store configuration can reference a custom function that takes a list of strings and returns a list of embeddings. Example implementation:

```md-code__content
# embeddings.py
def embed_texts(texts: list[str]) -> list[list[float]]:
    """Custom embedding function for semantic search."""
    # Implementation using your preferred embedding model
    return [[0.1, 0.2, ...] for _ in texts]  # dims-dimensional vectors

```

#### Adding custom authentication [¶](https://langchain-ai.github.io/langgraph/cloud/reference/cli/\#adding-custom-authentication "Permanent link")

```md-code__content
{
  "dependencies": ["."],
  "graphs": {
    "chat": "./chat/graph.py:graph"
  },
  "auth": {
    "path": "./auth.py:auth",
    "openapi": {
      "securitySchemes": {
        "apiKeyAuth": {
          "type": "apiKey",
          "in": "header",
          "name": "X-API-Key"
        }
      },
      "security": [{ "apiKeyAuth": [] }]
    },
    "disable_studio_auth": false
  }
}

```

See the [authentication conceptual guide](https://langchain-ai.github.io/langgraph/concepts/auth/) for details, and the [setting up custom authentication](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/) guide for a practical walk through of the process.

#### Basic Configuration [¶](https://langchain-ai.github.io/langgraph/cloud/reference/cli/\#basic-configuration_1 "Permanent link")

```md-code__content
{
  "graphs": {
    "chat": "./src/graph.ts:graph"
  }
}

```

## Commands [¶](https://langchain-ai.github.io/langgraph/cloud/reference/cli/\#commands "Permanent link")

**Usage**

[Python](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_4_1)[JS](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_4_2)

The base command for the LangGraph CLI is `langgraph`.

```md-code__content
langgraph [OPTIONS] COMMAND [ARGS]

```

The base command for the LangGraph.js CLI is `langgraphjs`.

```md-code__content
npx @langchain/langgraph-cli [OPTIONS] COMMAND [ARGS]

```

We recommend using `npx` to always use the latest version of the CLI.

### `dev` [¶](https://langchain-ai.github.io/langgraph/cloud/reference/cli/\#dev "Permanent link")

[Python](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_5_1)[JS](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_5_2)

Run LangGraph API server in development mode with hot reloading and debugging capabilities. This lightweight server requires no Docker installation and is suitable for development and testing. State is persisted to a local directory.

Note

Currently, the CLI only supports Python >= 3.11.

**Installation**

This command requires the "inmem" extra to be installed:

```md-code__content
pip install -U "langgraph-cli[inmem]"

```

**Usage**

```md-code__content
langgraph dev [OPTIONS]

```

**Options**

| Option | Default | Description |
| --- | --- | --- |
| `-c, --config FILE` | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables |
| `--host TEXT` | `127.0.0.1` | Host to bind the server to |
| `--port INTEGER` | `2024` | Port to bind the server to |
| `--no-reload` |  | Disable auto-reload |
| `--n-jobs-per-worker INTEGER` |  | Number of jobs per worker. Default is 10 |
| `--debug-port INTEGER` |  | Port for debugger to listen on |
| `--help` |  | Display command documentation |

Run LangGraph API server in development mode with hot reloading capabilities. This lightweight server requires no Docker installation and is suitable for development and testing. State is persisted to a local directory.

**Usage**

```md-code__content
npx @langchain/langgraph-cli dev [OPTIONS]

```

**Options**

| Option | Default | Description |
| --- | --- | --- |
| `-c, --config FILE` | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables |
| `--host TEXT` | `127.0.0.1` | Host to bind the server to |
| `--port INTEGER` | `2024` | Port to bind the server to |
| `--no-reload` |  | Disable auto-reload |
| `--n-jobs-per-worker INTEGER` |  | Number of jobs per worker. Default is 10 |
| `--debug-port INTEGER` |  | Port for debugger to listen on |
| `--help` |  | Display command documentation |

### `build` [¶](https://langchain-ai.github.io/langgraph/cloud/reference/cli/\#build "Permanent link")

[Python](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_6_1)[JS](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_6_2)

Build LangGraph Cloud API server Docker image.

**Usage**

```md-code__content
langgraph build [OPTIONS]

```

**Options**

| Option | Default | Description |
| --- | --- | --- |
| `--platform TEXT` |  | Target platform(s) to build the Docker image for. Example: `langgraph build --platform linux/amd64,linux/arm64` |
| `-t, --tag TEXT` |  | **Required**. Tag for the Docker image. Example: `langgraph build -t my-image` |
| `--pull / --no-pull` | `--pull` | Build with latest remote Docker image. Use `--no-pull` for running the LangGraph Cloud API server with locally built images. |
| `-c, --config FILE` | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables. |
| `--help` |  | Display command documentation. |

Build LangGraph Cloud API server Docker image.

**Usage**

```md-code__content
npx @langchain/langgraph-cli build [OPTIONS]

```

**Options**

| Option | Default | Description |
| --- | --- | --- |
| `--platform TEXT` |  | Target platform(s) to build the Docker image for. Example: `langgraph build --platform linux/amd64,linux/arm64` |
| `-t, --tag TEXT` |  | **Required**. Tag for the Docker image. Example: `langgraph build -t my-image` |
| `--no-pull` |  | Use locally built images. Defaults to `false` to build with latest remote Docker image. |
| `-c, --config FILE` | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables. |
| `--help` |  | Display command documentation. |

### `up` [¶](https://langchain-ai.github.io/langgraph/cloud/reference/cli/\#up "Permanent link")

[Python](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_7_1)[JS](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_7_2)

Start LangGraph API server. For local testing, requires a LangSmith API key with access to LangGraph Cloud closed beta. Requires a license key for production use.

**Usage**

```md-code__content
langgraph up [OPTIONS]

```

**Options**

| Option | Default | Description |
| --- | --- | --- |
| `--wait` |  | Wait for services to start before returning. Implies --detach |
| `--postgres-uri TEXT` | Local database | Postgres URI to use for the database. |
| `--watch` |  | Restart on file changes |
| `--debugger-base-url TEXT` | `http://127.0.0.1:[PORT]` | URL used by the debugger to access LangGraph API. |
| `--debugger-port INTEGER` |  | Pull the debugger image locally and serve the UI on specified port |
| `--verbose` |  | Show more output from the server logs. |
| `-c, --config FILE` | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables. |
| `-d, --docker-compose FILE` |  | Path to docker-compose.yml file with additional services to launch. |
| `-p, --port INTEGER` | `8123` | Port to expose. Example: `langgraph up --port 8000` |
| `--pull / --no-pull` | `pull` | Pull latest images. Use `--no-pull` for running the server with locally-built images. Example: `langgraph up --no-pull` |
| `--recreate / --no-recreate` | `no-recreate` | Recreate containers even if their configuration and image haven't changed |
| `--help` |  | Display command documentation. |

Start LangGraph API server. For local testing, requires a LangSmith API key with access to LangGraph Cloud closed beta. Requires a license key for production use.

**Usage**

```md-code__content
npx @langchain/langgraph-cli up [OPTIONS]

```

**Options**

| Option | Default | Description |
| --- | --- | --- |
| `--wait` |  | Wait for services to start before returning. Implies --detach |
| `--postgres-uri TEXT` | Local database | Postgres URI to use for the database. |
| `--watch` |  | Restart on file changes |
| `-c, --config FILE` | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables. |
| `-d, --docker-compose FILE` |  | Path to docker-compose.yml file with additional services to launch. |
| `-p, --port INTEGER` | `8123` | Port to expose. Example: `langgraph up --port 8000` |
| `--no-pull` |  | Use locally built images. Defaults to `false` to build with latest remote Docker image. |
| `--recreate` |  | Recreate containers even if their configuration and image haven't changed |
| `--help` |  | Display command documentation. |

### `dockerfile` [¶](https://langchain-ai.github.io/langgraph/cloud/reference/cli/\#dockerfile "Permanent link")

[Python](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_8_1)[JS](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#__tabbed_8_2)

Generate a Dockerfile for building a LangGraph Cloud API server Docker image.

**Usage**

```md-code__content
langgraph dockerfile [OPTIONS] SAVE_PATH

```

**Options**

| Option | Default | Description |
| --- | --- | --- |
| `-c, --config FILE` | `langgraph.json` | Path to the [configuration file](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file) declaring dependencies, graphs and environment variables. |
| `--help` |  | Show this message and exit. |

Example:

```md-code__content
langgraph dockerfile -c langgraph.json Dockerfile

```

This generates a Dockerfile that looks similar to:

```md-code__content
FROM langchain/langgraph-api:3.11

ADD ./pipconf.txt /pipconfig.txt

RUN PIP_CONFIG_FILE=/pipconfig.txt PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -c /api/constraints.txt langchain_community langchain_anthropic langchain_openai wikipedia scikit-learn

ADD ./graphs /deps/__outer_graphs/src
RUN set -ex && \
    for line in '[project]' \
                'name = "graphs"' \
                'version = "0.1"' \
                '[tool.setuptools.package-data]' \
                '"*" = ["**/*"]'; do \
        echo "$line" >> /deps/__outer_graphs/pyproject.toml; \
    done

RUN PIP_CONFIG_FILE=/pipconfig.txt PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -c /api/constraints.txt -e /deps/*

ENV LANGSERVE_GRAPHS='{"agent": "/deps/__outer_graphs/src/agent.py:graph", "storm": "/deps/__outer_graphs/src/storm.py:graph"}'

```

Updating your langgraph.json file

The `langgraph dockerfile` command translates all the configuration in your `langgraph.json` file into Dockerfile commands. When using this command, you will have to re-run it whenever you update your `langgraph.json` file. Otherwise, your changes will not be reflected when you build or run the dockerfile.

Generate a Dockerfile for building a LangGraph Cloud API server Docker image.

**Usage**

```md-code__content
npx @langchain/langgraph-cli dockerfile [OPTIONS] SAVE_PATH

```

**Options**

| Option | Default | Description |
| --- | --- | --- |
| `-c, --config FILE` | `langgraph.json` | Path to the [configuration file](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file) declaring dependencies, graphs and environment variables. |
| `--help` |  | Show this message and exit. |

Example:

```md-code__content
npx @langchain/langgraph-cli dockerfile -c langgraph.json Dockerfile

```

This generates a Dockerfile that looks similar to:

```md-code__content
FROM langchain/langgraphjs-api:20

ADD . /deps/agent

RUN cd /deps/agent && yarn install

ENV LANGSERVE_GRAPHS='{"agent":"./src/react_agent/graph.ts:graph"}'

WORKDIR /deps/agent

RUN (test ! -f /api/langgraph_api/js/build.mts && echo "Prebuild script not found, skipping") || tsx /api/langgraph_api/js/build.mts

```

Updating your langgraph.json file

The `npx @langchain/langgraph-cli dockerfile` command translates all the configuration in your `langgraph.json` file into Dockerfile commands. When using this command, you will have to re-run it whenever you update your `langgraph.json` file. Otherwise, your changes will not be reflected when you build or run the dockerfile.

## Comments

giscus

#### [5 reactions](https://github.com/langchain-ai/langgraph/discussions/1217)

🚀5

#### [16 comments](https://github.com/langchain-ai/langgraph/discussions/1217)

#### ·

#### 11 replies

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@gedion](https://avatars.githubusercontent.com/u/1224206?u=822e3f09394730a5e8f41fe5100df495a9438386&v=4)gedion](https://github.com/gedion) [Aug 4, 2024](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-10237096)

When can we expect TypeScript support?

1

👍2

4 replies

[![@hwchase17](https://avatars.githubusercontent.com/u/11986836?u=f4c4f21a82b2af6c9f91e1f1d99ea40062f7a101&v=4)](https://github.com/hwchase17)

[hwchase17](https://github.com/hwchase17) [Aug 5, 2024](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-10243908)

Contributor

hopefully late this month

👍3❤️1🚀1

[![@SaroAntonelloLovito](https://avatars.githubusercontent.com/u/91974562?v=4)](https://github.com/SaroAntonelloLovito)

[SaroAntonelloLovito](https://github.com/SaroAntonelloLovito) [Sep 3, 2024](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-10530443)

Will be compatible with Next?

[![@ajasingh](https://avatars.githubusercontent.com/u/15189049?v=4)](https://github.com/ajasingh)

[ajasingh](https://github.com/ajasingh) [Jan 11](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-11805210)

Any update on JS cli

[![@dqbd](https://avatars.githubusercontent.com/u/1443449?u=fe32372ae8f497065ef0a1c54194d9dff36fb81d&v=4)](https://github.com/dqbd)

[dqbd](https://github.com/dqbd) [Jan 18](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-11872630)

Contributor

Hello! We're actively working on a JS port of the CLI and the in-memory server. You can check it out here: [https://www.npmjs.com/package/@langchain/langgraph-cli](https://www.npmjs.com/package/@langchain/langgraph-cli)

[![@hrone-dev-satyammishra](https://avatars.githubusercontent.com/u/175679505?v=4)hrone-dev-satyammishra](https://github.com/hrone-dev-satyammishra) [Aug 7, 2024](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-10264174)

How to get access to langraph cloud? How do I deploy langraph applications to production?

1

👍1

1 reply

[![@eyurtsev](https://avatars.githubusercontent.com/u/3205522?v=4)](https://github.com/eyurtsev)

[eyurtsev](https://github.com/eyurtsev) [Nov 13, 2024](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-11244052)

Contributor

See documentation here: [https://langchain-ai.github.io/langgraph/concepts/deployment\_options/](https://langchain-ai.github.io/langgraph/concepts/deployment_options/)

[![@shunkakinoki](https://avatars.githubusercontent.com/u/39187513?u=01a71324ca76dbcb7c4f57622d5c9dcd254013eb&v=4)shunkakinoki](https://github.com/shunkakinoki) [Aug 7, 2024](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-10267738)

How to get started? Seems like the waitlist form is closed for general availability but can't get access.

1

👍2

1 reply

[![@eyurtsev](https://avatars.githubusercontent.com/u/3205522?v=4)](https://github.com/eyurtsev)

[eyurtsev](https://github.com/eyurtsev) [Nov 13, 2024](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-11244056)

Contributor

See documentation here: [https://langchain-ai.github.io/langgraph/concepts/deployment\_options/](https://langchain-ai.github.io/langgraph/concepts/deployment_options/)

[![@ssmith777](https://avatars.githubusercontent.com/u/46206462?u=9a5fc0b0ca7f1664f7a5fa23a3193ddde55cc9a4&v=4)ssmith777](https://github.com/ssmith777) [Aug 13, 2024](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-10330608)

How can I sign up for access please???

1

0 replies

[![@fletchertyler914](https://avatars.githubusercontent.com/u/3344498?u=be6f2ff193f913fb9b7ad2c9c1c98b6f8eaf93f4&v=4)fletchertyler914](https://github.com/fletchertyler914) [Aug 15, 2024](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-10349438)

Is there a way to have server-side config modification like langserve's `per_req_config_modifier`?

1

1 reply

[![@siddicky](https://avatars.githubusercontent.com/u/44811336?u=6b42d79a6dc9b974e00748c2dbf885cd67d4e4c6&v=4)](https://github.com/siddicky)

[siddicky](https://github.com/siddicky) [Aug 18, 2024](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-10374559)

This!

[![@kvkenyon](https://avatars.githubusercontent.com/u/1572831?u=42c9fcdfe95fda63f1d7a9feca1d572bfab59d12&v=4)kvkenyon](https://github.com/kvkenyon) [Aug 29, 2024](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-10489034)

Is there an explicit way to access your agent message history from a web service?

1

0 replies

[![@majorgilles](https://avatars.githubusercontent.com/u/5008200?v=4)majorgilles](https://github.com/majorgilles) [Nov 15, 2024](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-11266781)

I don't see any way to trigger a revision programmatically on a LangGraph cloud (not self hosted) deployment endpoint. This would be VERY needed as we need to inject tokens dynamically at build time so that we can consume a private AWS CodeArtifact library at build time. Those have a 12h lifecycle.

1

0 replies

[![@bacaxnot](https://avatars.githubusercontent.com/u/90140124?u=ec2e9240f1ea9134856636743060ad948642cce6&v=4)bacaxnot](https://github.com/bacaxnot) [Dec 2, 2024](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-11437654)

is there a way to use this with [sst](https://sst.dev/)...? All my environment variables and setup is built using sst's architecture, and the way to access the environment variables would be to wrap everything with the `sst shell` command.

1

0 replies

[![@DotCSanova](https://avatars.githubusercontent.com/u/177200921?u=535f16dc3707ad10b0487c9327de58bcdb9682f7&v=4)DotCSanova](https://github.com/DotCSanova) [Dec 16, 2024](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-11581548)

Hi all,

Everytime I try to start de Development server with 'langgraph dev' command from my venv, the following error arises: ModuleNotFoundError: No module named 'my\_agent'. I have tried to solve it and the only solution I found which works for me (from Mac and Windows too) is adding the following instruction: 'export PYTHONPATH="/path/to/my/project:$PYTHONPATH"'.

The project includes the required **.init.** files and the langgraph.json is as follows: {

"dependencies": \[\
\
"./my\_agent"\
\
\],

"graphs": {

"agent": "./my\_agent/agent.py:graph"

},

"env": "./varentorno.env"

}

Does anyone why does it happen? I think it is not normal to export the PYTHONPATH each time I create a new project.

Thank you!

1

2 replies

[![@sushi057](https://avatars.githubusercontent.com/u/64535753?u=ef7a681a6ddb0f0c4f45b7298f1ad03e278377c2&v=4)](https://github.com/sushi057)

[sushi057](https://github.com/sushi057) [Jan 16](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-11858523)

Apparently it is. I had a similar issue where even running a new terminal would mean I had to run this command. A quick and easy fix to this is to add the

`export PYTHONPATH="/path/to/my/project:$PYTHONPATH`

to your .bashrc or .zshrc file. This basically adds your project path to the default PYTHONPATH.

[![@DotCSanova](https://avatars.githubusercontent.com/u/177200921?u=535f16dc3707ad10b0487c9327de58bcdb9682f7&v=4)](https://github.com/DotCSanova)

[DotCSanova](https://github.com/DotCSanova) [13 days ago](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-12350220)

[@sushi057](https://github.com/sushi057) Thank you!

I was also able to 'solve' this issue by packaging the project (I created a 'setup.py' file including the line 'packages=find\_packages(),') and installing it locally with 'pip install -e .'. After that, the Development Server ran well.

[![@xtbwqtq](https://avatars.githubusercontent.com/u/146714110?u=c34939f4e6363410681f9342eab4c37ed0a4c376&v=4)xtbwqtq](https://github.com/xtbwqtq) [Jan 16](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-11850135)

What hook functions can be used to perform cleanup after langgraph-cli is shut down?

1

1 reply

[![@eyurtsev](https://avatars.githubusercontent.com/u/3205522?v=4)](https://github.com/eyurtsev)

[eyurtsev](https://github.com/eyurtsev) [Feb 3](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-12046359)

Contributor

What do you need to do?

[![@sushi057](https://avatars.githubusercontent.com/u/64535753?u=ef7a681a6ddb0f0c4f45b7298f1ad03e278377c2&v=4)sushi057](https://github.com/sushi057) [Jan 16](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-11858535)

How can I do this?

/your\_package/your\_file.py:make\_graph, where make\_graph is a function that takes a config dictionary (langchain\_core.runnables.RunnableConfig)

I have a creat\_agents() function, I need the config file for routing and tools.

1

0 replies

[![@sammy0055](https://avatars.githubusercontent.com/u/72170585?u=1d16fc2aeda43612196a5cd519c9bf8277de0d81&v=4)sammy0055](https://github.com/sammy0055) [Feb 3](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-12044883)

when is the langraph studio IDE for windows going to be available?

1

1 reply

[![@eyurtsev](https://avatars.githubusercontent.com/u/3205522?v=4)](https://github.com/eyurtsev)

[eyurtsev](https://github.com/eyurtsev) [Feb 3](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-12046353)

Contributor

You can access the langgraph studio IDE using langgraph dev. Follow this tutorial: [https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/)

[![@aeronesto](https://avatars.githubusercontent.com/u/13804518?u=b031006635a906df8dc4705f06239751cc2eb278&v=4)aeronesto](https://github.com/aeronesto) [Feb 7](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-12088028)

I noticed that when I run `langgraph dockerfile --config=langgraph.json Dockerfile` my generated Dockerfile doesn't contain the environment variables specified in my .env value of langgraph.json. I have tried to set .env to a path and as a dictionary of values, and neither worked. I see the following confirmation that my langgraph.json was validated.

```
🔍 Validating configuration at path: path/to/my/app/langgraph.json
✅ Configuration validated!
📝 Generating Dockerfile at path/to/my/app/Dockerfile
✅ Created: Dockerfile
🎉 Files generated successfully at path path/to/my/app!
```

I expected to see these environment variables in my Dockerfile:

ENV MY\_VAR1=value1

MY\_VAR2=value2

1

0 replies

[![@AndreaDelliGatti](https://avatars.githubusercontent.com/u/28861452?u=3f2992f8123d1caab972248455d021622c3eed29&v=4)AndreaDelliGatti](https://github.com/AndreaDelliGatti) [Feb 7](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-12096303)

I'm developing a graph that uses hnswlib as vectordb, so on filesystem, but I realized that the directory containing the index is not copied inside the docker image. Is there a way to bring this folder inside?.

1

0 replies

[![@om-dev-123](https://avatars.githubusercontent.com/u/193818086?u=5db324d7eb1d998d16af453bc48bada6c5bcb1bc&v=4)om-dev-123](https://github.com/om-dev-123) [16 days ago](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-12309507)

dev server - [https://pasteboard.co/QBCajjuaf3qB.png](https://pasteboard.co/QBCajjuaf3qB.png) messages easy to type

non dev server - [https://pasteboard.co/K973iDmUd1Be.png](https://pasteboard.co/K973iDmUd1Be.png) messages almost impossible to type

how to fix this in non dev server

non dev server command - npx @langchain/langgraph-cli build

dev server command - npx @langchain/langgraph-cli dev

1

0 replies

[![@khaeldev](https://avatars.githubusercontent.com/u/62652658?u=85981c7e77a13e20bd7fdd3fcd5254350d87e227&v=4)khaeldev](https://github.com/khaeldev) [12 days ago](https://github.com/langchain-ai/langgraph/discussions/1217#discussioncomment-12361287)

I didn't see it here in the documentation but we can also use docker compose 🚀, just langgraph dockerfile --add-docker-compose docker-compose.yml

```
langgraph dockerfile --add-docker-compose docker-compose.yml
🔍 Validating configuration at path: /path/langgraph.json
✅ Configuration validated!
📝 Generating Dockerfile at /path/docker-compose.yml
✅ Created: Dockerfile
✅ Created: .dockerignore
✅ Created: docker-compose.yml
➖ Skipped: .env. It already exists!
🎉 Files generated successfully at path ...
```

1

👍1

0 replies

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Freference%2Fcli%2F)