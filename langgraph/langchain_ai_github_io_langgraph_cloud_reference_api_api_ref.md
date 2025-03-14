[Skip to content](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#api-reference)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/reference/api/api_ref.md "Edit this page")

# API Reference [¶](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/\#api-reference "Permanent link")

The LangGraph Cloud API reference is available with each deployment at the `/docs` URL path (e.g. `http://localhost:8124/docs`).

Click [here](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html) to view the API reference.

## Authentication [¶](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/\#authentication "Permanent link")

For deployments to LangGraph Cloud, authentication is required. Pass the `X-Api-Key` header with each request to the LangGraph Cloud API. The value of the header should be set to a valid LangSmith API key for the organization where the API is deployed.

Example `curl` command:

```md-code__content
curl --request POST \
  --url http://localhost:8124/assistants/search \
  --header 'Content-Type: application/json' \
  --header 'X-Api-Key: LANGSMITH_API_KEY' \
  --data '{
  "metadata": {},
  "limit": 10,
  "offset": 0
}'

```

## Comments

giscus

#### [2 reactions](https://github.com/langchain-ai/langgraph/discussions/2074)

👍2

#### [1 comment](https://github.com/langchain-ai/langgraph/discussions/2074)

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

_This comment has been minimized._

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Freference%2Fapi%2Fapi_ref%2F)