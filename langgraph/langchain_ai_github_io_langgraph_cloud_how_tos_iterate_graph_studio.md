[Skip to content](https://langchain-ai.github.io/langgraph/cloud/how-tos/iterate_graph_studio/#prompt-engineering-in-langgraph-studio)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/iterate_graph_studio.md "Edit this page")

# Prompt Engineering in LangGraph Studio [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/iterate_graph_studio/\#prompt-engineering-in-langgraph-studio "Permanent link")

In LangGraph Studio you can iterate on the prompts used within your graph by utilizing the LangSmith Playground. To do so:

1. Open an existing thread or create a new one.
2. Within the thread log, any nodes that have made an LLM call will have a "View LLM Runs" button. Clicking this will open a popover with the LLM runs for that node.
3. Select the LLM run you want to edit. This will open the LangSmith Playground with the selected LLM run.

![Playground in Studio](https://langchain-ai.github.io/langgraph/cloud/how-tos/img/studio_playground.png)

From here you can edit the prompt, test different model configurations and re-run just this LLM call without having to re-run the entire graph. When you are happy with your changes, you can copy the updated prompt back into your graph.

For more information on how to use the LangSmith Playground, see the [LangSmith Playground documentation](https://docs.smith.langchain.com/prompt_engineering/how_to_guides#playground).

## Comments

giscus

#### 0 reactions

#### 0 comments

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fhow-tos%2Fiterate_graph_studio%2F)