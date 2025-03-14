[Skip to content](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#how-to-integrate-langgraph-into-your-react-application)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/use_stream_react.md "Edit this page")

# How to integrate LangGraph into your React application [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/\#how-to-integrate-langgraph-into-your-react-application "Permanent link")

Prerequisites

- [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
- [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)

The `useStream()` React hook provides a seamless way to integrate LangGraph into your React applications. It handles all the complexities of streaming, state management, and branching logic, letting you focus on building great chat experiences.

Key features:

- Messages streaming: Handle a stream of message chunks to form a complete message
- Automatic state management for messages, interrupts, loading states, and errors
- Conversation branching: Create alternate conversation paths from any point in the chat history
- UI-agnostic design: bring your own components and styling

Let's explore how to use `useStream()` in your React application.

The `useStream()` provides a solid foundation for creating bespoke chat experiences. For pre-built chat components and interfaces, we also recommend checking out [CopilotKit](https://docs.copilotkit.ai/coagents/quickstart/langgraph) and [assistant-ui](https://www.assistant-ui.com/docs/runtimes/langgraph).

## Installation [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/\#installation "Permanent link")

```md-code__content
npm install @langchain/langgraph-sdk @langchain/core

```

## Example [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/\#example "Permanent link")

```md-code__content
"use client";

import { useStream } from "@langchain/langgraph-sdk/react";
import type { Message } from "@langchain/langgraph-sdk";

export default function App() {
  const thread = useStream<{ messages: Message[] }>({
    apiUrl: "http://localhost:2024",
    assistantId: "agent",
    messagesKey: "messages",
  });

  return (
    <div>
      <div>
        {thread.messages.map((message) => (
          <div key={message.id}>{message.content as string}</div>
        ))}
      </div>

      <form
        onSubmit={(e) => {
          e.preventDefault();

          const form = e.target as HTMLFormElement;
          const message = new FormData(form).get("message") as string;

          form.reset();
          thread.submit({ messages: [{ type: "human", content: message }] });
        }}
      >
        <input type="text" name="message" />

        {thread.isLoading ? (
          <button key="stop" type="button" onClick={() => thread.stop()}>
            Stop
          </button>
        ) : (
          <button keytype="submit">Send</button>
        )}
      </form>
    </div>
  );
}

```

## Customizing Your UI [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/\#customizing-your-ui "Permanent link")

The `useStream()` hook takes care of all the complex state management behind the scenes, providing you with simple interfaces to build your UI. Here's what you get out of the box:

- Thread state management
- Loading and error states
- Interrupts
- Message handling and updates
- Branching support

Here are some examples on how to use these features effectively:

### Loading States [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/\#loading-states "Permanent link")

The `isLoading` property tells you when a stream is active, enabling you to:

- Show a loading indicator
- Disable input fields during processing
- Display a cancel button

```md-code__content
export default function App() {
  const { isLoading, stop } = useStream<{ messages: Message[] }>({
    apiUrl: "http://localhost:2024",
    assistantId: "agent",
    messagesKey: "messages",
  });

  return (
    <form>
      {isLoading && (
        <button key="stop" type="button" onClick={() => stop()}>
          Stop
        </button>
      )}
    </form>
  );
}

```

### Thread Management [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/\#thread-management "Permanent link")

Keep track of conversations with built-in thread management. You can access the current thread ID and get notified when new threads are created:

```md-code__content
const [threadId, setThreadId] = useState<string | null>(null);

const thread = useStream<{ messages: Message[] }>({
  apiUrl: "http://localhost:2024",
  assistantId: "agent",

  threadId: threadId,
  onThreadId: setThreadId,
});

```

We recommend storing the `threadId` in your URL's query parameters to let users resume conversations after page refreshes.

### Messages Handling [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/\#messages-handling "Permanent link")

The `useStream()` hook will keep track of the message chunks received from the server and concatenate them together to form a complete message. The completed message chunks can be retrieved via the `messages` property.

By default, the `messagesKey` is set to `messages`, where it will append the new messages chunks to `values["messages"]`. If you store messages in a different key, you can change the value of `messagesKey`.

```md-code__content
import type { Message } from "@langchain/langgraph-sdk";
import { useStream } from "@langchain/langgraph-sdk/react";

export default function HomePage() {
  const thread = useStream<{ messages: Message[] }>({
    apiUrl: "http://localhost:2024",
    assistantId: "agent",
    messagesKey: "messages",
  });

  return (
    <div>
      {thread.messages.map((message) => (
        <div key={message.id}>{message.content as string}</div>
      ))}
    </div>
  );
}

```

Under the hood, the `useStream()` hook will use the `streamMode: "messages-key"` to receive a stream of messages (i.e. individual LLM tokens) from any LangChain chat model invocations inside your graph nodes. Learn more about messages streaming in the [How to stream messages from your graph](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_messages/) guide.

### Interrupts [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/\#interrupts "Permanent link")

The `useStream()` hook exposes the `interrupt` property, which will be filled with the last interrupt from the thread. You can use interrupts to:

- Render a confirmation UI before executing a node
- Wait for human input, allowing agent to ask the user with clarifying questions

Learn more about interrupts in the [How to handle interrupts](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/) guide.

```md-code__content
const thread = useStream<
  { messages: Message[] },
  { InterruptType: string }
>({
  apiUrl: "http://localhost:2024",
  assistantId: "agent",
  messagesKey: "messages",
});

if (thread.interrupt) {
  return (
    <div>
      Interrupted! {thread.interrupt.value}

      <button
        type="button"
        onClick={() => {
          // `resume` can be any value that the agent accepts
          thread.submit(undefined, { command: { resume: true } });
        }}
      >
        Resume
      </button>
    </div>
  );
}

```

### Branching [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/\#branching "Permanent link")

For each message, you can use `getMessagesMetadata()` to get the first checkpoint from which the message has been first seen. You can then create a new run from the checkpoint preceding the first seen checkpoint to create a new branch in a thread.

A branch can be created in following ways:

1. Edit a previous user message.
2. Request a regeneration of a previous assistant message.

```md-code__content
"use client";

import type { Message } from "@langchain/langgraph-sdk";
import { useStream } from "@langchain/langgraph-sdk/react";
import { useState } from "react";

function BranchSwitcher({
  branch,
  branchOptions,
  onSelect,
}: {
  branch: string | undefined;
  branchOptions: string[] | undefined;
  onSelect: (branch: string) => void;
}) {
  if (!branchOptions || !branch) return null;
  const index = branchOptions.indexOf(branch);

  return (
    <div className="flex items-center gap-2">
      <button
        type="button"
        onClick={() => {
          const prevBranch = branchOptions[index - 1];
          if (!prevBranch) return;
          onSelect(prevBranch);
        }}
      >
        Prev
      </button>
      <span>
        {index + 1} / {branchOptions.length}
      </span>
      <button
        type="button"
        onClick={() => {
          const nextBranch = branchOptions[index + 1];
          if (!nextBranch) return;
          onSelect(nextBranch);
        }}
      >
        Next
      </button>
    </div>
  );
}

function EditMessage({
  message,
  onEdit,
}: {
  message: Message;
  onEdit: (message: Message) => void;
}) {
  const [editing, setEditing] = useState(false);

  if (!editing) {
    return (
      <button type="button" onClick={() => setEditing(true)}>
        Edit
      </button>
    );
  }

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        const form = e.target as HTMLFormElement;
        const content = new FormData(form).get("content") as string;

        form.reset();
        onEdit({ type: "human", content });
        setEditing(false);
      }}
    >
      <input name="content" defaultValue={message.content as string} />
      <button type="submit">Save</button>
    </form>
  );
}

export default function App() {
  const thread = useStream({
    apiUrl: "http://localhost:2024",
    assistantId: "agent",
    messagesKey: "messages",
  });

  return (
    <div>
      <div>
        {thread.messages.map((message) => {
          const meta = thread.getMessagesMetadata(message);
          const parentCheckpoint = meta?.firstSeenState?.parent_checkpoint;

          return (
            <div key={message.id}>
              <div>{message.content as string}</div>

              {message.type === "human" && (
                <EditMessage
                  message={message}
                  onEdit={(message) =>
                    thread.submit(
                      { messages: [message] },
                      { checkpoint: parentCheckpoint },
                    )
                  }
                />
              )}

              {message.type === "ai" && (
                <button
                  type="button"
                  onClick={() =>
                    thread.submit(undefined, { checkpoint: parentCheckpoint })
                  }
                >
                  <span>Regenerate</span>
                </button>
              )}

              <BranchSwitcher
                branch={meta?.branch}
                branchOptions={meta?.branchOptions}
                onSelect={(branch) => thread.setBranch(branch)}
              />
            </div>
          );
        })}
      </div>

      <form
        onSubmit={(e) => {
          e.preventDefault();

          const form = e.target as HTMLFormElement;
          const message = new FormData(form).get("message") as string;

          form.reset();
          thread.submit({ messages: [message] });
        }}
      >
        <input type="text" name="message" />

        {thread.isLoading ? (
          <button key="stop" type="button" onClick={() => thread.stop()}>
            Stop
          </button>
        ) : (
          <button key="submit" type="submit">
            Send
          </button>
        )}
      </form>
    </div>
  );
}

```

For advanced use cases you can use the `experimental_branchTree` property to get the tree representation of the thread, which can be used to render branching controls for non-message based graphs.

### TypeScript [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/\#typescript "Permanent link")

The `useStream()` hook is friendly for apps written in TypeScript and you can specify types for the state to get better type safety and IDE support.

```md-code__content
// Define your types
type State = {
  messages: Message[];
  context?: Record<string, unknown>;
};

// Use them with the hook
const thread = useStream<State>({
  apiUrl: "http://localhost:2024",
  assistantId: "agent",
  messagesKey: "messages",
});

```

You can also optionally specify types for different scenarios, such as:

- `ConfigurableType`: Type for the `config.configurable` property (default: `Record<string, unknown>`)
- `InterruptType`: Type for the interrupt value - i.e. contents of `interrupt(...)` function (default: `unknown`)
- `CustomEventType`: Type for the custom events (default: `unknown`)
- `UpdateType`: Type for the submit function (default: `Partial<State>`)

```md-code__content
const thread = useStream<State, {
  UpdateType: {
    messages: Message[] | Message;
    context?: Record<string, unknown>;
  };
  InterruptType: string;
  CustomEventType: {
    type: "progress" | "debug";
    payload: unknown;
  };
  ConfigurableType: {
    model: string;
  };
}>({
  apiUrl: "http://localhost:2024",
  assistantId: "agent",
  messagesKey: "messages",
});

```

If you're using LangGraph.js, you can also reuse your graph's annotation types. However, make sure to only import the types of the annotation schema in order to avoid importing the entire LangGraph.js runtime (i.e. via `import type { ... }` directive).

```md-code__content
import {
  Annotation,
  MessagesAnnotation,
  type StateType,
  type UpdateType,
} from "@langchain/langgraph/web";

const AgentState = Annotation.Root({
  ...MessagesAnnotation.spec,
  context: Annotation<string>(),
});

const thread = useStream<
  StateType<typeof AgentState.spec>,
  { UpdateType: UpdateType<typeof AgentState.spec> }
>({
  apiUrl: "http://localhost:2024",
  assistantId: "agent",
  messagesKey: "messages",
});

```

## Event Handling [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/\#event-handling "Permanent link")

The `useStream()` hook provides several callback options to help you respond to different events:

- `onError`: Called when an error occurs.
- `onFinish`: Called when the stream is finished.
- `onUpdateEvent`: Called when an update event is received.
- `onCustomEvent`: Called when a custom event is received. See [Custom events](https://langchain-ai.github.io/langgraph/concepts/streaming/#custom) to learn how to stream custom events.
- `onMetadataEvent`: Called when a metadata event is received, which contains the Run ID and Thread ID.

## Learn More [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/\#learn-more "Permanent link")

- [JS/TS SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)

## Comments

giscus

#### [0 reactions](https://github.com/langchain-ai/langgraph/discussions/3552)

#### [5 comments](https://github.com/langchain-ai/langgraph/discussions/3552)

#### ·

#### 5 replies

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@ajitaravind](https://avatars.githubusercontent.com/u/160585903?u=a04e014c6d9bf79d16146401c476766c66f3fae1&v=4)ajitaravind](https://github.com/ajitaravind) [18 days ago](https://github.com/langchain-ai/langgraph/discussions/3552#discussioncomment-12289907)

Even though I added an interrupt in the graph before the tool calls(used the npm create langgraph with react agent), don't see thread.interrupt becoming True, its always undefined.

* * *

interrupt:

export const graph = workflow.compile({

interruptBefore: \["tools"\], // if you want to update the state before calling the tools

interruptAfter: \[\],

});

* * *

from console logs:

Thread State:

interrupt: undefined

* * *

Tried with both python and typescript backend, it is the same result. I could see the tool node is interrupted but the thread status still remain undefined. Am i doing something wrong? Thanks.

1

0 replies

[![@slimeonmyhead](https://avatars.githubusercontent.com/u/192735849?v=4)slimeonmyhead](https://github.com/slimeonmyhead) [17 days ago](https://github.com/langchain-ai/langgraph/discussions/3552#discussioncomment-12295313)

How do we get the network usage lower for the streaming?

I tried this to stop the server from sending `event: values`, but they're still streamed

```notranslate
onSubmit={(input) => {
  thread.submit(
    { messages: [{ type: "human", content: input }] },
    {
      optimisticValues: (prev) => ({
        messages: [\
          ...(prev?.messages ?? []),\
          { type: "human", content: input },\
        ],
      }),
      streamMode: ["messages", "updates"],
    },
  );
}}

```

1

0 replies

[![@brilliantstory2](https://avatars.githubusercontent.com/u/189232691?u=f160c9d8639bcf6b81034f709927401499a2d13b&v=4)brilliantstory2](https://github.com/brilliantstory2) [6 days ago](https://github.com/langchain-ai/langgraph/discussions/3552#discussioncomment-12428120)

I need to stream messages that comes from certain node.

For example, only final node messages should stream, others don't display.

How can I do this?

1

2 replies

[![@dqbd](https://avatars.githubusercontent.com/u/1443449?u=fe32372ae8f497065ef0a1c54194d9dff36fb81d&v=4)](https://github.com/dqbd)

[dqbd](https://github.com/dqbd) [6 days ago](https://github.com/langchain-ai/langgraph/discussions/3552#discussioncomment-12428982)

Contributor

Hello! You can use `tags: ["langsmith:nostream"]` to turn off streaming to `messages` stream mode from an LLM. Will think about making this more ergonomic.

[![@brilliantstory2](https://avatars.githubusercontent.com/u/189232691?u=f160c9d8639bcf6b81034f709927401499a2d13b&v=4)](https://github.com/brilliantstory2)

[brilliantstory2](https://github.com/brilliantstory2) [6 days ago](https://github.com/langchain-ai/langgraph/discussions/3552#discussioncomment-12429313)

Hi David Duong.

Thanks for your replay.

Could you help me more?

This is my code.

llm = ChatOpenAI(model="gpt-4o", temperature=0)

def search\_llm(state):

response = llm.invoke(\[SystemMessage(content=prompt)\]+state\["messages"\])

return {"messages": \[AIMessage(content = response.content)\]}

In frontend I used useStream.

import { useStream } from "@langchain/langgraph-sdk/react";

/// thread definition

const thread = useStream({

apiUrl: apiUrl,

apiKey: apiKey,

assistantId: "chatbot",

messagesKey: "messages",

threadId: currentThreadId,

});

//// this is render

{thread.messages.map((message, index) => {

return (

{

message.type === "ai" && (

{message.content}

)}

////////////////////////

```notranslate
            </div>
          )
        } )}

```

How can I use \["langsmith:nostream"\]

My final goal is to display only certain node's message on frontend.

Thanks a lot.🙂🎊

[![@brilliantstory2](https://avatars.githubusercontent.com/u/189232691?u=f160c9d8639bcf6b81034f709927401499a2d13b&v=4)brilliantstory2](https://github.com/brilliantstory2) [6 days ago](https://github.com/langchain-ai/langgraph/discussions/3552#discussioncomment-12429293)

Hi David Duong.
Thanks for your replay.
Could you help me more?

This is my code.
llm = ChatOpenAI(model="gpt-4o", temperature=0)

def search\_llm(state):
response = llm.invoke(\[SystemMessage(content=prompt)\]+state\["messages"\])
return {"messages": \[AIMessage(content = response.content)\]}

In frontend I used useStream.

import { useStream } from \*\*\*@\*\*\*.\*\*\*/langgraph-sdk/react";

/// thread definition
const thread = useStream({
apiUrl: apiUrl,
apiKey: apiKey,
assistantId: "chatbot",
messagesKey: "messages",
threadId: currentThreadId,
});

//// this is render
{thread.messages.map((message, index) => {
return (
<div
key={index}
className="......"

{
message.type === "ai" && (
<div className=".......">
<p>{message.content}</p>
</div>
)}
////////////////////////

</div>
)
} )}

How can I use \["langsmith:nostream"\]

My final goal is to display only certain node's message on frontend.

Thanks a lot.🙂🎊

[…](https://giscus.app/en/widget?origin=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fhow-tos%2Fuse_stream_react%2F&session=&theme=preferred_color_scheme&reactionsEnabled=1&emitMetadata=0&inputPosition=bottom&repo=langchain-ai%2Flanggraph&repoId=R_kgDOKFU0lQ&category=Discussions&categoryId=DIC_kwDOKFU0lc4CfZgA&strict=0&description=Build+language+agents+as+graphs&backLink=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fhow-tos%2Fuse_stream_react%2F&term=langgraph%2Fcloud%2Fhow-tos%2Fuse_stream_react%2F#)

On Fri, Mar 7, 2025 at 6:59 PM David Duong \*\*\*@\*\*\*.\*\*\*> wrote:
Hello! You can use tags: \["langsmith:nostream"\] to turn off streaming to
messages stream mode from an LLM. Will think about making this more
ergonomic.

—
Reply to this email directly, view it on GitHub
< [#3552 (reply in thread)](https://github.com/langchain-ai/langgraph/discussions/3552#discussioncomment-12428982) >,
or unsubscribe
< [https://github.com/notifications/unsubscribe-auth/BNDXMM4W2TCPHXNPL5AOHZ32THF7DAVCNFSM6AAAAABXUYQHU2VHI2DSMVQWIX3LMV43URDJONRXK43TNFXW4Q3PNVWWK3TUHMYTENBSHA4TQMQ](https://github.com/notifications/unsubscribe-auth/BNDXMM4W2TCPHXNPL5AOHZ32THF7DAVCNFSM6AAAAABXUYQHU2VHI2DSMVQWIX3LMV43URDJONRXK43TNFXW4Q3PNVWWK3TUHMYTENBSHA4TQMQ) >
.
You are receiving this because you commented.Message ID:
\*\*\*@\*\*\*.\*\*\*
com>

1

0 replies

[![@gelftheshot](https://avatars.githubusercontent.com/u/113858444?u=bb0e11839846463bfdd6e98ba8ea5b56fbd0efa4&v=4)gelftheshot](https://github.com/gelftheshot) [3 days ago](https://github.com/langchain-ai/langgraph/discussions/3552#discussioncomment-12445290)

Hey I tried to send configuration/ metadata to the agent. for example for booking agent I want to send. the information about currently signed in user to allow the AI who is talking to him for better UX. so that the AI don't have to ask about the name email and other information about the user.

so i tried this but not working.

thread.submit({

messages: \[{ type: "human", content: trimmedMessage },\],

}, {

config: {

configurable: {

name: "Mr. lihon Gebre",

email: " [gelf.learing@gmail.com](mailto:gelf.learing@gmail.com)",

phoneNumber: "0923245422"

}

}

});

no error but my agent doesn't recognize the user and on langgsmith there is not configuration. coming from the request. can any one help me

1

3 replies

[![@brilliantstory2](https://avatars.githubusercontent.com/u/189232691?u=f160c9d8639bcf6b81034f709927401499a2d13b&v=4)](https://github.com/brilliantstory2)

[brilliantstory2](https://github.com/brilliantstory2) [3 days ago](https://github.com/langchain-ai/langgraph/discussions/3552#discussioncomment-12450848)

I used metadata.

thread.submit({

messages: \[{ type: "human", content: message, metadata: { username: "YourUsername" }} \]

});

graph is python

print(state\["messages"\]\[-1\]

//printed on terminal

content='HI' additional\_kwargs={'metadata': {'username': 'YourUsername'}} response\_metadata={} id='873ac3ff-b716-4895-a358-82282c81a11c'

[![@brilliantstory2](https://avatars.githubusercontent.com/u/189232691?u=f160c9d8639bcf6b81034f709927401499a2d13b&v=4)](https://github.com/brilliantstory2)

[brilliantstory2](https://github.com/brilliantstory2) [3 days ago](https://github.com/langchain-ai/langgraph/discussions/3552#discussioncomment-12451634)

Could you help me?

Do you know how to display only final node's message?

[![@brilliantstory2](https://avatars.githubusercontent.com/u/189232691?u=f160c9d8639bcf6b81034f709927401499a2d13b&v=4)](https://github.com/brilliantstory2)

[brilliantstory2](https://github.com/brilliantstory2) [3 days ago](https://github.com/langchain-ai/langgraph/discussions/3552#discussioncomment-12452125)

I found solution that you want.

you can use your code on frontend.

thread.submit({

messages: \[{ type: "human", content: trimmedMessage },\],

}, {

config: {

configurable: {

name: "Mr. lihon Gebre",

email: " [gelf.learing@gmail.com](mailto:gelf.learing@gmail.com)",

phoneNumber: "0923245422"

}

}

});

on langgraph

from langchain\_core.runnables import RunnableConfig

def node\_name(state, config: RunnableConfig):

print(config\["configurable"\]\["name"\])

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fhow-tos%2Fuse_stream_react%2F)