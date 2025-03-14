[Skip to content](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#interrupt)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/interrupt_concurrent.md "Edit this page")

# Interrupt [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/\#interrupt "Permanent link")

This guide assumes knowledge of what double-texting is, which you can learn about in the [double-texting conceptual guide](https://langchain-ai.github.io/langgraph/concepts/double_texting/).

The guide covers the `interrupt` option for double texting, which interrupts the prior run of the graph and starts a new one with the double-text. This option does not delete the first run, but rather keeps it in the database but sets its status to `interrupted`. Below is a quick example of using the `interrupt` option.

## Setup [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/\#setup "Permanent link")

First, we will define a quick helper function for printing out JS and CURL model outputs (you can skip this if using Python):

[Javascript](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__tabbed_1_1)[CURL](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__tabbed_1_2)

```md-code__content
function prettyPrint(m) {
  const padded = " " + m['type'] + " ";
  const sepLen = Math.floor((80 - padded.length) / 2);
  const sep = "=".repeat(sepLen);
  const secondSep = sep + (padded.length % 2 ? "=" : "");

  console.log(`${sep}${padded}${secondSep}`);
  console.log("\n\n");
  console.log(m.content);
}

```

```md-code__content
# PLACE THIS IN A FILE CALLED pretty_print.sh
pretty_print() {
  local type="$1"
  local content="$2"
  local padded=" $type "
  local total_width=80
  local sep_len=$(( (total_width - ${#padded}) / 2 ))
  local sep=$(printf '=%.0s' $(eval "echo {1.."${sep_len}"}"))
  local second_sep=$sep
  if (( (total_width - ${#padded}) % 2 )); then
    second_sep="${second_sep}="
  fi

  echo "${sep}${padded}${second_sep}"
  echo
  echo "$content"
}

```

Now, let's import our required packages and instantiate our client, assistant, and thread.

[Python](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__tabbed_2_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__tabbed_2_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__tabbed_2_3)

```md-code__content
import asyncio

from langchain_core.messages import convert_to_messages
from langgraph_sdk import get_client

client = get_client(url=<DEPLOYMENT_URL>)
# Using the graph deployed with the name "agent"
assistant_id = "agent"
thread = await client.threads.create()

```

```md-code__content
import { Client } from "@langchain/langgraph-sdk";

const client = new Client({ apiUrl: <DEPLOYMENT_URL> });
// Using the graph deployed with the name "agent"
const assistantId = "agent";
const thread = await client.threads.create();

```

```md-code__content
curl --request POST \
  --url <DEPLOYMENT_URL>/threads \
  --header 'Content-Type: application/json' \
  --data '{}'

```

## Create runs [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/\#create-runs "Permanent link")

Now we can start our two runs and join the second one until it has completed:

[Python](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__tabbed_3_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__tabbed_3_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__tabbed_3_3)

```md-code__content
# the first run will be interrupted
interrupted_run = await client.runs.create(
    thread["thread_id"],
    assistant_id,
    input={"messages": [{"role": "user", "content": "what's the weather in sf?"}]},
)
# sleep a bit to get partial outputs from the first run
await asyncio.sleep(2)
run = await client.runs.create(
    thread["thread_id"],
    assistant_id,
    input={"messages": [{"role": "user", "content": "what's the weather in nyc?"}]},
    multitask_strategy="interrupt",
)
# wait until the second run completes
await client.runs.join(thread["thread_id"], run["run_id"])

```

```md-code__content
// the first run will be interrupted
let interruptedRun = await client.runs.create(
  thread["thread_id"],
  assistantId,
  { input: { messages: [{ role: "human", content: "what's the weather in sf?" }] } }
);
// sleep a bit to get partial outputs from the first run
await new Promise(resolve => setTimeout(resolve, 2000));

let run = await client.runs.create(
  thread["thread_id"],
  assistantId,
  {
    input: { messages: [{ role: "human", content: "what's the weather in nyc?" }] },
    multitaskStrategy: "interrupt"
  }
);

// wait until the second run completes
await client.runs.join(thread["thread_id"], run["run_id"]);

```

```md-code__content
curl --request POST \
--url <DEPLOY<ENT_URL>>/threads/<THREAD_ID>/runs \
--header 'Content-Type: application/json' \
--data "{
  \"assistant_id\": \"agent\",
  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what\'s the weather in sf?\"}]},
}" && sleep 2 && curl --request POST \
--url <DEPLOY<ENT_URL>>/threads/<THREAD_ID>/runs \
--header 'Content-Type: application/json' \
--data "{
  \"assistant_id\": \"agent\",
  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what\'s the weather in nyc?\"}]},
  \"multitask_strategy\": \"interrupt\"
}" && curl --request GET \
--url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>/join

```

## View run results [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/\#view-run-results "Permanent link")

We can see that the thread has partial data from the first run + data from the second run

[Python](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__tabbed_4_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__tabbed_4_2)[CURL](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__tabbed_4_3)

```md-code__content
state = await client.threads.get_state(thread["thread_id"])

for m in convert_to_messages(state["values"]["messages"]):
    m.pretty_print()

```

```md-code__content
const state = await client.threads.getState(thread["thread_id"]);

for (const m of state['values']['messages']) {
  prettyPrint(m);
}

```

```md-code__content
source pretty_print.sh && curl --request GET \
--url <DEPLOYMENT_URL>/threads/<THREAD_ID>/state | \
jq -c '.values.messages[]' | while read -r element; do
    type=$(echo "$element" | jq -r '.type')
    content=$(echo "$element" | jq -r '.content | if type == "array" then tostring else . end')
    pretty_print "$type" "$content"
done

```

Output:

```
================================ Human Message =================================

what's the weather in sf?
================================== Ai Message ==================================

[{'id': 'toolu_01MjNtVJwEcpujRGrf3x6Pih', 'input': {'query': 'weather in san francisco'}, 'name': 'tavily_search_results_json', 'type': 'tool_use'}]
Tool Calls:
  tavily_search_results_json (toolu_01MjNtVJwEcpujRGrf3x6Pih)
 Call ID: toolu_01MjNtVJwEcpujRGrf3x6Pih
  Args:
    query: weather in san francisco
================================= Tool Message =================================
Name: tavily_search_results_json

[{"url": "https://www.wunderground.com/hourly/us/ca/san-francisco/KCASANFR2002/date/2024-6-18", "content": "High 64F. Winds W at 10 to 20 mph. A few clouds from time to time. Low 49F. Winds W at 10 to 20 mph. Temp. San Francisco Weather Forecasts. Weather Underground provides local & long-range weather ..."}]
================================ Human Message =================================

what's the weather in nyc?
================================== Ai Message ==================================

[{'id': 'toolu_01KtE1m1ifPLQAx4fQLyZL9Q', 'input': {'query': 'weather in new york city'}, 'name': 'tavily_search_results_json', 'type': 'tool_use'}]
Tool Calls:
  tavily_search_results_json (toolu_01KtE1m1ifPLQAx4fQLyZL9Q)
 Call ID: toolu_01KtE1m1ifPLQAx4fQLyZL9Q
  Args:
    query: weather in new york city
================================= Tool Message =================================
Name: tavily_search_results_json

[{"url": "https://www.accuweather.com/en/us/new-york/10021/june-weather/349727", "content": "Get the monthly weather forecast for New York, NY, including daily high/low, historical averages, to help you plan ahead."}]
================================== Ai Message ==================================

The search results provide weather forecasts and information for New York City. Based on the top result from AccuWeather, here are some key details about the weather in NYC:

- This is a monthly weather forecast for New York City for the month of June.
- It includes daily high and low temperatures to help plan ahead.
- Historical averages for June in NYC are also provided as a reference point.
- More detailed daily or hourly forecasts with precipitation chances, humidity, wind, etc. can be found by visiting the AccuWeather page.

So in summary, the search provides a convenient overview of the expected weather conditions in New York City over the next month to give you an idea of what to prepare for if traveling or making plans there. Let me know if you need any other details!

```

Verify that the original, interrupted run was interrupted

[Python](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__tabbed_5_1)[Javascript](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__tabbed_5_2)

```md-code__content
print((await client.runs.get(thread["thread_id"], interrupted_run["run_id"]))["status"])

```

```md-code__content
console.log((await client.runs.get(thread['thread_id'], interruptedRun["run_id"]))["status"])

```

Output:

```
'interrupted'

```

## Comments

giscus

#### 0 reactions

#### 0 comments

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fhow-tos%2Finterrupt_concurrent%2F)