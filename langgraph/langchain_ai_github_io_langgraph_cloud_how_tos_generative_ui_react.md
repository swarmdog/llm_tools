[Skip to content](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/#how-to-implement-generative-user-interfaces-with-langgraph)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/generative_ui_react.md "Edit this page")

# How to implement Generative User Interfaces with LangGraph [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/\#how-to-implement-generative-user-interfaces-with-langgraph "Permanent link")

Prerequisites

- [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
- [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)
- [`useStream()` React Hook](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/)

Generative user interfaces (Generative UI) allows agents to go beyond text and generate rich user interfaces. This enables creating more interactive and context-aware applications where the UI adapts based on the conversation flow and AI responses.

![Generative UI Sample](https://langchain-ai.github.io/langgraph/cloud/how-tos/img/generative_ui_sample.jpg)

LangGraph Platform supports colocating your React components with your graph code. This allows you to focus on building specific UI components for your graph while easily plugging into existing chat interfaces such as [Agent Chat](https://agentchat.vercel.app/) and loading the code only when actually needed.

LangGraph.js only

Currently only LangGraph.js supports Generative UI. Support for Python is coming soon.

## Tutorial [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/\#tutorial "Permanent link")

### 1\. Define and configure UI components [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/\#1-define-and-configure-ui-components "Permanent link")

First, create your first UI component. For each component you need to provide an unique identifier that will be used to reference the component in your graph code.

src/agent/ui.tsx

```md-code__content
const WeatherComponent = (props: { city: string }) => {
  return <div>Weather for {props.city}</div>;
};

export default {
  weather: WeatherComponent,
};

```

Next, define your UI components in your `langgraph.json` configuration:

```md-code__content
{
  "node_version": "20",
  "graphs": {
    "agent": "./src/agent/index.ts:graph"
  },
  "ui": {
    "agent": "./src/agent/ui.tsx"
  }
}

```

The `ui` section points to the UI components that will be used by graphs. By default, we recommend using the same key as the graph name, but you can split out the components however you like, see [Customise the namespace of UI components](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/#customise-the-namespace-of-ui-components) for more details.

LangGraph Platform will automatically bundle your UI components code and styles and serve them as external assets that can be loaded by the `LoadExternalComponent` component. Some dependencies such as `react` and `react-dom` will be automatically excluded from the bundle.

CSS and Tailwind 4.x is also supported out of the box, so you can freely use Tailwind classes as well as `shadcn/ui` in your UI components.

[`src/agent/ui.tsx`](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/#__tabbed_1_1)[`src/agent/styles.css`](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/#__tabbed_1_2)

```md-code__content
import "./styles.css";

const WeatherComponent = (props: { city: string }) => {
  return <div className="bg-red-500">Weather for {props.city}</div>;
};

export default {
  weather: WeatherComponent,
};

```

```md-code__content
@import "tailwindcss";

```

### 2\. Send the UI components in your graph [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/\#2-send-the-ui-components-in-your-graph "Permanent link")

Use the `typedUi` utility to emit UI elements from your agent nodes:

src/agent/index.ts

```md-code__content
import {
  typedUi,
  uiMessageReducer,
} from "@langchain/langgraph-sdk/react-ui/server";

import { ChatOpenAI } from "@langchain/openai";
import { v4 as uuidv4 } from "uuid";
import { z } from "zod";

import type ComponentMap from "./ui.js";

import {
  Annotation,
  MessagesAnnotation,
  StateGraph,
  type LangGraphRunnableConfig,
} from "@langchain/langgraph";

const AgentState = Annotation.Root({
  ...MessagesAnnotation.spec,
  ui: Annotation({ reducer: uiMessageReducer, default: () => [] }),
});

export const graph = new StateGraph(AgentState)
  .addNode("weather", async (state, config) => {
    // Provide the type of the component map to ensure
    // type safety of `ui.push()` calls as well as
    // pushing the messages to the `ui` and sending a custom event as well.
    const ui = typedUi<typeof ComponentMap>(config);

    const weather = await new ChatOpenAI({ model: "gpt-4o-mini" })
      .withStructuredOutput(z.object({ city: z.string() }))
      .withConfig({ tags: ["langsmith:nostream"] })
      .invoke(state.messages);

    const response = {
      id: uuidv4(),
      type: "ai",
      content: `Here's the weather for ${weather.city}`,
    };

    // Emit UI elements with associated AI message
    ui.push({ name: "weather", props: weather }, { message: response });

    return { messages: [response] };
  })
  .addEdge("__start__", "weather")
  .compile();

```

### 3\. Handle UI elements in your React application [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/\#3-handle-ui-elements-in-your-react-application "Permanent link")

On the client side, you can use `useStream()` and `LoadExternalComponent` to display the UI elements.

src/app/page.tsx

```md-code__content
"use client";

import { useStream } from "@langchain/langgraph-sdk/react";
import { LoadExternalComponent } from "@langchain/langgraph-sdk/react-ui";

export default function Page() {
  const { thread, values } = useStream({
    apiUrl: "http://localhost:2024",
    assistantId: "agent",
  });

  return (
    <div>
      {thread.messages.map((message) => (
        <div key={message.id}>
          {message.content}
          {values.ui
            ?.filter((ui) => ui.metadata?.message_id === message.id)
            .map((ui) => (
              <LoadExternalComponent key={ui.id} stream={thread} message={ui} />
            ))}
        </div>
      ))}
    </div>
  );
}

```

Behind the scenes, `LoadExternalComponent` will fetch the JS and CSS for the UI components from LangGraph Platform and render them in a shadow DOM, thus ensuring style isolation from the rest of your application.

## How-to guides [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/\#how-to-guides "Permanent link")

### Show loading UI when components are loading [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/\#show-loading-ui-when-components-are-loading "Permanent link")

You can provide a fallback UI to be rendered when the components are loading.

```md-code__content
<LoadExternalComponent
  stream={thread}
  message={ui}
  fallback={<div>Loading...</div>}
/>

```

### Provide custom components on the client side [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/\#provide-custom-components-on-the-client-side "Permanent link")

If you already have the components loaded in your client application, you can provide a map of such components to be rendered directly without fetching the UI code from LangGraph Platform.

```md-code__content
const clientComponents = {
  weather: WeatherComponent,
};

<LoadExternalComponent
  stream={thread}
  message={ui}
  components={clientComponents}
/>;

```

### Customise the namespace of UI components. [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/\#customise-the-namespace-of-ui-components "Permanent link")

By default `LoadExternalComponent` will use the `assistantId` from `useStream()` hook to fetch the code for UI components. You can customise this by providing a `namespace` prop to the `LoadExternalComponent` component.

[`src/app/page.tsx`](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/#__tabbed_2_1)[`langgraph.json`](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/#__tabbed_2_2)

```md-code__content
<LoadExternalComponent
  stream={thread}
  message={ui}
  namespace="custom-namespace"
/>

```

```md-code__content
{
  "ui": {
    "custom-namespace": "./src/agent/ui.tsx"
  }
}

```

### Access and interact with the thread state from the UI component [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/\#access-and-interact-with-the-thread-state-from-the-ui-component "Permanent link")

You can access the thread state inside the UI component by using the `useStreamContext` hook.

```md-code__content
import { useStreamContext } from "@langchain/langgraph-sdk/react-ui";

const WeatherComponent = (props: { city: string }) => {
  const { thread, submit } = useStreamContext();
  return (
    <>
      <div>Weather for {props.city}</div>

      <button
        onClick={() => {
          const newMessage = {
            type: "human",
            content: `What's the weather in ${props.city}?`,
          };

          submit({ messages: [newMessage] });
        }}
      >
        Retry
      </button>
    </>
  );
};

```

### Pass additional context to the client components [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/\#pass-additional-context-to-the-client-components "Permanent link")

You can pass additional context to the client components by providing a `meta` prop to the `LoadExternalComponent` component.

```md-code__content
<LoadExternalComponent stream={thread} message={ui} meta={{ userId: "123" }} />

```

Then, you can access the `meta` prop in the UI component by using the `useStreamContext` hook.

```md-code__content
import { useStreamContext } from "@langchain/langgraph-sdk/react-ui";

const WeatherComponent = (props: { city: string }) => {
  const { meta } = useStreamContext<
    { city: string },
    { MetaType: { userId?: string } }
  >();

  return (
    <div>
      Weather for {props.city} (user: {meta?.userId})
    </div>
  );
};

```

### Streaming UI updates before the node execution is finished [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/\#streaming-ui-updates-before-the-node-execution-is-finished "Permanent link")

You can stream UI updates before the node execution is finished by using the `onCustomEvent` callback of the `useStream()` hook.

```md-code__content
import { uiMessageReducer } from "@langchain/langgraph-sdk/react-ui";

const { thread, submit } = useStream({
  apiUrl: "http://localhost:2024",
  assistantId: "agent",
  onCustomEvent: (event, options) => {
    options.mutate((prev) => {
      const ui = uiMessageReducer(prev.ui ?? [], event);
      return { ...prev, ui };
    });
  },
});

```

### Remove UI messages from state [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/\#remove-ui-messages-from-state "Permanent link")

Similar to how messages can be removed from the state by appending a RemoveMessage you can remove an UI message from the state by calling `ui.delete` with the ID of the UI message.

```md-code__content
// pushed message
const message = ui.push({ name: "weather", props: { city: "London" } });

// remove said message
ui.delete(message.id);

// return new state to persist changes
return { ui: ui.items };

```

## Learn more [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/generative_ui_react/\#learn-more "Permanent link")

- [JS/TS SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)

## Comments

giscus

#### 0 reactions

#### 0 comments

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fhow-tos%2Fgenerative_ui_react%2F)