[Skip to content](https://langchain-ai.github.io/langgraph/concepts/bring_your_own_cloud/#bring-your-own-cloud-byoc)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/bring_your_own_cloud.md "Edit this page")

# Bring Your Own Cloud (BYOC) [¶](https://langchain-ai.github.io/langgraph/concepts/bring_your_own_cloud/\#bring-your-own-cloud-byoc "Permanent link")

Note

- [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
- [Deployment Options](https://langchain-ai.github.io/langgraph/concepts/deployment_options/)

## Architecture [¶](https://langchain-ai.github.io/langgraph/concepts/bring_your_own_cloud/\#architecture "Permanent link")

Split control plane (hosted by us) and data plane (hosted by you, managed by us).

|  | Control Plane | Data Plane |
| --- | --- | --- |
| What it does | Manages deployments, revisions. | Runs your LangGraph graphs, stores your data. |
| Where it is hosted | LangChain Cloud account | Your cloud account |
| Who provisions and monitors | LangChain | LangChain |

LangChain has no direct access to the resources created in your cloud account, and can only interact with them via AWS APIs. Your data never leaves your cloud account / VPC at rest or in transit.

![Architecture](https://langchain-ai.github.io/langgraph/concepts/img/byoc_architecture.png)

## Requirements [¶](https://langchain-ai.github.io/langgraph/concepts/bring_your_own_cloud/\#requirements "Permanent link")

- You’re using AWS already.
- You use `langgraph-cli` and/or [LangGraph Studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/) app to test graph locally.
- You use `langgraph build` command to build image and then push it to your AWS ECR repository ( `docker push`).

## How it works [¶](https://langchain-ai.github.io/langgraph/concepts/bring_your_own_cloud/\#how-it-works "Permanent link")

- We provide you a [Terraform module](https://github.com/langchain-ai/terraform/tree/main/modules/langgraph_cloud_setup) which you run to set up our requirements
1. Creates an AWS role (which our control plane will later assume to provision and monitor resources)
     - [https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonVPCReadOnlyAccess.html](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonVPCReadOnlyAccess.html)
       - Read VPCS to find subnets
     - [https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonECS\_FullAccess.html](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonECS_FullAccess.html)
       - Used to create/delete ECS resources for your LangGraph Cloud instances
     - [https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SecretsManagerReadWrite.html](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SecretsManagerReadWrite.html)
       - Create secrets for your ECS resources
     - [https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchReadOnlyAccess.html](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchReadOnlyAccess.html)
       - Read CloudWatch metrics/logs to monitor your instances/push deployment logs
     - [https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRDSFullAccess.html](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRDSFullAccess.html)
       - Provision `RDS` instances for your LangGraph Cloud instances
       - Alternatively, an externally managed Postgres instance can be used instead of the default `RDS` instance. LangChain does not monitor or manage the externally managed Postgres instance. See details for [`POSTGRES_URI_CUSTOM` environment variable](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#postgres_uri_custom).
2. Either
     - Tags an existing vpc / subnets as `langgraph-cloud-enabled`
     - Creates a new vpc and subnets and tags them as `langgraph-cloud-enabled`
- You create a LangGraph Cloud Project in `smith.langchain.com` providing
  - the ID of the AWS role created in the step above
  - the AWS ECR repo to pull the service image from
- We provision the resources in your cloud account using the role above
- We monitor those resources to ensure uptime and recovery from errors

Notes for customers using [self-hosted LangSmith](https://docs.smith.langchain.com/self_hosting):

- Creation of new LangGraph Cloud projects and revisions currently needs to be done on `smith.langchain.com`.
- However, you can set up the project to trace to your self-hosted LangSmith instance if desired. See details for [`LANGSMITH_RUNS_ENDPOINTS` environment variable](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#langsmith_runs_endpoints).

## Comments

giscus

#### [0 reactions](https://github.com/langchain-ai/langgraph/discussions/3320)

#### [2 comments](https://github.com/langchain-ai/langgraph/discussions/3320)

#### ·

#### 2 replies

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@daher928](https://avatars.githubusercontent.com/u/40135454?u=20c70866f0b2ec77873dd7e7e9281b0f5a988fe6&v=4)daher928](https://github.com/daher928) [Feb 5](https://github.com/langchain-ai/langgraph/discussions/3320#discussioncomment-12068933)

will there be support for Azure any soon?

1

1 reply

[![@andrewnguonly](https://avatars.githubusercontent.com/u/7654246?u=b8599019655adaada3cdc3c3006798df42c44494&v=4)](https://github.com/andrewnguonly)

[andrewnguonly](https://github.com/andrewnguonly) [Feb 5](https://github.com/langchain-ai/langgraph/discussions/3320#discussioncomment-12072580)

Contributor

We don't have immediate plans to support specifically Azure. However, we are planning to support a more generalized Kubernetes offering for Bring Your Own Cloud (BYOC), which will be cloud agnostic (i.e. it will be compatible with Azure).

[![@vishal-g](https://avatars.githubusercontent.com/u/9883621?v=4)vishal-g](https://github.com/vishal-g) [12 days ago](https://github.com/langchain-ai/langgraph/discussions/3320#discussioncomment-12358131)

edited

What is the pricing for BYOC?

1

1 reply

[![@andrewnguonly](https://avatars.githubusercontent.com/u/7654246?u=b8599019655adaada3cdc3c3006798df42c44494&v=4)](https://github.com/andrewnguonly)

[andrewnguonly](https://github.com/andrewnguonly) [12 days ago](https://github.com/langchain-ai/langgraph/discussions/3320#discussioncomment-12358307)

Contributor

[https://www.langchain.com/pricing-langgraph-platform](https://www.langchain.com/pricing-langgraph-platform)

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fconcepts%2Fbring_your_own_cloud%2F)