[Skip to content](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#self-hosted)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/self_hosted.md "Edit this page")

# Self-Hosted [¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/\#self-hosted "Permanent link")

Note

- [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
- [Deployment Options](https://langchain-ai.github.io/langgraph/concepts/deployment_options/)

## Versions [¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/\#versions "Permanent link")

There are two versions of the self-hosted deployment: [Self-Hosted Enterprise](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-enterprise) and [Self-Hosted Lite](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-lite).

### Self-Hosted Lite [¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/\#self-hosted-lite "Permanent link")

The Self-Hosted Lite version is a limited version of LangGraph Platform that you can run locally or in a self-hosted manner (up to 1 million nodes executed per year).

When using the Self-Hosted Lite version, you authenticate with a [LangSmith](https://smith.langchain.com/) API key.

### Self-Hosted Enterprise [¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/\#self-hosted-enterprise "Permanent link")

The Self-Hosted Enterprise version is the full version of LangGraph Platform.

To use the Self-Hosted Enterprise version, you must acquire a license key that you will need to pass in when running the Docker image. To acquire a license key, please email [sales@langchain.dev](mailto:sales@langchain.dev).

## Requirements [¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/\#requirements "Permanent link")

- You use `langgraph-cli` and/or [LangGraph Studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/) app to test graph locally.
- You use `langgraph build` command to build image.

## How it works [¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/\#how-it-works "Permanent link")

- Deploy Redis and Postgres instances on your own infrastructure.
- Build the docker image for [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/) using the [LangGraph CLI](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/).
- Deploy a web server that will run the docker image and pass in the necessary environment variables.

Note

The LangGraph Platform Deployments view is optionally available for Self-Hosted LangGraph deployments. With one click, self-hosted LangGraph deployments can be deployed in the same Kubernetes cluster where a self-hosted LangSmith instance is deployed.

For step-by-step instructions, see [How to set up a self-hosted deployment of LangGraph](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/).

## Helm Chart [¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/\#helm-chart "Permanent link")

If you would like to deploy LangGraph Cloud on Kubernetes, you can use this [Helm chart](https://github.com/langchain-ai/helm/blob/main/charts/langgraph-cloud/README.md).

## Related [¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/\#related "Permanent link")

- [How to set up a self-hosted deployment of LangGraph](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/).

## Comments

giscus

#### 0 reactions

#### 0 comments

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fconcepts%2Fself_hosted%2F)