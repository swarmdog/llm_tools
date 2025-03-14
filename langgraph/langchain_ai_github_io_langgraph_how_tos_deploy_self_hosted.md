[Skip to content](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/#how-to-do-a-self-hosted-deployment-of-langgraph)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/deploy-self-hosted.md "Edit this page")

# How to do a Self-hosted deployment of LangGraph [¶](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/\#how-to-do-a-self-hosted-deployment-of-langgraph "Permanent link")

Prerequisites

- [Application Structure](https://langchain-ai.github.io/langgraph/concepts/application_structure/)
- [Deployment Options](https://langchain-ai.github.io/langgraph/concepts/deployment_options/)

This how-to guide will walk you through how to create a docker image from an existing LangGraph application, so you can deploy it on your own infrastructure.

## How it works [¶](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/\#how-it-works "Permanent link")

With the self-hosted deployment option, you are responsible for managing the infrastructure, including setting up and maintaining necessary databases, Redis instances, and other services.

You will need to do the following:

1. Deploy Redis and Postgres instances on your own infrastructure.
2. Build a docker image with the [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/) using the [LangGraph CLI](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/).
3. Deploy a web server that will run the docker image and pass in the necessary environment variables.

## Helm Chart [¶](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/\#helm-chart "Permanent link")

If you would like to deploy LangGraph Cloud on Kubernetes, you can use this [Helm chart](https://github.com/langchain-ai/helm/blob/main/charts/langgraph-cloud/README.md).

## Environment Variables [¶](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/\#environment-variables "Permanent link")

You will eventually need to pass in the following environment variables to the LangGraph Deploy server:

- `REDIS_URI`: Connection details to a Redis instance. Redis will be used as a pub-sub broker to enable streaming real time output from background runs. The value of `REDIS_URI` must be a valid [Redis connection URI](https://redis-py.readthedocs.io/en/stable/connections.html#redis.Redis.from_url).



Shared Redis Instance



Multiple self-hosted deployments can share the same Redis instance. For example, for `Deployment A`, `REDIS_URI` can be set to `redis://<hostname_1>:<port>/1` and for `Deployment B`, `REDIS_URI` can be set to `redis://<hostname_1>:<port>/2`.



`1` and `2` are different database numbers within the same instance, but `<hostname_1>` is shared. **The same database number cannot be used for separate deployments**.

- `DATABASE_URI`: Postgres connection details. Postgres will be used to store assistants, threads, runs, persist thread state and long term memory, and to manage the state of the background task queue with 'exactly once' semantics. The value of `DATABASE_URI` must be a valid [Postgres connection URI](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS).



Shared Postgres Instance



Multiple self-hosted deployments can share the same Postgres instance. For example, for `Deployment A`, `DATABASE_URI` can be set to `postgres://<user>:<password>@/<database_name_1>?host=<hostname_1>` and for `Deployment B`, `DATABASE_URI` can be set to `postgres://<user>:<password>@/<database_name_2>?host=<hostname_1>`.



`<database_name_1>` and `database_name_2` are different databases within the same instance, but `<hostname_1>` is shared. **The same database cannot be used for separate deployments**.

- `LANGSMITH_API_KEY`: (If using [Self-Hosted Lite](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-lite)) LangSmith API key. This will be used to authenticate ONCE at server start up.

- `LANGGRAPH_CLOUD_LICENSE_KEY`: (If using [Self-Hosted Enterprise](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-enterprise)) LangGraph Platform license key. This will be used to authenticate ONCE at server start up.
- `LANGCHAIN_ENDPOINT`: To send traces to a [self-hosted LangSmith](https://docs.smith.langchain.com/self_hosting) instance, set `LANGCHAIN_ENDPOINT` to the hostname of the self-hosted LangSmith instance.

## Build the Docker Image [¶](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/\#build-the-docker-image "Permanent link")

Please read the [Application Structure](https://langchain-ai.github.io/langgraph/concepts/application_structure/) guide to understand how to structure your LangGraph application.

If the application is structured correctly, you can build a docker image with the LangGraph Deploy server.

To build the docker image, you first need to install the CLI:

```md-code__content
pip install -U langgraph-cli

```

You can then use:

```md-code__content
langgraph build -t my-image

```

This will build a docker image with the LangGraph Deploy server. The `-t my-image` is used to tag the image with a name.

When running this server, you need to pass three environment variables:

## Running the application locally [¶](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/\#running-the-application-locally "Permanent link")

### Using Docker [¶](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/\#using-docker "Permanent link")

```md-code__content
docker run \
    --env-file .env \
    -p 8123:8000 \
    -e REDIS_URI="foo" \
    -e DATABASE_URI="bar" \
    -e LANGSMITH_API_KEY="baz" \
    my-image

```

If you want to run this quickly without setting up a separate Redis and Postgres instance, you can use this docker compose file.

Note

- You need to replace `my-image` with the name of the image you built in the previous step (from `langgraph build`).
and you should provide appropriate values for `REDIS_URI`, `DATABASE_URI`, and `LANGSMITH_API_KEY`.
- If your application requires additional environment variables, you can pass them in a similar way.
- If using [Self-Hosted Enterprise](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-enterprise), you must provide `LANGGRAPH_CLOUD_LICENSE_KEY` as an additional environment variable.

### Using Docker Compose [¶](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/\#using-docker-compose "Permanent link")

```md-code__content
volumes:
    langgraph-data:
        driver: local
services:
    langgraph-redis:
        image: redis:6
        healthcheck:
            test: redis-cli ping
            interval: 5s
            timeout: 1s
            retries: 5
    langgraph-postgres:
        image: postgres:16
        ports:
            - "5433:5432"
        environment:
            POSTGRES_DB: postgres
            POSTGRES_USER: postgres
            POSTGRES_PASSWORD: postgres
        volumes:
            - langgraph-data:/var/lib/postgresql/data
        healthcheck:
            test: pg_isready -U postgres
            start_period: 10s
            timeout: 1s
            retries: 5
            interval: 5s
    langgraph-api:
        image: ${IMAGE_NAME}
        ports:
            - "8123:8000"
        depends_on:
            langgraph-redis:
                condition: service_healthy
            langgraph-postgres:
                condition: service_healthy
        env_file:
            - .env
        environment:
            REDIS_URI: redis://langgraph-redis:6379
            LANGSMITH_API_KEY: ${LANGSMITH_API_KEY}
            POSTGRES_URI: postgres://postgres:postgres@langgraph-postgres:5432/postgres?sslmode=disable

```

You can then run `docker compose up` with this Docker compose file in the same folder.

This will spin up LangGraph Deploy on port `8123` (if you want to change this, you can change this by changing the ports in the `langgraph-api` volume).

You can test that the application is up by checking:

```md-code__content
curl --request GET --url 0.0.0.0:8123/ok

```

Assuming everything is running correctly, you should see a response like:

```md-code__content
{"ok":true}

```

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Please help us improve this page by adding to the discussion below.


## Comments

[iframe](https://giscus.app/en/widget?origin=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fhow-tos%2Fdeploy-self-hosted%2F&session=&theme=preferred_color_scheme&reactionsEnabled=1&emitMetadata=0&inputPosition=bottom&repo=langchain-ai%2Flanggraph&repoId=R_kgDOKFU0lQ&category=Discussions&categoryId=DIC_kwDOKFU0lc4CfZgA&strict=0&description=Build+language+agents+as+graphs&backLink=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fhow-tos%2Fdeploy-self-hosted%2F&term=langgraph%2Fhow-tos%2Fdeploy-self-hosted%2F)

Back to top