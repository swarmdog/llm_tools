[Skip to content](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/#langgraph-studio-with-local-deployment)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/test_local_deployment.md "Edit this page")

# LangGraph Studio With Local Deployment [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/\#langgraph-studio-with-local-deployment "Permanent link")

Browser Compatibility

Viewing the studio page of a local LangGraph deployment does not work in Safari. Use Chrome instead.

## Setup [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/\#setup "Permanent link")

Make sure you have setup your app correctly, by creating a compiled graph, a `.env` file with any environment variables, and a `langgraph.json` config file that points to your environment file and compiled graph. See [here](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/) for more detailed instructions.

After you have your app setup, head into the directory with your `langgraph.json` file and call `langgraph dev` to start the API server in watch mode which means it will restart on code changes, which is ideal for local testing. If the API server start correctly you should see logs that look something like this:

> Ready!
>
> - API: [http://localhost:2024](http://localhost:2024/)
>
> - Docs: [http://localhost:2024/docs](http://localhost:2024/docs)
>
> - LangGraph Studio Web UI: [https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024](https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024)

Read this [reference](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#up) to learn about all the options for starting the API server.

## Access Studio [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/\#access-studio "Permanent link")

Once you have successfully started the API server, you can access the studio by going to the following URL: `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024` (see warning above if using Safari).

If everything is working correctly you should see the studio show up looking something like this (with your graph diagram on the left hand side):

![LangGraph Studio](https://langchain-ai.github.io/langgraph/cloud/how-tos/img/studio_screenshot.png)

## Use the Studio for Testing [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/\#use-the-studio-for-testing "Permanent link")

To learn about how to use the studio for testing, read the [LangGraph Studio how-tos](https://langchain-ai.github.io/langgraph/cloud/how-tos/#langgraph-studio).

## Comments

giscus

#### [0 reactions](https://github.com/langchain-ai/langgraph/discussions/3424)

#### [1 comment](https://github.com/langchain-ai/langgraph/discussions/3424)

#### ·

#### 1 reply

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@bejjani](https://avatars.githubusercontent.com/u/12160733?u=15c786ea89ae33f3ee30da9ed4055386a809bbd2&v=4)bejjani](https://github.com/bejjani) [28 days ago](https://github.com/langchain-ai/langgraph/discussions/3424#discussioncomment-12191424)

why does the LangGraph Studio Web UI have to go through the website [https://smith.langchain.com/studio/](https://smith.langchain.com/studio/) if it is deployed locally? Is there a option to access the Studio without any data going out?

1

1 reply

[![@hinthornw](https://avatars.githubusercontent.com/u/13333726?u=82ebf1e0eb0663ebd49ba66f67a43f51bbf11442&v=4)](https://github.com/hinthornw)

[hinthornw](https://github.com/hinthornw) [28 days ago](https://github.com/langchain-ai/langgraph/discussions/3424#discussioncomment-12191565)

Contributor

Frontend code is co-deployed right now. No local frontend yet.

👎1😕1

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fhow-tos%2Ftest_local_deployment%2F)