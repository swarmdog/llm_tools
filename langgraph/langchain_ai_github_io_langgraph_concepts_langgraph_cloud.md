[Skip to content](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#cloud-saas)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/langgraph_cloud.md "Edit this page")

# Cloud SaaS [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/\#cloud-saas "Permanent link")

Prerequisites

- [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
- [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)

## Overview [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/\#overview "Permanent link")

LangGraph's Cloud SaaS is a managed service for deploying LangGraph Servers, regardless of its definition or dependencies. The service offers managed implementations of checkpointers and stores, allowing you to focus on building the right cognitive architecture for your use case. By handling scalable & secure infrastructure, LangGraph Cloud SaaS offers the fastest path to getting your LangGraph Server deployed to production.

## Deployment [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/\#deployment "Permanent link")

A **deployment** is an instance of a LangGraph Server. A single deployment can have many [revisions](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#revision). When a deployment is created, all the necessary infrastructure (e.g. database, containers, secrets store) are automatically provisioned. See the [architecture diagram](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#architecture) below for more details.

Resource Allocation:

| **Deployment Type** | **CPU** | **Memory** | **Scaling** |
| --- | --- | --- | --- |
| Development | 1 CPU | 1 GB | Up to 1 container |
| Production | 2 CPU | 2 GB | Up to 10 containers |

See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/#create-new-deployment) for creating a new deployment.

## Revision [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/\#revision "Permanent link")

A revision is an iteration of a [deployment](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#deployment). When a new deployment is created, an initial revision is automatically created. To deploy new code changes or update environment variable configurations for a deployment, a new revision must be created. When a revision is created, a new container image is built automatically.

See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/#create-new-revision) for creating a new revision.

## Persistence [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/\#persistence "Permanent link")

A dedicated database is automatically created for each deployment. The database serves as the [persistence layer](https://langchain-ai.github.io/langgraph/concepts/persistence/) for the deployment.

When defining a graph to be deployed to LangGraph Cloud SaaS, a [checkpointer](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpointer-libraries) should not be configured by the user. Instead, a checkpointer is automatically configured for the graph.

There is no direct access to the database. All access to the database occurs through the LangGraph Server APIs.

## Autoscaling [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/\#autoscaling "Permanent link")

`Production` type deployments automatically scale up to 10 containers. Scaling is based on the current request load for a single container. Specifically, the autoscaling implementation scales the deployment so that each container is processing about 10 concurrent requests. For example...

- If the deployment is processing 20 concurrent requests, the deployment will scale up from 1 container to 2 containers (20 requests / 2 containers = 10 requests per container).
- If a deployment of 2 containers is processing 10 requests, the deployment will scale down from 2 containers to 1 container (10 requests / 1 container = 10 requests per container).

10 concurrent requests per container is the target threshold. However, 10 concurrent requests per container is not a hard limit. The number of concurrent requests can exceed 10 if there is a sudden burst of requests.

Scale down actions are delayed for 30 minutes before any action is taken. In other words, if the autoscaling implementation decides to scale down a deployment, it will first wait for 30 minutes before scaling down. After 30 minutes, the concurrency metric is recomputed and the deployment will scale down if the concurrency metric has met the target threshold. Otherwise, the deployment remains scaled up. This "cool down" period ensures that deployments do not scale up and down too frequently.

In the future, the autoscaling implementation may evolve to accommodate other metrics such as background run queue size.

## Asynchronous Deployment [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/\#asynchronous-deployment "Permanent link")

Infrastructure for [deployments](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#deployment) and [revisions](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#revision) are provisioned and deployed asynchronously. They are not deployed immediately after submission. Currently, deployment can take up to several minutes.

- When a new deployment is created, a new database is created for the deployment. Database creation is a one-time step. This step contributes to a longer deployment time for the initial revision of the deployment.
- When a subsequent revision is created for a deployment, there is no database creation step. The deployment time for a subsequent revision is significantly faster compared to the deployment time of the initial revision.
- The deployment process for each revision contains a build step, which can take up to a few minutes.

## LangSmith Integration [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/\#langsmith-integration "Permanent link")

A [LangSmith](https://docs.smith.langchain.com/) tracing project is automatically created for each deployemnt. The tracing project has the same name as the deployment. When creating a deployment, the `LANGCHAIN_TRACING_V2` and `LANGCHAIN_API_KEY` environment variables do not need to be specified; they are set internally, automatically. Traces are created for each run and are emitted to the tracing project automatically.

When a deployment is deleted, the traces and the tracing project are not deleted.

## Automatic Deletion [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/\#automatic-deletion "Permanent link")

Deployments are automatically deleted after 28 consecutive days of non-use (it is in an unused state). A deployment is in an unused state if there are no traces emitted to LangSmith from the deployment after 28 consecutive days. On any given day, if a deployment emits a trace to LangSmith, the counter for consecutive days of non-use is reset.

- An email notification is sent after 7 consecutive days of non-use.
- A deployment is deleted after 28 consecutive days of non-use.

Data Cannot Be Recovered

After a deployment is deleted, the data (i.e. [persistence](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#persistence)) from the deployment cannot be recovered.

## Architecture [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/\#architecture "Permanent link")

Subject to Change

The Cloud SaaS deployment architecture may change in the future.

A high-level diagram of a Cloud SaaS deployment.

![diagram](https://langchain-ai.github.io/langgraph/concepts/img/langgraph_cloud_architecture.png)

## Whitelisting IP Addresses [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/\#whitelisting-ip-addresses "Permanent link")

All traffic from `LangGraph Platform` deployments created after January 6th 2025 will come through a NAT gateway.
This NAT gateway will have several static ip addresses depending on the region you are deploying in. Refer to the table below for the list of IP addresses to whitelist:

| US | EU |
| --- | --- |
| 35.197.29.146 | 34.13.192.67 |
| 34.145.102.123 | 34.147.105.64 |
| 34.169.45.153 | 34.90.22.166 |
| 34.82.222.17 | 34.147.36.213 |
| 35.227.171.135 | 34.32.137.113 |
| 34.169.88.30 | 34.91.238.184 |
| 34.19.93.202 | 35.204.101.241 |
| 34.19.34.50 | 35.204.48.32 |

## Related [¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/\#related "Permanent link")

- [Deployment Options](https://langchain-ai.github.io/langgraph/concepts/deployment_options/)

## Comments

giscus

#### [0 reactions](https://github.com/langchain-ai/langgraph/discussions/2587)

#### [3 comments](https://github.com/langchain-ai/langgraph/discussions/2587)

#### ·

#### 1 reply

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@RVCA212](https://avatars.githubusercontent.com/u/112829052?u=306814ef458a514e27a72e1aa56653c6c5de7392&v=4)RVCA212](https://github.com/RVCA212) [Jan 17](https://github.com/langchain-ai/langgraph/discussions/2587#discussioncomment-11868842)

Is it possible to turn off langsmith tracing at runtime for projects deployed on Langgraph Cloud?

I tried setting:\`\`\`

os.environ\["LANGCHAIN\_TRACING\_V2"\] = "false"

LANGCHAIN\_TRACING\_V2 = "false"

```notranslate
but the runs are still being traced. I'm wondering if there's any way around this?

```

1

0 replies

[![@ahgoos](https://avatars.githubusercontent.com/u/30512230?u=f91d6b57619018dcca1c5792d33e16705f81f714&v=4)ahgoos](https://github.com/ahgoos) [Jan 18](https://github.com/langchain-ai/langgraph/discussions/2587#discussioncomment-11878071)

Is there a way to configure a custom url for Langgraph Cloud deployments? I scoured Langsmith for a configuration option but couldn't find one, could be a good addition as a field in the langgraph.json conf file

1

1 reply

[![@andrewnguonly](https://avatars.githubusercontent.com/u/7654246?u=b8599019655adaada3cdc3c3006798df42c44494&v=4)](https://github.com/andrewnguonly)

[andrewnguonly](https://github.com/andrewnguonly) [Jan 27](https://github.com/langchain-ai/langgraph/discussions/2587#discussioncomment-11977284)

Contributor

At the moment, LangGraph Cloud SaaS deployments do not support custom URLs.

[![@kihumban](https://avatars.githubusercontent.com/u/3886280?u=be226484faecf404d51ca99675a0da24224e37d0&v=4)kihumban](https://github.com/kihumban) [24 days ago](https://github.com/langchain-ai/langgraph/discussions/2587#discussioncomment-12229735)

I recently got on the Cloud SaaS plan.

However, after deploying my application, I’ve encountered an issue when integrating it with a deployed frontend application. Previously, I hosted the backend API locally using a Docker container, and everything worked (and still works) as expected.

Here’s what I’ve observed:

\-\- I can successfully connect to the backend server via Notebook and CLI.

\-\- The app also functions correctly in LangGraph Studio.

\-\- However, when accessing the application from any browser-based connection—including my local development environment, a Vercel-hosted app, or even the LangGraph Platform API Client—I consistently receive an HTTP 403: "Missing authentication headers" error.

I’ve ensured that the x-api-key header is included and set to the correct API key. I’ve also verified that the API key is valid, as it works without issue in Notebook, CLI, and Studio environments.

Despite researching and posting on several forums, I haven’t been able to resolve this issue. Could you please advise on any additional authentication details or configuration steps required to enable the server to work with a deployed frontend application?

1

👍1

0 replies

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fconcepts%2Flanggraph_cloud%2F)