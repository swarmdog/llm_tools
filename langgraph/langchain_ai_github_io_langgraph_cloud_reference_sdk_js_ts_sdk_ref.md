[Skip to content](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#langchainlanggraph-sdk)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/reference/sdk/js_ts_sdk_ref.md "Edit this page")

# SDK (JS/TS)

**[@langchain/langgraph-sdk](https://github.com/langchain-ai/langgraph/tree/main/libs/sdk-js)**

* * *

## [@langchain/langgraph-sdk](https://github.com/langchain-ai/langgraph/tree/main/libs/sdk-js) [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#langchainlanggraph-sdk "Permanent link")

### Classes [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#classes "Permanent link")

- [AssistantsClient](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesassistantsclientmd)
- [Client](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesclientmd)
- [CronsClient](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classescronsclientmd)
- [RunsClient](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesrunsclientmd)
- [StoreClient](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesstoreclientmd)
- [ThreadsClient](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesthreadsclientmd)

### Interfaces [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#interfaces "Permanent link")

- [ClientConfig](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#interfacesclientconfigmd)

### Functions [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#functions "Permanent link")

- [getApiKey](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#functionsgetapikeymd)

[**@langchain/langgraph-sdk**](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd)

* * *

[@langchain/langgraph-sdk](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd) / AssistantsClient

## Class: AssistantsClient [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#class-assistantsclient "Permanent link")

Defined in: [client.ts:270](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L270)

### Extends [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#extends "Permanent link")

- `BaseClient`

### Constructors [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#constructors "Permanent link")

#### new AssistantsClient() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#new-assistantsclient "Permanent link")

> **new AssistantsClient**( `config`?): [`AssistantsClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesassistantsclientmd)

Defined in: [client.ts:85](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L85)

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters "Permanent link")

###### config? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#config "Permanent link")

[`ClientConfig`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#interfacesclientconfigmd)

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns "Permanent link")

[`AssistantsClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesassistantsclientmd)

##### Inherited from [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#inherited-from "Permanent link")

`BaseClient.constructor`

### Methods [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#methods "Permanent link")

#### create() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#create "Permanent link")

> **create**( `payload`): `Promise`\\< `Assistant` >

Defined in: [client.ts:335](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L335)

Create a new assistant.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_1 "Permanent link")

###### payload [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#payload "Permanent link")

Payload for creating an assistant.

###### \\# assistantId? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid "Permanent link")

`string`

###### \\# config? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#config_1 "Permanent link")

`Config`

###### \\# graphId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#graphid "Permanent link")

`string`

###### \\# ifExists? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#ifexists "Permanent link")

`OnConflictBehavior`

###### \\# metadata? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#metadata "Permanent link")

`Metadata`

###### \\# name? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#name "Permanent link")

`string`

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_1 "Permanent link")

`Promise`\\< `Assistant` >

The created assistant.

* * *

#### delete() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#delete "Permanent link")

> **delete**( `assistantId`): `Promise`\\< `void` >

Defined in: [client.ts:387](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L387)

Delete an assistant.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_2 "Permanent link")

###### assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_1 "Permanent link")

`string`

ID of the assistant.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_2 "Permanent link")

`Promise`\\< `void` >

* * *

#### get() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#get "Permanent link")

> **get**( `assistantId`): `Promise`\\< `Assistant` >

Defined in: [client.ts:277](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L277)

Get an assistant by ID.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_3 "Permanent link")

###### assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_2 "Permanent link")

`string`

The ID of the assistant.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_3 "Permanent link")

`Promise`\\< `Assistant` >

Assistant

* * *

#### getGraph() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#getgraph "Permanent link")

> **getGraph**( `assistantId`, `options`?): `Promise`\\< `AssistantGraph` >

Defined in: [client.ts:287](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L287)

Get the JSON representation of the graph assigned to a runnable

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_4 "Permanent link")

###### assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_3 "Permanent link")

`string`

The ID of the assistant.

###### options? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#options "Permanent link")

###### \\# xray? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#xray "Permanent link")

`number` \| `boolean`

Whether to include subgraphs in the serialized graph representation. If an integer value is provided, only subgraphs with a depth less than or equal to the value will be included.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_4 "Permanent link")

`Promise`\\< `AssistantGraph` >

Serialized graph

* * *

#### getSchemas() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#getschemas "Permanent link")

> **getSchemas**( `assistantId`): `Promise`\\< `GraphSchema` >

Defined in: [client.ts:301](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L301)

Get the state and config schema of the graph assigned to a runnable

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_5 "Permanent link")

###### assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_4 "Permanent link")

`string`

The ID of the assistant.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_5 "Permanent link")

`Promise`\\< `GraphSchema` >

Graph schema

* * *

#### getSubgraphs() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#getsubgraphs "Permanent link")

> **getSubgraphs**( `assistantId`, `options`?): `Promise`\\< `Subgraphs` >

Defined in: [client.ts:312](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L312)

Get the schemas of an assistant by ID.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_6 "Permanent link")

###### assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_5 "Permanent link")

`string`

The ID of the assistant to get the schema of.

###### options? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#options_1 "Permanent link")

Additional options for getting subgraphs, such as namespace or recursion extraction.

###### \\# namespace? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#namespace "Permanent link")

`string`

###### \\# recurse? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#recurse "Permanent link")

`boolean`

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_6 "Permanent link")

`Promise`\\< `Subgraphs` >

The subgraphs of the assistant.

* * *

#### getVersions() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#getversions "Permanent link")

> **getVersions**( `assistantId`, `payload`?): `Promise`\\< `AssistantVersion`\[\]>

Defined in: [client.ts:421](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L421)

List all versions of an assistant.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_7 "Permanent link")

###### assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_6 "Permanent link")

`string`

ID of the assistant.

###### payload? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#payload_1 "Permanent link")

###### \\# limit? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#limit "Permanent link")

`number`

###### \\# metadata? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#metadata_1 "Permanent link")

`Metadata`

###### \\# offset? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#offset "Permanent link")

`number`

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_7 "Permanent link")

`Promise`\\< `AssistantVersion`\[\]>

List of assistant versions.

* * *

#### search() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#search "Permanent link")

> **search**( `query`?): `Promise`\\< `Assistant`\[\]>

Defined in: [client.ts:398](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L398)

List assistants.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_8 "Permanent link")

###### query? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#query "Permanent link")

Query options.

###### \\# graphId? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#graphid_1 "Permanent link")

`string`

###### \\# limit? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#limit_1 "Permanent link")

`number`

###### \\# metadata? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#metadata_2 "Permanent link")

`Metadata`

###### \\# offset? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#offset_1 "Permanent link")

`number`

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_8 "Permanent link")

`Promise`\\< `Assistant`\[\]>

List of assistants.

* * *

#### setLatest() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#setlatest "Permanent link")

> **setLatest**( `assistantId`, `version`): `Promise`\\< `Assistant` >

Defined in: [client.ts:449](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L449)

Change the version of an assistant.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_9 "Permanent link")

###### assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_7 "Permanent link")

`string`

ID of the assistant.

###### version [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#version "Permanent link")

`number`

The version to change to.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_9 "Permanent link")

`Promise`\\< `Assistant` >

The updated assistant.

* * *

#### update() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#update "Permanent link")

> **update**( `assistantId`, `payload`): `Promise`\\< `Assistant` >

Defined in: [client.ts:362](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L362)

Update an assistant.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_10 "Permanent link")

###### assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_8 "Permanent link")

`string`

ID of the assistant.

###### payload [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#payload_2 "Permanent link")

Payload for updating the assistant.

###### \\# config? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#config_2 "Permanent link")

`Config`

###### \\# graphId? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#graphid_2 "Permanent link")

`string`

###### \\# metadata? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#metadata_3 "Permanent link")

`Metadata`

###### \\# name? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#name_1 "Permanent link")

`string`

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_10 "Permanent link")

`Promise`\\< `Assistant` >

The updated assistant.

[**@langchain/langgraph-sdk**](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd)

* * *

[@langchain/langgraph-sdk](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd) / Client

## Class: Client\\<TStateType, TUpdateType, TCustomEventType> [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#class-clienttstatetype-tupdatetype-tcustomeventtype "Permanent link")

Defined in: [client.ts:1370](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1370)

### Type Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-parameters "Permanent link")

• **TStateType** = `DefaultValues`

• **TUpdateType** = `TStateType`

• **TCustomEventType** = `unknown`

### Constructors [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#constructors_1 "Permanent link")

#### new Client() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#new-client "Permanent link")

> **new Client**\\< `TStateType`, `TUpdateType`, `TCustomEventType` >( `config`?): [`Client`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesclientmd)\\< `TStateType`, `TUpdateType`, `TCustomEventType` >

Defined in: [client.ts:1406](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1406)

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_11 "Permanent link")

###### config? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#config_3 "Permanent link")

[`ClientConfig`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#interfacesclientconfigmd)

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_11 "Permanent link")

[`Client`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesclientmd)\\< `TStateType`, `TUpdateType`, `TCustomEventType` >

### Properties [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#properties "Permanent link")

#### ~ui [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#ui "Permanent link")

> **~ui**: `UiClient`

Defined in: [client.ts:1404](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1404)

**`Internal`**

The client for interacting with the UI.
Used by LoadExternalComponent and the API might change in the future.

* * *

#### assistants [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistants "Permanent link")

> **assistants**: [`AssistantsClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesassistantsclientmd)

Defined in: [client.ts:1378](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1378)

The client for interacting with assistants.

* * *

#### crons [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#crons "Permanent link")

> **crons**: [`CronsClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classescronsclientmd)

Defined in: [client.ts:1393](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1393)

The client for interacting with cron runs.

* * *

#### runs [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#runs "Permanent link")

> **runs**: [`RunsClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesrunsclientmd)\\< `TStateType`, `TUpdateType`, `TCustomEventType` >

Defined in: [client.ts:1388](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1388)

The client for interacting with runs.

* * *

#### store [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#store "Permanent link")

> **store**: [`StoreClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesstoreclientmd)

Defined in: [client.ts:1398](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1398)

The client for interacting with the KV store.

* * *

#### threads [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threads "Permanent link")

> **threads**: [`ThreadsClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesthreadsclientmd)\\< `TStateType`, `TUpdateType` >

Defined in: [client.ts:1383](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1383)

The client for interacting with threads.

[**@langchain/langgraph-sdk**](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd)

* * *

[@langchain/langgraph-sdk](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd) / CronsClient

## Class: CronsClient [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#class-cronsclient "Permanent link")

Defined in: [client.ts:175](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L175)

### Extends [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#extends_1 "Permanent link")

- `BaseClient`

### Constructors [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#constructors_2 "Permanent link")

#### new CronsClient() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#new-cronsclient "Permanent link")

> **new CronsClient**( `config`?): [`CronsClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classescronsclientmd)

Defined in: [client.ts:85](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L85)

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_12 "Permanent link")

###### config? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#config_4 "Permanent link")

[`ClientConfig`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#interfacesclientconfigmd)

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_12 "Permanent link")

[`CronsClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classescronsclientmd)

##### Inherited from [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#inherited-from_1 "Permanent link")

`BaseClient.constructor`

### Methods [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#methods_1 "Permanent link")

#### create() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#create_1 "Permanent link")

> **create**( `assistantId`, `payload`?): `Promise`\\< `CronCreateResponse` >

Defined in: [client.ts:215](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L215)

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_13 "Permanent link")

###### assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_9 "Permanent link")

`string`

Assistant ID to use for this cron job.

###### payload? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#payload_3 "Permanent link")

`CronsCreatePayload`

Payload for creating a cron job.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_13 "Permanent link")

`Promise`\\< `CronCreateResponse` >

* * *

#### createForThread() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#createforthread "Permanent link")

> **createForThread**( `threadId`, `assistantId`, `payload`?): `Promise`\\< `CronCreateForThreadResponse` >

Defined in: [client.ts:183](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L183)

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_14 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid "Permanent link")

`string`

The ID of the thread.

###### assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_10 "Permanent link")

`string`

Assistant ID to use for this cron job.

###### payload? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#payload_4 "Permanent link")

`CronsCreatePayload`

Payload for creating a cron job.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_14 "Permanent link")

`Promise`\\< `CronCreateForThreadResponse` >

The created background run.

* * *

#### delete() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#delete_1 "Permanent link")

> **delete**( `cronId`): `Promise`\\< `void` >

Defined in: [client.ts:241](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L241)

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_15 "Permanent link")

###### cronId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#cronid "Permanent link")

`string`

Cron ID of Cron job to delete.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_15 "Permanent link")

`Promise`\\< `void` >

* * *

#### search() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#search_1 "Permanent link")

> **search**( `query`?): `Promise`\\< `Cron`\[\]>

Defined in: [client.ts:252](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L252)

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_16 "Permanent link")

###### query? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#query_1 "Permanent link")

Query options.

###### \\# assistantId? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_11 "Permanent link")

`string`

###### \\# limit? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#limit_2 "Permanent link")

`number`

###### \\# offset? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#offset_2 "Permanent link")

`number`

###### \\# threadId? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_1 "Permanent link")

`string`

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_16 "Permanent link")

`Promise`\\< `Cron`\[\]>

List of crons.

[**@langchain/langgraph-sdk**](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd)

* * *

[@langchain/langgraph-sdk](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd) / RunsClient

## Class: RunsClient\\<TStateType, TUpdateType, TCustomEventType> [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#class-runsclienttstatetype-tupdatetype-tcustomeventtype "Permanent link")

Defined in: [client.ts:701](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L701)

### Extends [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#extends_2 "Permanent link")

- `BaseClient`

### Type Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-parameters_1 "Permanent link")

• **TStateType** = `DefaultValues`

• **TUpdateType** = `TStateType`

• **TCustomEventType** = `unknown`

### Constructors [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#constructors_3 "Permanent link")

#### new RunsClient() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#new-runsclient "Permanent link")

> **new RunsClient**\\< `TStateType`, `TUpdateType`, `TCustomEventType` >( `config`?): [`RunsClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesrunsclientmd)\\< `TStateType`, `TUpdateType`, `TCustomEventType` >

Defined in: [client.ts:85](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L85)

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_17 "Permanent link")

###### config? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#config_5 "Permanent link")

[`ClientConfig`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#interfacesclientconfigmd)

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_17 "Permanent link")

[`RunsClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesrunsclientmd)\\< `TStateType`, `TUpdateType`, `TCustomEventType` >

##### Inherited from [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#inherited-from_2 "Permanent link")

`BaseClient.constructor`

### Methods [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#methods_2 "Permanent link")

#### cancel() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#cancel "Permanent link")

> **cancel**( `threadId`, `runId`, `wait`, `action`): `Promise`\\< `void` >

Defined in: [client.ts:985](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L985)

Cancel a run.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_18 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_2 "Permanent link")

`string`

The ID of the thread.

###### runId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#runid "Permanent link")

`string`

The ID of the run.

###### wait [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#wait "Permanent link")

`boolean` = `false`

Whether to block when canceling

###### action [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#action "Permanent link")

`CancelAction` = `"interrupt"`

Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. Default is `interrupt`.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_18 "Permanent link")

`Promise`\\< `void` >

* * *

#### create() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#create_2 "Permanent link")

> **create**( `threadId`, `assistantId`, `payload`?): `Promise`\\< `Run` >

Defined in: [client.ts:809](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L809)

Create a run.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_19 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_3 "Permanent link")

`string`

The ID of the thread.

###### assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_12 "Permanent link")

`string`

Assistant ID to use for this run.

###### payload? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#payload_5 "Permanent link")

`RunsCreatePayload`

Payload for creating a run.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_19 "Permanent link")

`Promise`\\< `Run` >

The created run.

* * *

#### createBatch() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#createbatch "Permanent link")

> **createBatch**( `payloads`): `Promise`\\< `Run`\[\]>

Defined in: [client.ts:844](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L844)

Create a batch of stateless background runs.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_20 "Permanent link")

###### payloads [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#payloads "Permanent link")

`RunsCreatePayload` & `object`\[\]

An array of payloads for creating runs.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_20 "Permanent link")

`Promise`\\< `Run`\[\]>

An array of created runs.

* * *

#### delete() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#delete_2 "Permanent link")

> **delete**( `threadId`, `runId`): `Promise`\\< `void` >

Defined in: [client.ts:1079](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1079)

Delete a run.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_21 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_4 "Permanent link")

`string`

The ID of the thread.

###### runId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#runid_1 "Permanent link")

`string`

The ID of the run.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_21 "Permanent link")

`Promise`\\< `void` >

* * *

#### get() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#get_1 "Permanent link")

> **get**( `threadId`, `runId`): `Promise`\\< `Run` >

Defined in: [client.ts:972](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L972)

Get a run by ID.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_22 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_5 "Permanent link")

`string`

The ID of the thread.

###### runId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#runid_2 "Permanent link")

`string`

The ID of the run.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_22 "Permanent link")

`Promise`\\< `Run` >

The run.

* * *

#### join() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#join "Permanent link")

> **join**( `threadId`, `runId`, `options`?): `Promise`\\< `void` >

Defined in: [client.ts:1007](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1007)

Block until a run is done.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_23 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_6 "Permanent link")

`string`

The ID of the thread.

###### runId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#runid_3 "Permanent link")

`string`

The ID of the run.

###### options? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#options_2 "Permanent link")

###### \\# signal? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#signal "Permanent link")

`AbortSignal`

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_23 "Permanent link")

`Promise`\\< `void` >

* * *

#### joinStream() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#joinstream "Permanent link")

> **joinStream**( `threadId`, `runId`, `options`?): `AsyncGenerator`\\<{ `data`: `any`; `event`: `StreamEvent`; }>

Defined in: [client.ts:1033](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1033)

Stream output from a run in real-time, until the run is done.
Output is not buffered, so any output produced before this call will
not be received here.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_24 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_7 "Permanent link")

`string`

The ID of the thread.

###### runId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#runid_4 "Permanent link")

`string`

The ID of the run.

###### options? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#options_3 "Permanent link")

Additional options for controlling the stream behavior:
\- signal: An AbortSignal that can be used to cancel the stream request
\- cancelOnDisconnect: When true, automatically cancels the run if the client disconnects from the stream
\- streamMode: Controls what types of events to receive from the stream (can be a single mode or array of modes)
Must be a subset of the stream modes passed when creating the run. Background runs default to having the union of all
stream modes enabled.

`AbortSignal` \| { `cancelOnDisconnect`: `boolean`; `signal`: `AbortSignal`; `streamMode`: `StreamMode` \| `StreamMode`\[\]; }

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_24 "Permanent link")

`AsyncGenerator`\\<{ `data`: `any`; `event`: `StreamEvent`; }>

An async generator yielding stream parts.

* * *

#### list() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#list "Permanent link")

> **list**( `threadId`, `options`?): `Promise`\\< `Run`\[\]>

Defined in: [client.ts:935](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L935)

List all runs for a thread.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_25 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_8 "Permanent link")

`string`

The ID of the thread.

###### options? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#options_4 "Permanent link")

Filtering and pagination options.

###### \\# limit? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#limit_3 "Permanent link")

`number`

Maximum number of runs to return.
Defaults to 10

###### \\# offset? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#offset_3 "Permanent link")

`number`

Offset to start from.
Defaults to 0.

###### \\# status? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#status "Permanent link")

`RunStatus`

Status of the run to filter by.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_25 "Permanent link")

`Promise`\\< `Run`\[\]>

List of runs.

* * *

#### stream() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#stream "Permanent link")

Create a run and stream the results.

##### Param [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#param "Permanent link")

The ID of the thread.

##### Param [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#param_1 "Permanent link")

Assistant ID to use for this run.

##### Param [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#param_2 "Permanent link")

Payload for creating a run.

##### Call Signature [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#call-signature "Permanent link")

> **stream**\\< `TStreamMode`, `TSubgraphs` >( `threadId`, `assistantId`, `payload`?): `TypedAsyncGenerator`\\< `TStreamMode`, `TSubgraphs`, `TStateType`, `TUpdateType`, `TCustomEventType` >

Defined in: [client.ts:706](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L706)

###### Type Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-parameters_2 "Permanent link")

• **TStreamMode** _extends_ `StreamMode` \| `StreamMode`\[\] = `StreamMode`

• **TSubgraphs** _extends_ `boolean` = `false`

###### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_26 "Permanent link")

###### \\# threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_9 "Permanent link")

`null`

###### \\# assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_13 "Permanent link")

`string`

###### \\# payload? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#payload_6 "Permanent link")

`Omit`\\< `RunsStreamPayload`\\< `TStreamMode`, `TSubgraphs` >, `"multitaskStrategy"` \| `"onCompletion"` >

###### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_26 "Permanent link")

`TypedAsyncGenerator`\\< `TStreamMode`, `TSubgraphs`, `TStateType`, `TUpdateType`, `TCustomEventType` >

##### Call Signature [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#call-signature_1 "Permanent link")

> **stream**\\< `TStreamMode`, `TSubgraphs` >( `threadId`, `assistantId`, `payload`?): `TypedAsyncGenerator`\\< `TStreamMode`, `TSubgraphs`, `TStateType`, `TUpdateType`, `TCustomEventType` >

Defined in: [client.ts:724](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L724)

###### Type Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-parameters_3 "Permanent link")

• **TStreamMode** _extends_ `StreamMode` \| `StreamMode`\[\] = `StreamMode`

• **TSubgraphs** _extends_ `boolean` = `false`

###### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_27 "Permanent link")

###### \\# threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_10 "Permanent link")

`string`

###### \\# assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_14 "Permanent link")

`string`

###### \\# payload? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#payload_7 "Permanent link")

`RunsStreamPayload`\\< `TStreamMode`, `TSubgraphs` >

###### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_27 "Permanent link")

`TypedAsyncGenerator`\\< `TStreamMode`, `TSubgraphs`, `TStateType`, `TUpdateType`, `TCustomEventType` >

* * *

#### wait() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#wait_1 "Permanent link")

Create a run and wait for it to complete.

##### Param [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#param_3 "Permanent link")

The ID of the thread.

##### Param [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#param_4 "Permanent link")

Assistant ID to use for this run.

##### Param [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#param_5 "Permanent link")

Payload for creating a run.

##### Call Signature [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#call-signature_2 "Permanent link")

> **wait**( `threadId`, `assistantId`, `payload`?): `Promise`\\< `DefaultValues` >

Defined in: [client.ts:861](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L861)

###### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_28 "Permanent link")

###### \\# threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_11 "Permanent link")

`null`

###### \\# assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_15 "Permanent link")

`string`

###### \\# payload? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#payload_8 "Permanent link")

`Omit`\\< `RunsWaitPayload`, `"multitaskStrategy"` \| `"onCompletion"` >

###### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_28 "Permanent link")

`Promise`\\< `DefaultValues` >

##### Call Signature [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#call-signature_3 "Permanent link")

> **wait**( `threadId`, `assistantId`, `payload`?): `Promise`\\< `DefaultValues` >

Defined in: [client.ts:867](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L867)

###### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_29 "Permanent link")

###### \\# threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_12 "Permanent link")

`string`

###### \\# assistantId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#assistantid_16 "Permanent link")

`string`

###### \\# payload? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#payload_9 "Permanent link")

`RunsWaitPayload`

###### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_29 "Permanent link")

`Promise`\\< `DefaultValues` >

[**@langchain/langgraph-sdk**](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd)

* * *

[@langchain/langgraph-sdk](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd) / StoreClient

## Class: StoreClient [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#class-storeclient "Permanent link")

Defined in: [client.ts:1097](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1097)

### Extends [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#extends_3 "Permanent link")

- `BaseClient`

### Constructors [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#constructors_4 "Permanent link")

#### new StoreClient() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#new-storeclient "Permanent link")

> **new StoreClient**( `config`?): [`StoreClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesstoreclientmd)

Defined in: [client.ts:85](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L85)

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_30 "Permanent link")

###### config? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#config_6 "Permanent link")

[`ClientConfig`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#interfacesclientconfigmd)

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_30 "Permanent link")

[`StoreClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesstoreclientmd)

##### Inherited from [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#inherited-from_3 "Permanent link")

`BaseClient.constructor`

### Methods [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#methods_3 "Permanent link")

#### deleteItem() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#deleteitem "Permanent link")

> **deleteItem**( `namespace`, `key`): `Promise`\\< `void` >

Defined in: [client.ts:1218](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1218)

Delete an item.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_31 "Permanent link")

###### namespace [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#namespace_1 "Permanent link")

`string`\[\]

A list of strings representing the namespace path.

###### key [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#key "Permanent link")

`string`

The unique identifier for the item.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_31 "Permanent link")

`Promise`\\< `void` >

Promise

* * *

#### getItem() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#getitem "Permanent link")

> **getItem**( `namespace`, `key`, `options`?): `Promise`\\< `null` \| `Item` >

Defined in: [client.ts:1174](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1174)

Retrieve a single item.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_32 "Permanent link")

###### namespace [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#namespace_2 "Permanent link")

`string`\[\]

A list of strings representing the namespace path.

###### key [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#key_1 "Permanent link")

`string`

The unique identifier for the item.

###### options? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#options_5 "Permanent link")

###### \\# refreshTtl? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#refreshttl "Permanent link")

`null` \| `boolean`

Whether to refresh the TTL on this read operation. If null, uses the store's default behavior.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_32 "Permanent link")

`Promise`\\< `null` \| `Item` >

Promise

##### Example [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#example "Permanent link")

```md-code__content
const item = await client.store.getItem(
  ["documents", "user123"],
  "item456",
  { refreshTtl: true }
);
console.log(item);
// {
//   namespace: ["documents", "user123"],
//   key: "item456",
//   value: { title: "My Document", content: "Hello World" },
//   createdAt: "2024-07-30T12:00:00Z",
//   updatedAt: "2024-07-30T12:00:00Z"
// }

```

* * *

#### listNamespaces() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#listnamespaces "Permanent link")

> **listNamespaces**( `options`?): `Promise`\\< `ListNamespaceResponse` >

Defined in: [client.ts:1314](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1314)

List namespaces with optional match conditions.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_33 "Permanent link")

###### options? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#options_6 "Permanent link")

###### \\# limit? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#limit_4 "Permanent link")

`number`

Maximum number of namespaces to return (default is 100).

###### \\# maxDepth? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#maxdepth "Permanent link")

`number`

Optional integer specifying the maximum depth of namespaces to return.

###### \\# offset? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#offset_4 "Permanent link")

`number`

Number of namespaces to skip before returning results (default is 0).

###### \\# prefix? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#prefix "Permanent link")

`string`\[\]

Optional list of strings representing the prefix to filter namespaces.

###### \\# suffix? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#suffix "Permanent link")

`string`\[\]

Optional list of strings representing the suffix to filter namespaces.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_33 "Permanent link")

`Promise`\\< `ListNamespaceResponse` >

Promise

* * *

#### putItem() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#putitem "Permanent link")

> **putItem**( `namespace`, `key`, `value`, `options`?): `Promise`\\< `void` >

Defined in: [client.ts:1118](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1118)

Store or update an item.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_34 "Permanent link")

###### namespace [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#namespace_3 "Permanent link")

`string`\[\]

A list of strings representing the namespace path.

###### key [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#key_2 "Permanent link")

`string`

The unique identifier for the item within the namespace.

###### value [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#value "Permanent link")

`Record`\\< `string`, `any` >

A dictionary containing the item's data.

###### options? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#options_7 "Permanent link")

###### \\# index? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#index "Permanent link")

`null` \| `false` \| `string`\[\]

Controls search indexing - null (use defaults), false (disable), or list of field paths to index.

###### \\# ttl? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#ttl "Permanent link")

`null` \| `number`

Optional time-to-live in minutes for the item, or null for no expiration.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_34 "Permanent link")

`Promise`\\< `void` >

Promise

##### Example [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#example_1 "Permanent link")

```md-code__content
await client.store.putItem(
  ["documents", "user123"],
  "item456",
  { title: "My Document", content: "Hello World" },
  { ttl: 60 } // expires in 60 minutes
);

```

* * *

#### searchItems() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#searchitems "Permanent link")

> **searchItems**( `namespacePrefix`, `options`?): `Promise`\\< `SearchItemsResponse` >

Defined in: [client.ts:1269](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L1269)

Search for items within a namespace prefix.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_35 "Permanent link")

###### namespacePrefix [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#namespaceprefix "Permanent link")

`string`\[\]

List of strings representing the namespace prefix.

###### options? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#options_8 "Permanent link")

###### \\# filter? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#filter "Permanent link")

`Record`\\< `string`, `any` >

Optional dictionary of key-value pairs to filter results.

###### \\# limit? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#limit_5 "Permanent link")

`number`

Maximum number of items to return (default is 10).

###### \\# offset? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#offset_5 "Permanent link")

`number`

Number of items to skip before returning results (default is 0).

###### \\# query? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#query_2 "Permanent link")

`string`

Optional search query.

###### \\# refreshTtl? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#refreshttl_1 "Permanent link")

`null` \| `boolean`

Whether to refresh the TTL on items returned by this search. If null, uses the store's default behavior.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_35 "Permanent link")

`Promise`\\< `SearchItemsResponse` >

Promise

##### Example [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#example_2 "Permanent link")

```md-code__content
const results = await client.store.searchItems(
  ["documents"],
  {
    filter: { author: "John Doe" },
    limit: 5,
    refreshTtl: true
  }
);
console.log(results);
// {
//   items: [\
//     {\
//       namespace: ["documents", "user123"],\
//       key: "item789",\
//       value: { title: "Another Document", author: "John Doe" },\
//       createdAt: "2024-07-30T12:00:00Z",\
//       updatedAt: "2024-07-30T12:00:00Z"\
//     },\
//     // ... additional items ...\
//   ]
// }

```

[**@langchain/langgraph-sdk**](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd)

* * *

[@langchain/langgraph-sdk](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd) / ThreadsClient

## Class: ThreadsClient\\<TStateType, TUpdateType> [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#class-threadsclienttstatetype-tupdatetype "Permanent link")

Defined in: [client.ts:457](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L457)

### Extends [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#extends_4 "Permanent link")

- `BaseClient`

### Type Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-parameters_4 "Permanent link")

• **TStateType** = `DefaultValues`

• **TUpdateType** = `TStateType`

### Constructors [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#constructors_5 "Permanent link")

#### new ThreadsClient() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#new-threadsclient "Permanent link")

> **new ThreadsClient**\\< `TStateType`, `TUpdateType` >( `config`?): [`ThreadsClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesthreadsclientmd)\\< `TStateType`, `TUpdateType` >

Defined in: [client.ts:85](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L85)

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_36 "Permanent link")

###### config? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#config_7 "Permanent link")

[`ClientConfig`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#interfacesclientconfigmd)

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_36 "Permanent link")

[`ThreadsClient`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#classesthreadsclientmd)\\< `TStateType`, `TUpdateType` >

##### Inherited from [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#inherited-from_4 "Permanent link")

`BaseClient.constructor`

### Methods [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#methods_4 "Permanent link")

#### copy() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#copy "Permanent link")

> **copy**( `threadId`): `Promise`\\< `Thread`\\< `TStateType` >>

Defined in: [client.ts:502](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L502)

Copy an existing thread

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_37 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_13 "Permanent link")

`string`

ID of the thread to be copied

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_37 "Permanent link")

`Promise`\\< `Thread`\\< `TStateType` >>

Newly copied thread

* * *

#### create() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#create_3 "Permanent link")

> **create**( `payload`?): `Promise`\\< `Thread`\\< `TStateType` >>

Defined in: [client.ts:479](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L479)

Create a new thread.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_38 "Permanent link")

###### payload? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#payload_10 "Permanent link")

Payload for creating a thread.

###### \\# ifExists? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#ifexists_1 "Permanent link")

`OnConflictBehavior`

###### \\# metadata? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#metadata_4 "Permanent link")

`Metadata`

Metadata for the thread.

###### \\# threadId? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_14 "Permanent link")

`string`

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_38 "Permanent link")

`Promise`\\< `Thread`\\< `TStateType` >>

The created thread.

* * *

#### delete() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#delete_3 "Permanent link")

> **delete**( `threadId`): `Promise`\\< `void` >

Defined in: [client.ts:535](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L535)

Delete a thread.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_39 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_15 "Permanent link")

`string`

ID of the thread.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_39 "Permanent link")

`Promise`\\< `void` >

* * *

#### get() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#get_2 "Permanent link")

> **get**\\< `ValuesType` >( `threadId`): `Promise`\\< `Thread`\\< `ValuesType` >>

Defined in: [client.ts:467](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L467)

Get a thread by ID.

##### Type Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-parameters_5 "Permanent link")

• **ValuesType** = `TStateType`

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_40 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_16 "Permanent link")

`string`

ID of the thread.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_40 "Permanent link")

`Promise`\\< `Thread`\\< `ValuesType` >>

The thread.

* * *

#### getHistory() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#gethistory "Permanent link")

> **getHistory**\\< `ValuesType` >( `threadId`, `options`?): `Promise`\\< `ThreadState`\\< `ValuesType` >\[\]>

Defined in: [client.ts:677](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L677)

Get all past states for a thread.

##### Type Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-parameters_6 "Permanent link")

• **ValuesType** = `TStateType`

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_41 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_17 "Permanent link")

`string`

ID of the thread.

###### options? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#options_9 "Permanent link")

Additional options.

###### \\# before? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#before "Permanent link")

`Config`

###### \\# checkpoint? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#checkpoint "Permanent link")

`Partial`\\< `Omit`\\< `Checkpoint`, `"thread_id"` >>

###### \\# limit? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#limit_6 "Permanent link")

`number`

###### \\# metadata? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#metadata_5 "Permanent link")

`Metadata`

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_41 "Permanent link")

`Promise`\\< `ThreadState`\\< `ValuesType` >\[\]>

List of thread states.

* * *

#### getState() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#getstate "Permanent link")

> **getState**\\< `ValuesType` >( `threadId`, `checkpoint`?, `options`?): `Promise`\\< `ThreadState`\\< `ValuesType` >>

Defined in: [client.ts:584](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L584)

Get state for a thread.

##### Type Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-parameters_7 "Permanent link")

• **ValuesType** = `TStateType`

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_42 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_18 "Permanent link")

`string`

ID of the thread.

###### checkpoint? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#checkpoint_1 "Permanent link")

`string` \| `Checkpoint`

###### options? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#options_10 "Permanent link")

###### \\# subgraphs? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#subgraphs "Permanent link")

`boolean`

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_42 "Permanent link")

`Promise`\\< `ThreadState`\\< `ValuesType` >>

Thread state.

* * *

#### patchState() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#patchstate "Permanent link")

> **patchState**( `threadIdOrConfig`, `metadata`): `Promise`\\< `void` >

Defined in: [client.ts:647](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L647)

Patch the metadata of a thread.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_43 "Permanent link")

###### threadIdOrConfig [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadidorconfig "Permanent link")

Thread ID or config to patch the state of.

`string` \| `Config`

###### metadata [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#metadata_6 "Permanent link")

`Metadata`

Metadata to patch the state with.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_43 "Permanent link")

`Promise`\\< `void` >

* * *

#### search() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#search_2 "Permanent link")

> **search**\\< `ValuesType` >( `query`?): `Promise`\\< `Thread`\\< `ValuesType` >\[\]>

Defined in: [client.ts:547](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L547)

List threads

##### Type Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-parameters_8 "Permanent link")

• **ValuesType** = `TStateType`

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_44 "Permanent link")

###### query? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#query_3 "Permanent link")

Query options

###### \\# limit? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#limit_7 "Permanent link")

`number`

Maximum number of threads to return.
Defaults to 10

###### \\# metadata? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#metadata_7 "Permanent link")

`Metadata`

Metadata to filter threads by.

###### \\# offset? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#offset_6 "Permanent link")

`number`

Offset to start from.

###### \\# status? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#status_1 "Permanent link")

`ThreadStatus`

Thread status to filter on.
Must be one of 'idle', 'busy', 'interrupted' or 'error'.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_44 "Permanent link")

`Promise`\\< `Thread`\\< `ValuesType` >\[\]>

List of threads

* * *

#### update() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#update_1 "Permanent link")

> **update**( `threadId`, `payload`?): `Promise`\\< `Thread`\\< `DefaultValues` >>

Defined in: [client.ts:515](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L515)

Update a thread.

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_45 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_19 "Permanent link")

`string`

ID of the thread.

###### payload? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#payload_11 "Permanent link")

Payload for updating the thread.

###### \\# metadata? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#metadata_8 "Permanent link")

`Metadata`

Metadata for the thread.

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_45 "Permanent link")

`Promise`\\< `Thread`\\< `DefaultValues` >>

The updated thread.

* * *

#### updateState() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#updatestate "Permanent link")

> **updateState**\\< `ValuesType` >( `threadId`, `options`): `Promise`\\< `Pick`\\< `Config`, `"configurable"` >>

Defined in: [client.ts:618](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L618)

Add state to a thread.

##### Type Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-parameters_9 "Permanent link")

• **ValuesType** = `TUpdateType`

##### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_46 "Permanent link")

###### threadId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#threadid_20 "Permanent link")

`string`

The ID of the thread.

###### options [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#options_11 "Permanent link")

###### \\# asNode? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#asnode "Permanent link")

`string`

###### \\# checkpoint? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#checkpoint_2 "Permanent link")

`Checkpoint`

###### \\# checkpointId? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#checkpointid "Permanent link")

`string`

###### \\# values [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#values "Permanent link")

`ValuesType`

##### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_46 "Permanent link")

`Promise`\\< `Pick`\\< `Config`, `"configurable"` >>

[**@langchain/langgraph-sdk**](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd)

* * *

[@langchain/langgraph-sdk](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd) / getApiKey

## Function: getApiKey() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#function-getapikey "Permanent link")

> **getApiKey**( `apiKey`?): `undefined` \| `string`

Defined in: [client.ts:50](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L50)

Get the API key from the environment.
Precedence:
1\. explicit argument
2\. LANGGRAPH\_API\_KEY
3\. LANGSMITH\_API\_KEY
4\. LANGCHAIN\_API\_KEY

### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_47 "Permanent link")

#### apiKey? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#apikey "Permanent link")

`string`

Optional API key provided as an argument

### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_47 "Permanent link")

`undefined` \| `string`

The API key if found, otherwise undefined

[**@langchain/langgraph-sdk**](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd)

* * *

[@langchain/langgraph-sdk](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#readmemd) / ClientConfig

## Interface: ClientConfig [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#interface-clientconfig "Permanent link")

Defined in: [client.ts:68](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L68)

### Properties [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#properties_1 "Permanent link")

#### apiKey? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#apikey_1 "Permanent link")

> `optional` **apiKey**: `string`

Defined in: [client.ts:70](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L70)

* * *

#### apiUrl? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#apiurl "Permanent link")

> `optional` **apiUrl**: `string`

Defined in: [client.ts:69](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L69)

* * *

#### callerOptions? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#calleroptions "Permanent link")

> `optional` **callerOptions**: `AsyncCallerParams`

Defined in: [client.ts:71](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L71)

* * *

#### defaultHeaders? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#defaultheaders "Permanent link")

> `optional` **defaultHeaders**: `Record`\\< `string`, `undefined` \| `null` \| `string` >

Defined in: [client.ts:73](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L73)

* * *

#### timeoutMs? [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#timeoutms "Permanent link")

> `optional` **timeoutMs**: `number`

Defined in: [client.ts:72](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/client.ts#L72)

**[langchain/langgraph-sdk](https://github.com/langchain/langgraph-sdk "GitHub Repository: langchain/langgraph-sdk")**

* * *

## [langchain/langgraph-sdk](https://github.com/langchain/langgraph-sdk "GitHub Repository: langchain/langgraph-sdk")/react [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#langchainlanggraph-sdkreact "Permanent link")

### Type Aliases [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-aliases "Permanent link")

- [MessageMetadata](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#reacttype-aliasesmessagemetadatamd)

### Functions [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#functions_1 "Permanent link")

- [useStream](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#reactfunctionsusestreammd)

[**@langchain/langgraph-sdk**](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#reactreadmemd)

* * *

[@langchain/langgraph-sdk](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#reactreadmemd) / useStream

## Function: useStream() [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#function-usestream "Permanent link")

> **useStream**\\< `StateType`, `Bag` >( `options`): `UseStream`\\< `StateType`, `Bag` >

Defined in: [stream.tsx:601](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/react/stream.tsx#L601)

### Type Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-parameters_10 "Permanent link")

• **StateType** _extends_ `Record`\\< `string`, `unknown` \> = `Record`\\< `string`, `unknown` >

• **Bag** _extends_ `object` = `BagTemplate`

### Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#parameters_48 "Permanent link")

#### options [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#options_12 "Permanent link")

`UseStreamOptions`\\< `StateType`, `Bag` >

### Returns [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#returns_48 "Permanent link")

`UseStream`\\< `StateType`, `Bag` >

[**@langchain/langgraph-sdk**](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#reactreadmemd)

* * *

[@langchain/langgraph-sdk](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#reactreadmemd) / MessageMetadata

## Type Alias: MessageMetadata\\<StateType> [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-alias-messagemetadatastatetype "Permanent link")

> **MessageMetadata**\\< `StateType` >: `object`

Defined in: [stream.tsx:169](https://github.com/langchain-ai/langgraph/blob/baedf91836c7cad7fceb44f8e689af169cbccb34/libs/sdk-js/src/react/stream.tsx#L169)

### Type Parameters [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-parameters_11 "Permanent link")

• **StateType** _extends_ `Record`\\< `string`, `unknown` >

### Type declaration [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#type-declaration "Permanent link")

#### branch [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#branch "Permanent link")

> **branch**: `string` \| `undefined`

The branch of the message.

#### branchOptions [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#branchoptions "Permanent link")

> **branchOptions**: `string`\[\] \| `undefined`

The list of branches this message is part of.
This is useful for displaying branching controls.

#### firstSeenState [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#firstseenstate "Permanent link")

> **firstSeenState**: `ThreadState`\\< `StateType` \> \| `undefined`

The first thread state the message was seen in.

#### messageId [¶](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/\#messageid "Permanent link")

> **messageId**: `string`

The ID of the message used.

## Comments

giscus

#### [0 reactions](https://github.com/langchain-ai/langgraph/discussions/2963)

#### [1 comment](https://github.com/langchain-ai/langgraph/discussions/2963)

#### ·

#### 2 replies

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@liwoo](https://avatars.githubusercontent.com/u/11289074?u=a63ff49e3b7bc938117002c09abd99b8ca71a1f3&v=4)liwoo](https://github.com/liwoo) [Jan 9](https://github.com/langchain-ai/langgraph/discussions/2963#discussioncomment-11782114)

Is there anyone else facing issues with CORS when testing the graphs locally?

1

2 replies

[![@hinthornw](https://avatars.githubusercontent.com/u/13333726?u=82ebf1e0eb0663ebd49ba66f67a43f51bbf11442&v=4)](https://github.com/hinthornw)

[hinthornw](https://github.com/hinthornw) [Jan 9](https://github.com/langchain-ai/langgraph/discussions/2963#discussioncomment-11782119)

Contributor

What browser are you using?

[![@liwoo](https://avatars.githubusercontent.com/u/11289074?u=a63ff49e3b7bc938117002c09abd99b8ca71a1f3&v=4)](https://github.com/liwoo)

[liwoo](https://github.com/liwoo) [Jan 9](https://github.com/langchain-ai/langgraph/discussions/2963#discussioncomment-11782124)

Firefox... I'm using React (TS SDK) to update state in a graph that's running locally...

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Freference%2Fsdk%2Fjs_ts_sdk_ref%2F)