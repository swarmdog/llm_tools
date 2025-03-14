[Skip to content](https://langchain-ai.github.io/langgraph/prebuilt/#prebuilt-agents)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/prebuilt.md "Edit this page")

# 🚀 Prebuilt Agents [¶](https://langchain-ai.github.io/langgraph/prebuilt/\#prebuilt-agents "Permanent link")

LangGraph includes a prebuilt React agent. For more information on how to use it,
check out our [how-to guides](https://langchain-ai.github.io/langgraph/how-tos/#prebuilt-react-agent).

If you’re looking for other prebuilt libraries, explore the community-built options
below. These libraries can extend LangGraph's functionality in various ways.

## 📚 Available Libraries [¶](https://langchain-ai.github.io/langgraph/prebuilt/\#available-libraries "Permanent link")

| Name | GitHub URL | Description | Weekly Downloads | Stars |
| --- | --- | --- | --- | --- |
| **trustcall** | [hinthornw/trustcall](https://github.com/hinthornw/trustcall) | Tenacious tool calling built on LangGraph. | 13550 | ![GitHub stars](https://img.shields.io/github/stars/hinthornw/trustcall?style=social) |
| **langgraph-supervisor** | [langchain-ai/langgraph-supervisor-py](https://github.com/langchain-ai/langgraph-supervisor-py) | Build supervisor multi-agent systems with LangGraph. | 9488 | ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph-supervisor-py?style=social) |
| **langmem** | [langchain-ai/langmem](https://github.com/langchain-ai/langmem) | Build agents that learn and adapt from interactions over time. | 4881 | ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langmem?style=social) |
| **langchain-mcp-adapters** | [langchain-ai/langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters) | Make Anthropic Model Context Protocol (MCP) tools compatible with LangGraph agents. | 2662 | ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langchain-mcp-adapters?style=social) |
| **open-deep-research** | [langchain-ai/open\_deep\_research](https://github.com/langchain-ai/open_deep_research) | Open source assistant for iterative web research and report writing. | 1883 | ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/open_deep_research?style=social) |
| **langgraph-swarm** | [langchain-ai/langgraph-swarm-py](https://github.com/langchain-ai/langgraph-swarm-py) | Build swarm-style multi-agent systems using LangGraph. | 1155 | ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph-swarm-py?style=social) |
| **langgraph-reflection** | [langchain-ai/langgraph-reflection](https://github.com/langchain-ai/langgraph-reflection) | LangGraph agent that runs a reflection step. | 567 | ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph-reflection?style=social) |
| **langgraph-bigtool** | [langchain-ai/langgraph-bigtool](https://github.com/langchain-ai/langgraph-bigtool) | Build LangGraph agents with large numbers of tools. | 167 | ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph-bigtool?style=social) |
| **delve-taxonomy-generator** | [andrestorres123/delve](https://github.com/andrestorres123/delve) | A taxonomy generator for unstructured data | 61 | ![GitHub stars](https://img.shields.io/github/stars/andrestorres123/delve?style=social) |
| **breeze-agent** | [andrestorres123/breeze-agent](https://github.com/andrestorres123/breeze-agent) | A streamlined research system built inspired on STORM and built on LangGraph. | 51 | ![GitHub stars](https://img.shields.io/github/stars/andrestorres123/breeze-agent?style=social) |
| **nodeology** | [xyin-anl/Nodeology](https://github.com/xyin-anl/Nodeology) | Enable researcher to build scientific workflows easily with simplified interface. | 50 | ![GitHub stars](https://img.shields.io/github/stars/xyin-anl/Nodeology?style=social) |

## ✨ Contributing Your Library [¶](https://langchain-ai.github.io/langgraph/prebuilt/\#contributing-your-library "Permanent link")

Have you built an awesome open-source library using LangGraph? We'd love to feature
your project on the official LangGraph documentation pages! 🏆

To share your project, simply open a Pull Request adding an entry for your package in our [packages.yml](https://github.com/langchain-ai/langgraph/blob/main/docs/_scripts/third_party_page/packages.yml) file.

**Guidelines**

- Your repo must be distributed as an installable package (e.g., PyPI for Python, npm
for JavaScript/TypeScript, etc.) 📦
- The repo should either use the Graph API (exposing a `StateGraph` instance) or
the Functional API (exposing an `entrypoint`).
- The package must include documentation (e.g., a `README.md` or docs site)
explaining how to use it.

We'll review your contribution and merge it in!

Thanks for contributing! 🚀

## Comments

giscus

#### [6 reactions](https://github.com/langchain-ai/langgraph/discussions/517)

👍5🚀1

#### [8 comments](https://github.com/langchain-ai/langgraph/discussions/517)

#### ·

#### 8 replies

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@woodswift](https://avatars.githubusercontent.com/u/15988956?u=091d00f8d0f0b3e323f27f6495a877000e15b361&v=4)woodswift](https://github.com/woodswift) [Jul 16, 2024](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-10065190)

Could you please provide a better solution to use the pre-defined prompt by create\_react\_agent() interface? For example, as shown below, the variable `prompt` is a global variable, and it is used internally by the function modify\_messages(). It does not follow the best practice of programming. One potential solution is to move prompt inside the function. However, it might limit the reuse ability of the function. Any advice?

```notranslate
>>> from langchain_core.prompts import ChatPromptTemplate
>>> prompt = ChatPromptTemplate.from_messages([\
...     ("system", "You are a helpful bot named Fred."),\
...     ("placeholder", "{messages}"),\
...     ("user", "Remember, always be polite!"),\
... ])
>>> def modify_messages(messages: list):
...     # You can do more complex modifications here
...     return prompt.invoke({"messages": messages})
>>>
>>> graph = create_react_agent(model, tools, messages_modifier=modify_messages)

```

1

1 reply

[![@hinthornw](https://avatars.githubusercontent.com/u/13333726?u=82ebf1e0eb0663ebd49ba66f67a43f51bbf11442&v=4)](https://github.com/hinthornw)

[hinthornw](https://github.com/hinthornw) [Feb 7](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-12098679)

Contributor

1. It's not something that's mutated so it's not bad to have outside
2. You can namespace it if you want
3. You can use a class instead if you want
4. You can use a function instead if you watn.
5. You can use closures if you want.

[![@SvenDuve](https://avatars.githubusercontent.com/u/10611906?u=b9759e8c8ac068c28a727c1d70800fba279dfce5&v=4)SvenDuve](https://github.com/SvenDuve) [Oct 29, 2024](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-11086440)

Just in case somebody else is confused, the following example won't work like this:

```notranslate
>>> from typing import TypedDict
>>> prompt = ChatPromptTemplate.from_messages(
...     [\
...         ("system", "Today is {today}"),\
...         ("placeholder", "{messages}"),\
...     ]
... )
>>>
>>> class CustomState(TypedDict):
...     today: str
...     messages: Annotated[list[BaseMessage], add_messages]
...     is_last_step: str
>>>
>>> graph = create_react_agent(model, tools, state_schema=CustomState, state_modifier=prompt)
>>> inputs = {"messages": [("user", "What's today's date? And what's the weather in SF?")], "today": "July 16, 2004"}
>>> for s in graph.stream(inputs, stream_mode="values"):
...     message = s["messages"][-1]
...     if isinstance(message, tuple):
...         print(message)
...     else:
...         message.pretty_print()

```

you would have to pass the `is_last_step=False`:

```notranslate
inputs = {"messages": [("user", "What's today's date? And what's the weather in SF?")], "today": "July 16, 2004", "is_last_step":False}

```

1

1 reply

[![@vbarda](https://avatars.githubusercontent.com/u/19161700?u=e76bcd472b51c9f07befd2654783d0a381f49005&v=4)](https://github.com/vbarda)

[vbarda](https://github.com/vbarda) [8 days ago](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-12402355)

Collaborator

you shouldn't need to specify `is_last_step` at all -- you need to subclass your graph state to use custom state schema:

```
from langgraph.prebuilt.chat_agent_executor import AgentState

class CustomState(AgentState):
    today: str
```

[![@sepety](https://avatars.githubusercontent.com/u/120281248?v=4)sepety](https://github.com/sepety) [Nov 14, 2024](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-11250281)

good day!! please help me solve such a simple problem (but I'm confused in the code and don't see any acceptable examples or instructions) - I want to make an agent with the rag\_tool tool that will take the kottext from my pinecone index. what methods should I use, maybe there are examples of such a simple agent? I would be extremely grateful!!

1

1 reply

[![@Heiden133](https://avatars.githubusercontent.com/u/102782285?v=4)](https://github.com/Heiden133)

[Heiden133](https://github.com/Heiden133) [Dec 3, 2024](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-11447132)

You can use Pinecone vector store as a retriever and append it to tools.

[https://python.langchain.com/api\_reference/pinecone/vectorstores/langchain\_pinecone.vectorstores.PineconeVectorStore.html#langchain\_pinecone.vectorstores.PineconeVectorStore](https://python.langchain.com/api_reference/pinecone/vectorstores/langchain_pinecone.vectorstores.PineconeVectorStore.html#langchain_pinecone.vectorstores.PineconeVectorStore)

[![@jimmyn88](https://avatars.githubusercontent.com/u/177209061?v=4)jimmyn88](https://github.com/jimmyn88) [Dec 19, 2024](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-11616386)

Hi,

Is it possibile to get a structured output from a ReAct Agent?

At the moment this is my output:

```
{
  "action": "search",
  "action_input": "what is the temperature in SF"
}'''
```

1

👍2

3 replies

[![@jimmyn88](https://avatars.githubusercontent.com/u/177209061?v=4)](https://github.com/jimmyn88)

[jimmyn88](https://github.com/jimmyn88) [Dec 19, 2024](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-11616401)

At the moment this is my output:

'''JSON

{

"action": "search",

"action\_input": "what is the temperature in SF"

}'''

[![@Hamza5](https://avatars.githubusercontent.com/u/7011111?v=4)](https://github.com/Hamza5)

[Hamza5](https://github.com/Hamza5) [Feb 11](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-12143937)

There is already a tutorial on this:

[How to return structured output from a ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/)

[![@vbarda](https://avatars.githubusercontent.com/u/19161700?u=e76bcd472b51c9f07befd2654783d0a381f49005&v=4)](https://github.com/vbarda)

[vbarda](https://github.com/vbarda) [8 days ago](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-12402364)

Collaborator

and you can also pass `response_format` to `create_react_agent`

[![@amandafanny](https://avatars.githubusercontent.com/u/54808661?u=a68800acb68332b76841539bc70ca59893695e66&v=4)amandafanny](https://github.com/amandafanny) [Dec 30, 2024](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-11695671)

the code in ValidationNode can't run well.

```notranslate
File ~/miniconda3/lib/python3.12/site-packages/langgraph/pregel/__init__.py:1929, in Pregel.invoke(self, input, config, stream_mode, output_keys, interrupt_before, interrupt_after, debug, **kwargs)
   1927 else:
   1928     chunks = []
-> 1929 for chunk in self.stream(
   1930     input,
   1931     config,
   1932     stream_mode=stream_mode,
   1933     output_keys=output_keys,
   1934     interrupt_before=interrupt_before,
   1935     interrupt_after=interrupt_after,
   1936     debug=debug,
   1937     **kwargs,
   1938 ):
   1939     if stream_mode == "values":
   1940         latest = chunk
...
--> 643     raise InvalidUpdateError(msg)

InvalidUpdateError: Expected dict, got ('user', 'Select a number, any number')

```

1

😕1

1 reply

[![@vbarda](https://avatars.githubusercontent.com/u/19161700?u=e76bcd472b51c9f07befd2654783d0a381f49005&v=4)](https://github.com/vbarda)

[vbarda](https://github.com/vbarda) [8 days ago](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-12402334)

Collaborator

how are you invoking it?

[![@agdev](https://avatars.githubusercontent.com/u/3872949?v=4)agdev](https://github.com/agdev) [Jan 3](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-11725466)

When using Groq

The code below does not work in ends up in loop.

==============Code===================

> > > from langchain\_core.prompts import ChatPromptTemplate
> > >
> > > prompt = ChatPromptTemplate.from\_messages(\[\
> > >\
> > > ... ("system", "You are a helpful bot named Fred."),\
> > >\
> > > ... ("placeholder", "{messages}"),\
> > >\
> > > ... ("user", "Remember, always be polite!"),\
> > >\
> > > ... \])
> > >
> > > def format\_for\_model(state: AgentState):
> > >
> > > ... # You can do more complex modifications here
> > >
> > > ... return prompt.invoke({"messages": state\["messages"\]})
> > >
> > > graph = create\_react\_agent(model, tools, state\_modifier=format\_for\_model)
> > >
> > > inputs = {"messages": \[("user", "What's your name? And what's the weather in SF?")\]}
> > >
> > > for s in graph.stream(inputs, stream\_mode="values"):
> > >
> > > ... message = s\["messages"\]\[-1\]
> > >
> > > ... if isinstance(message, tuple):
> > >
> > > ... print(message)
> > >
> > > ... else:
> > >
> > > ... message.pretty\_print()
> > >
> > > ==============End of code ==============

1

👀1

0 replies

[![@ashwanthkumar1007](https://avatars.githubusercontent.com/u/67331617?u=452af930304523dc5da25ee571e33b637cf00384&v=4)ashwanthkumar1007](https://github.com/ashwanthkumar1007) [28 days ago](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-12190211)

Is it possible to connect multiple databases to a create\_react\_agent and make the LLM query from these multiple databases to find the final result?

connection\_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={DRIVER\_NAME}"

engine = create\_engine(connection\_string)

db = SQLDatabase(engine)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

toolkit.get\_tools()

agent\_executor = create\_react\_agent(

llm, toolkit.get\_tools(), state\_modifier=system\_message

)

1

😕1

0 replies

[![@tiaan720](https://avatars.githubusercontent.com/u/157584945?v=4)tiaan720](https://github.com/tiaan720) [21 days ago](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-12261367)

Good day, we had code that relied on the state\_modifier. Since this feature is now removed. How can we still achieve the same state modification?

1

1 reply

[![@eyurtsev](https://avatars.githubusercontent.com/u/3205522?v=4)](https://github.com/eyurtsev)

[eyurtsev](https://github.com/eyurtsev) [15 days ago](https://github.com/langchain-ai/langgraph/discussions/517#discussioncomment-12329044)

Contributor

The feature has not been removed. It's been renamed, although the old parameter name will continue to work. If you're on a new version rename the parameter to `prompt`. Please consult the API reference: [https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat\_agent\_executor.create\_react\_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fprebuilt%2F)