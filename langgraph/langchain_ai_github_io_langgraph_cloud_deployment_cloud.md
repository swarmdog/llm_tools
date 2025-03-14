[Skip to content](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/#how-to-deploy-to-langgraph-cloud)

[Edit this page](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/deployment/cloud.md "Edit this page")

# How to Deploy to LangGraph Cloud [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/\#how-to-deploy-to-langgraph-cloud "Permanent link")

LangGraph Cloud is available within [LangSmith](https://www.langchain.com/langsmith). To deploy a LangGraph Cloud API, navigate to the [LangSmith UI](https://smith.langchain.com/).

## Prerequisites [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/\#prerequisites "Permanent link")

1. LangGraph Cloud applications are deployed from GitHub repositories. Configure and upload a LangGraph Cloud application to a GitHub repository in order to deploy it to LangGraph Cloud.
2. [Verify that the LangGraph API runs locally](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/). If the API does not run successfully (i.e. `langgraph dev`), deploying to LangGraph Cloud will fail as well.

## Create New Deployment [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/\#create-new-deployment "Permanent link")

Starting from the [LangSmith UI](https://smith.langchain.com/)...

1. In the left-hand navigation panel, select `LangGraph Platform`. The `LangGraph Platform` view contains a list of existing LangGraph Cloud deployments.
2. In the top-right corner, select `+ New Deployment` to create a new deployment.
3. In the `Create New Deployment` panel, fill out the required fields.
1. `Deployment details`
      1. Select `Import from GitHub` and follow the GitHub OAuth workflow to install and authorize LangChain's `hosted-langserve` GitHub app to access the selected repositories. After installation is complete, return to the `Create New Deployment` panel and select the GitHub repository to deploy from the dropdown menu. **Note**: The GitHub user installing LangChain's `hosted-langserve` GitHub app must be an [owner](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#organization-owners) of the organization or account.
      2. Specify a name for the deployment.
      3. Specify the desired `Git Branch`. A deployment is linked to a branch. When a new revision is created, code for the linked branch will be deployed. The branch can be updated later in the [Deployment Settings](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/#deployment-settings).
      4. Specify the full path to the [LangGraph API config file](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file) including the file name. For example, if the file `langgraph.json` is in the root of the repository, simply specify `langgraph.json`.
      5. Check/uncheck checkbox to `Automatically update deployment on push to branch`. If checked, the deployment will automatically be updated when changes are pushed to the specified `Git Branch`. This setting can be enabled/disabled later in the [Deployment Settings](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/#deployment-settings).
2. Select the desired `Deployment Type`.
      1. `Development` deployments are meant for non-production use cases and are provisioned with minimal resources.
      2. `Production` deployments can serve up to 500 requests/second and are provisioned with highly available storage with automatic backups.
3. Determine if the deployment should be `Shareable through LangGraph Studio`.
      1. If unchecked, the deployment will only be accessible with a valid LangSmith API key for the workspace.
      2. If checked, the deployment will be accessible through LangGraph Studio to any LangSmith user. A direct URL to LangGraph Studio for the deployment will be provided to share with other LangSmith users.
4. Specify `Environment Variables` and secrets. See the [Environment Variables reference](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/) to configure additional variables for the deployment.
      1. Sensitive values such as API keys (e.g. `OPENAI_API_KEY`) should be specified as secrets.
      2. Additional non-secret environment variables can be specified as well.
5. A new LangSmith `Tracing Project` is automatically created with the same name as the deployment.
4. In the top-right corner, select `Submit`. After a few seconds, the `Deployment` view appears and the new deployment will be queued for provisioning.

## Create New Revision [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/\#create-new-revision "Permanent link")

When [creating a new deployment](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/#create-new-deployment), a new revision is created by default. Subsequent revisions can be created to deploy new code changes.

Starting from the [LangSmith UI](https://smith.langchain.com/)...

1. In the left-hand navigation panel, select `LangGraph Platform`. The `LangGraph Platform` view contains a list of existing LangGraph Cloud deployments.
2. Select an existing deployment to create a new revision for.
3. In the `Deployment` view, in the top-right corner, select `+ New Revision`.
4. In the `New Revision` modal, fill out the required fields.
1. Specify the full path to the [LangGraph API config file](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file) including the file name. For example, if the file `langgraph.json` is in the root of the repository, simply specify `langgraph.json`.
2. Determine if the deployment should be `Shareable through LangGraph Studio`.
      1. If unchecked, the deployment will only be accessible with a valid LangSmith API key for the workspace.
      2. If checked, the deployment will be accessible through LangGraph Studio to any LangSmith user. A direct URL to LangGraph Studio for the deployment will be provided to share with other LangSmith users.
3. Specify `Environment Variables` and secrets. Existing secrets and environment variables are prepopulated. See the [Environment Variables reference](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/) to configure additional variables for the revision.
      1. Add new secrets or environment variables.
      2. Remove existing secrets or environment variables.
      3. Update the value of existing secrets or environment variables.
5. Select `Submit`. After a few seconds, the `New Revision` modal will close and the new revision will be queued for deployment.

## View Build and Server Logs [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/\#view-build-and-server-logs "Permanent link")

Build and server logs are available for each revision.

Starting from the `LangGraph Platform` view...

1. Select the desired revision from the `Revisions` table. A panel slides open from the right-hand side and the `Build` tab is selected by default, which displays build logs for the revision.
2. In the panel, select the `Server` tab to view server logs for the revision. Server logs are only available after a revision has been deployed.
3. Within the `Server` tab, adjust the date/time range picker as needed. By default, the date/time range picker is set to the `Last 7 days`.

## Interrupt Revision [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/\#interrupt-revision "Permanent link")

Interrupting a revision will stop deployment of the revision.

Undefined Behavior

Interrupted revisions have undefined behavior. This is only useful if you need to deploy a new revision and you already have a revision "stuck" in progress. In the future, this feature may be removed.

Starting from the `LangGraph Platform` view...

1. Select the menu icon (three dots) on the right-hand side of the row for the desired revision from the `Revisions` table.
2. Select `Interrupt` from the menu.
3. A modal will appear. Review the confirmation message. Select `Interrupt revision`.

## Delete Deployment [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/\#delete-deployment "Permanent link")

Starting from the [LangSmith UI](https://smith.langchain.com/)...

1. In the left-hand navigation panel, select `LangGraph Platform`. The `LangGraph Platform` view contains a list of existing LangGraph Cloud deployments.
2. Select the menu icon (three dots) on the right-hand side of the row for the desired deployment and select `Delete`.
3. A `Confirmation` modal will appear. Select `Delete`.

## Deployment Settings [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/\#deployment-settings "Permanent link")

Starting from the `LangGraph Platform` view...

1. In the top-right corner, select the gear icon ( `Deployment Settings`).
2. Update the `Git Branch` to the desired branch.
3. Check/uncheck checkbox to `Automatically update deployment on push to branch`.
1. Branch creation/deletion and tag creation/deletion events will not trigger an update. Only pushes to an existing branch will trigger an update.
2. Pushes in quick succession to a branch will not trigger subsequent updates. In the future, this functionality may be changed/improved.

## Add or Remove GitHub Repositories [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/\#add-or-remove-github-repositories "Permanent link")

After installing and authorizing LangChain's `hosted-langserve` GitHub app, repository access for the app can be modified to add new repositories or remove existing repositories. If a new repository is created, it may need to be added explicitly.

1. From the GitHub profile, navigate to `Settings` \> `Applications` \> `hosted-langserve` \> click `Configure`.
2. Under `Repository access`, select `All repositories` or `Only select repositories`. If `Only select repositories` is selected, new repositories must be explicitly added.
3. Click `Save`.
4. When creating a new deployment, the list of GitHub repositories in the dropdown menu will be updated to reflect the repository access changes.

## Whitelisting IP Addresses [¶](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/\#whitelisting-ip-addresses "Permanent link")

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

## Comments

giscus

#### [0 reactions](https://github.com/langchain-ai/langgraph/discussions/1585)

#### [13 comments](https://github.com/langchain-ai/langgraph/discussions/1585)

#### ·

#### 21 replies

_– powered by [giscus](https://giscus.app/)_

- Oldest
- Newest

[![@marinij](https://avatars.githubusercontent.com/u/24779300?u=046cf8b6b947b28005fc0deeb4e08fa09c93aff4&v=4)marinij](https://github.com/marinij) [Sep 3, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-10529727)

Hello!

Is there a way to create a new revision by command-line ?

Also, would it be possible to restart a deployment by command-line ?

2

🚀1

1 reply

[![@andrewnguonly](https://avatars.githubusercontent.com/u/7654246?u=b8599019655adaada3cdc3c3006798df42c44494&v=4)](https://github.com/andrewnguonly)

[andrewnguonly](https://github.com/andrewnguonly) [Oct 8, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-10883036)

Contributor

Creating a new revision and restarting a deployment by command line are not supported at the moment.

Alternatively, LangGraph Cloud supports the ability to automatically update a deployment (i.e. create a new revision) on push to a branch. This can be configured in the [Deployment Settings](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/#deployment-settings).

[![@vermapratyush](https://avatars.githubusercontent.com/u/159288?v=4)vermapratyush](https://github.com/vermapratyush) [Sep 13, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-10642635)

Contributor

When running `langgraph up`, I get the following build error

Seems like gcc isn't available in the base image?

```notranslate
#7 16.03 Downloading zipp-3.20.2-py3-none-any.whl (9.2 kB)
#7 16.04 Downloading leb128-1.0.8-py3-none-any.whl (3.8 kB)
#7 16.05 Downloading tzlocal-5.2-py3-none-any.whl (17 kB)
#7 16.06 Downloading zstd-1.5.5.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (1.8 MB)
#7 16.09    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 67.2 MB/s eta 0:00:00
#7 16.09 Downloading mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)
#7 16.34 Building wheels for collected packages: clickhouse-sqlalchemy, ciso8601
#7 16.34   Building wheel for clickhouse-sqlalchemy (setup.py): started
#7 16.90   Building wheel for clickhouse-sqlalchemy (setup.py): finished with status 'done'
#7 16.90   Created wheel for clickhouse-sqlalchemy: filename=clickhouse_sqlalchemy-0.3.2-py3-none-any.whl size=53508 sha256=8fc7e355526c8e4b239d2861e5c1b1863b156265572843b2dc788a7ec1199a0a
#7 16.90   Stored in directory: /tmp/pip-ephem-wheel-cache-mvdwl9ae/wheels/d0/c6/3f/e92747d519bd8e6c779750883f6bd42189d71cd97a8e879c8f
#7 16.90   Building wheel for ciso8601 (pyproject.toml): started
#7 17.16   Building wheel for ciso8601 (pyproject.toml): finished with status 'error'
#7 17.17   error: subprocess-exited-with-error
#7 17.17
#7 17.17   × Building wheel for ciso8601 (pyproject.toml) did not run successfully.
#7 17.17   │ exit code: 1
#7 17.17   ╰─> [19 lines of output]
#7 17.17       /tmp/pip-build-env-m9g8ximl/overlay/lib/python3.11/site-packages/setuptools/_distutils/dist.py:261: UserWarning: Unknown distribution option: 'test_suite'
#7 17.17         warnings.warn(msg)
#7 17.17       /tmp/pip-build-env-m9g8ximl/overlay/lib/python3.11/site-packages/setuptools/_distutils/dist.py:261: UserWarning: Unknown distribution option: 'tests_require'
#7 17.17         warnings.warn(msg)
#7 17.17       running bdist_wheel
#7 17.17       running build
#7 17.17       running build_py
#7 17.17       creating build
#7 17.17       creating build/lib.linux-aarch64-cpython-311
#7 17.17       creating build/lib.linux-aarch64-cpython-311/ciso8601
#7 17.17       copying ciso8601/__init__.pyi -> build/lib.linux-aarch64-cpython-311/ciso8601
#7 17.17       copying ciso8601/py.typed -> build/lib.linux-aarch64-cpython-311/ciso8601
#7 17.17       warning: build_py: byte-compiling is disabled, skipping.
#7 17.17
#7 17.17       running build_ext
#7 17.17       building 'ciso8601' extension
#7 17.17       creating build/temp.linux-aarch64-cpython-311
#7 17.17       gcc -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DCISO8601_VERSION=2.3.1 -DCISO8601_CACHING_ENABLED=1 -I/usr/local/include/python3.11 -c isocalendar.c -o build/temp.linux-aarch64-cpython-311/isocalendar.o
#7 17.17       error: command 'gcc' failed: No such file or directory
#7 17.17       [end of output]
#7 17.17
#7 17.17   note: This error originates from a subprocess, and is likely not a problem with pip.
#7 17.17   ERROR: Failed building wheel for ciso8601
#7 17.17 Successfully built clickhouse-sqlalchemy
#7 17.17 Failed to build ciso8601
#7 17.17 ERROR: Could not build wheels for ciso8601, which is required to install pyproject.toml-based projects
#7 17.25
#7 17.25 [notice] A new release of pip is available: 24.0 -> 24.2
#7 17.25 [notice] To update, run: pip install --upgrade pip
#7 ERROR: process "/bin/sh -c PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -c /api/constraints.txt -r /deps/__outer_inference/inference/requirements.txt" did not complete successfully: exit code: 1
------
 > [langgraph-api 3/7] RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -c /api/constraints.txt -r /deps/__outer_inference/inference/requirements.txt:
17.17       [end of output]
17.17
17.17   note: This error originates from a subprocess, and is likely not a problem with pip.
17.17   ERROR: Failed building wheel for ciso8601
17.17 Successfully built clickhouse-sqlalchemy
17.17 Failed to build ciso8601
17.17 ERROR: Could not build wheels for ciso8601, which is required to install pyproject.toml-based projects
17.25
17.25 [notice] A new release of pip is available: 24.0 -> 24.2
17.25 [notice] To update, run: pip install --upgrade pip
------
time="2024-09-13T23:13:52+01:00" level=warning msg="The \"line\" variable is not set. Defaulting to a blank string."
failed to solve: process "/bin/sh -c PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -c /api/constraints.txt -r /deps/__outer_inference/inference/requirements.txt" did not complete successfully: exit code: 1

```

1

1 reply

[![@vermapratyush](https://avatars.githubusercontent.com/u/159288?v=4)](https://github.com/vermapratyush)

[vermapratyush](https://github.com/vermapratyush) [Sep 13, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-10642699)

Contributor

Fixed it by adding the following to langgraph.json. Shouldn't this be install in the base image itself.

```notranslate
"dockerfile_lines": [\
    "RUN apt-get update && apt-get install -y gcc"\
  ],

```

[![@suyashkumar2409](https://avatars.githubusercontent.com/u/10911412?u=b7f8dea2bd45a8cb479bcc8014e3d1f4c8a42eff&v=4)suyashkumar2409](https://github.com/suyashkumar2409) [Oct 7, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-10873703)

Hey, I am actively using langgraph and langgraph studio to build my AI agents. I would love to see what you are doing for langgraph cloud, and whether it makes my use cases simpler to execute.

What is the procedure for gaining beta access?

1

2 replies

[![@hwchase17](https://avatars.githubusercontent.com/u/11986836?u=f4c4f21a82b2af6c9f91e1f1d99ea40062f7a101&v=4)](https://github.com/hwchase17)

[hwchase17](https://github.com/hwchase17) [Oct 8, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-10874283)

Contributor

its currently available for all users with a Plus account

[![@vbarda](https://avatars.githubusercontent.com/u/19161700?u=e76bcd472b51c9f07befd2654783d0a381f49005&v=4)](https://github.com/vbarda)

[vbarda](https://github.com/vbarda) [Oct 31, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-11114340)

Collaborator

Hi [@suyashkumar2409](https://github.com/suyashkumar2409)! We just added more deployment options for LangGraph Platform (formerly LangGraph Cloud), including "Self-hosted Lite" - a limited **free** version. It is available to anyone with a **free** (developer) [LangSmith account](https://giscus.app/en/smith.langchain.com). Please check out the documentation to learn more: [https://langchain-ai.github.io/langgraph/concepts/deployment\_options/#self-hosted-lite](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-lite). let me know if you have any questions!

[![@antoremin](https://avatars.githubusercontent.com/u/6918736?v=4)antoremin](https://github.com/antoremin) [Oct 8, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-10882830)

Seems like "interrupt" button is grayed out on my instance, and there's no delete button altogether. Would love to have a way to stop all current threads/redeploy from the latest commit.

1

1 reply

[![@andrewnguonly](https://avatars.githubusercontent.com/u/7654246?u=b8599019655adaada3cdc3c3006798df42c44494&v=4)](https://github.com/andrewnguonly)

[andrewnguonly](https://github.com/andrewnguonly) [Oct 10, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-10908796)

Contributor

You can create a new revision to redeploy from the latest commit of the specified branch for your deployment. There's no way to delete an individual revision. If the `Interrupt` button is grayed out, then the revision is in a terminal state (i.e. it can't be interrupted).

If you want to delete the entire deployment (including all revisions for the deployment), you can delete the deployment from the deployments list view. See [Delete Deployment](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/#delete-deployment) in the documentation.

[![@alchemistgo87](https://avatars.githubusercontent.com/u/1254443?u=783b7d14eb1d053956b95d96a819dda08bfbfeb5&v=4)alchemistgo87](https://github.com/alchemistgo87) [Oct 15, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-10946372)

I don't see any "New Deployment" button on deployments tab. How can I deploy a github repo?

1

4 replies

[![@andrewnguonly](https://avatars.githubusercontent.com/u/7654246?u=b8599019655adaada3cdc3c3006798df42c44494&v=4)](https://github.com/andrewnguonly)

[andrewnguonly](https://github.com/andrewnguonly) [Oct 15, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-10948755)

Contributor

After clicking on the `Deployments` tab in the left-hand navigation, do you see the following screenshot at the top of your screen?

[![image](https://private-user-images.githubusercontent.com/7654246/376657897-9cf31f73-517a-41d7-9105-a0c8d0f9d3dd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDE5MTA4ODQsIm5iZiI6MTc0MTkxMDU4NCwicGF0aCI6Ii83NjU0MjQ2LzM3NjY1Nzg5Ny05Y2YzMWY3My01MTdhLTQxZDctOTEwNS1hMGM4ZDBmOWQzZGQucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDMxNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAzMTRUMDAwMzA0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NDdjZjZlYjA0NGJlZjA4OWY5YTE1YTI4NzkxNjc2MGViZjQ5NTFiMjZhYjY1M2U2ODVlYjgyN2I0MThiNGQzMCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.pFfJNme61cSrnGnY1oooYetOeHh2sfljCahRpLvMPAg)](https://private-user-images.githubusercontent.com/7654246/376657897-9cf31f73-517a-41d7-9105-a0c8d0f9d3dd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDE5MTA4ODQsIm5iZiI6MTc0MTkxMDU4NCwicGF0aCI6Ii83NjU0MjQ2LzM3NjY1Nzg5Ny05Y2YzMWY3My01MTdhLTQxZDctOTEwNS1hMGM4ZDBmOWQzZGQucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDMxNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAzMTRUMDAwMzA0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NDdjZjZlYjA0NGJlZjA4OWY5YTE1YTI4NzkxNjc2MGViZjQ5NTFiMjZhYjY1M2U2ODVlYjgyN2I0MThiNGQzMCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.pFfJNme61cSrnGnY1oooYetOeHh2sfljCahRpLvMPAg)

If not, can you share a screenshot of what you see after clicking on the `Deployments` tab?

[![@alchemistgo87](https://avatars.githubusercontent.com/u/1254443?u=783b7d14eb1d053956b95d96a819dda08bfbfeb5&v=4)](https://github.com/alchemistgo87)

[alchemistgo87](https://github.com/alchemistgo87) [Oct 16, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-10954980)

Hi Andrew,

Thanks for the reply!

Sharing the screenshot of what I see on my deployments page:

[https://drive.google.com/file/d/1-gLQ4Wsm9B3OXxkVF\_7x4axhE0scbhcn/view?usp=sharing](https://drive.google.com/file/d/1-gLQ4Wsm9B3OXxkVF_7x4axhE0scbhcn/view?usp=sharing)

[![@andrewnguonly](https://avatars.githubusercontent.com/u/7654246?u=b8599019655adaada3cdc3c3006798df42c44494&v=4)](https://github.com/andrewnguonly)

[andrewnguonly](https://github.com/andrewnguonly) [Oct 17, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-10973995)

Contributor

LangGraph Cloud is only available for paid LangSmith plans (Plus, Premier, Startup Enterprise). Based on your screenshot, it looks like your LangSmith plan is a free Developer plan. The free Developer plan is not able to access LangGraph Cloud. You'll need to upgrade your LangSmith plan to a paid plan in order to access LangGraph Cloud.

👍1

[![@alchemistgo87](https://avatars.githubusercontent.com/u/1254443?u=783b7d14eb1d053956b95d96a819dda08bfbfeb5&v=4)](https://github.com/alchemistgo87)

[alchemistgo87](https://github.com/alchemistgo87) [Oct 18, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-10979252)

Ok, got it. Thanks for the help!

[![@achrafmam2](https://avatars.githubusercontent.com/u/4048514?v=4)achrafmam2](https://github.com/achrafmam2) [Nov 11, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-11217498)

I am using [https://www.pantsbuild.org](https://www.pantsbuild.org/) for building our python binaries. Pants can output a docker image. Is it possible to use a custom docker image for deployment?

1

1 reply

[![@andrewnguonly](https://avatars.githubusercontent.com/u/7654246?u=b8599019655adaada3cdc3c3006798df42c44494&v=4)](https://github.com/andrewnguonly)

[andrewnguonly](https://github.com/andrewnguonly) [Nov 13, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-11235596)

Contributor

At this moment, LangGraph Cloud does not support deploying from a custom Docker image.

[![@belmai](https://avatars.githubusercontent.com/u/59979912?v=4)belmai](https://github.com/belmai) [Nov 22, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-11349009)

It is possible to connect gitlab repo?

1

1 reply

[![@andrewnguonly](https://avatars.githubusercontent.com/u/7654246?u=b8599019655adaada3cdc3c3006798df42c44494&v=4)](https://github.com/andrewnguonly)

[andrewnguonly](https://github.com/andrewnguonly) [Nov 22, 2024](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-11352758)

Contributor

Currently, it's not possible to connect and deploy from a GitLab repository. As a workaround, you can mirror a GitLab repository to a GitHub repository.

Repository mirroring: [https://docs.gitlab.com/ee/user/project/repository/mirror/](https://docs.gitlab.com/ee/user/project/repository/mirror/)

👍1

[![@yerx](https://avatars.githubusercontent.com/u/10455085?u=a01b91f3c2ffbcb15b95f396b45adaf7e45970e6&v=4)yerx](https://github.com/yerx) [Jan 29](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-11990609)

Hi, I created a new deployment and added environment variables. I want to add more environment variables to my project, but I can't find a button to update environment variables. Could you point me in the right direction?

1

1 reply

[![@andrewnguonly](https://avatars.githubusercontent.com/u/7654246?u=b8599019655adaada3cdc3c3006798df42c44494&v=4)](https://github.com/andrewnguonly)

[andrewnguonly](https://github.com/andrewnguonly) [Jan 30](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12001986)

Contributor

To add/change environment variables, you'll have to create a new revision.

Create new revision: [https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/#create-new-revision](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/#create-new-revision)

[![@phfifofum](https://avatars.githubusercontent.com/u/178105107?v=4)phfifofum](https://github.com/phfifofum) [Feb 6](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12085033)

Trying to deploy to cloud and getting a timeout on the the server starting up. Build passes fine, seems to be a server issue but the logs dont give me any insight....

Revision ID - 02a1678d35-bbf6-4770-8b3d-00ae2800ee3d

Any ideas team?

06/02/2025, 11:19:21 Using auth of type=langsmith

06/02/2025, 11:19:21 Started server process \[1\]

06/02/2025, 11:19:21 Waiting for application startup.

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 Applied database migration

06/02/2025, 11:19:21 No LANGGRAPH\_STORE configuration found, using default configuration

06/02/2025, 11:19:34 Using auth of type=langsmith

06/02/2025, 11:19:34 Started server process \[1\]

06/02/2025, 11:19:34 Waiting for application startup.

06/02/2025, 11:19:34 No LANGGRAPH\_STORE configuration found, using default configuration

06/02/2025, 11:19:51 Using auth of type=langsmith

06/02/2025, 11:19:52 Started server process \[1\]

06/02/2025, 11:19:52 Waiting for application startup.

06/02/2025, 11:19:52 No LANGGRAPH\_STORE configuration found, using default configuration

06/02/2025, 11:20:27 Using auth of type=langsmith

06/02/2025, 11:20:27 Started server process \[1\]

06/02/2025, 11:20:27 Waiting for application startup.

06/02/2025, 11:20:27 No LANGGRAPH\_STORE configuration found, using default configuration

06/02/2025, 11:21:10 Using auth of type=langsmith

06/02/2025, 11:21:10 Started server process \[1\]

06/02/2025, 11:21:10 Waiting for application startup.

06/02/2025, 11:21:10 No LANGGRAPH\_STORE configuration found, using default configuration

1

2 replies

[![@andrewnguonly](https://avatars.githubusercontent.com/u/7654246?u=b8599019655adaada3cdc3c3006798df42c44494&v=4)](https://github.com/andrewnguonly)

[andrewnguonly](https://github.com/andrewnguonly) [Feb 7](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12099484)

Contributor

I looked at the deployment. I'm not sure what the issue is, but I think the issue might be a fluke. Can you try creating a new revision for the deployment and see if the issue persists?

[![@phfifofum](https://avatars.githubusercontent.com/u/178105107?v=4)](https://github.com/phfifofum)

[phfifofum](https://github.com/phfifofum) [Feb 8](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12103802)

just replied on slack, i tried it again with fresh deployment and no beuno - 33f980f5-4ff7-4829-af95-6b3e04f04679

Again this works fine locally and in studio

[![@kihumban](https://avatars.githubusercontent.com/u/3886280?u=be226484faecf404d51ca99675a0da24224e37d0&v=4)kihumban](https://github.com/kihumban) [28 days ago](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12181742)

I previously hosted my Langgraph backend API locally using a Docker container, and everything worked as long as the container was running. The frontend was hosted on Vercel.

Recently, I migrated the backend API to Langgraph Cloud and redeployed the frontend on Vercel after removing the previous deployment. I updated the environment variable NEXT\_PUBLIC\_API\_URL to point to the new cloud API server and modified the frontend code accordingly.

However, the application is now failing to work, and I keep receiving error messages - "Unable to find the current thread ID" in the client application. This normally happens the client application cannot connect to the backend API server. Langgraph cloud automatically create a new API key when you deploy, however, I am unable to get the value of that API key. I am suspecting the issue is the API key that I have in the environmental variable is the issue.

I updated the environment variable NEXT\_PUBLIC\_API\_URL to point to the new cloud API server and modified the frontend code accordingly:

export const createClient = () => {

const apiUrl = process.env.NEXT\_PUBLIC\_API\_URL;

const apiKey = process.env.LANGSMITH\_API\_KEY;

return new Client({

apiUrl: apiUrl,

apiKey: apiKey

});

};

Here is error from the browser console:

Error creating thread HTTPError: HTTP 403: {"detail":"Missing authentication headers"}

at HTTPError.fromResponse (7933-37d17a5b62912814.js:256:24595)

at async 7933-37d17a5b62912814.js:256:25713

at async RetryOperation.\_fn (7933-37d17a5b62912814.js:204:6647)

Could you please advise on what additional authentication details or configuration might be required?

1

4 replies

[![@andrewnguonly](https://avatars.githubusercontent.com/u/7654246?u=b8599019655adaada3cdc3c3006798df42c44494&v=4)](https://github.com/andrewnguonly)

[andrewnguonly](https://github.com/andrewnguonly) [28 days ago](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12191128)

Contributor

> However, the application is now failing to work, and I keep receiving error messages - "Unable to find the current thread ID" in the client application. They're simply separate deployments.

Clarifying: Any existing thread IDs that were created from a local deployment will not exist in a new cloud deployment.

> Langgraph cloud automatically create a new API key when you deploy, however, I am unable to get the value of that API key.

This is expected. You won't be able to access the API key that's automatically created for the deployment. You'll need to create another key (a second one), which will be used to authenticate with the API server.

Authentication: [https://langchain-ai.github.io/langgraph/cloud/reference/api/api\_ref/#authentication](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#authentication)

> I am suspecting the issue is the API key that I have in the environmental variable is the issue.

Can you confirm that `process.env.LANGSMITH_API_KEY` is set to a valid API key that was created from the same LangSmith organization where the LangGraph deployment was created? For example, just print out the value of `process.env.LANGSMITH_API_KEY` to double check.

[![@kihumban](https://avatars.githubusercontent.com/u/3886280?u=be226484faecf404d51ca99675a0da24224e37d0&v=4)](https://github.com/kihumban)

[kihumban](https://github.com/kihumban) [28 days ago](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12191452)

[@andrewnguonly](https://github.com/andrewnguonly) Thank you for the feedback.

I created a new API key which is what I have used in the environmental variable and I have confirmed it's correct. I have also tried with one of the existing API key. However, I am still getting the same error. The application is working perfectly in Langgraph Studio

[![@kihumban](https://avatars.githubusercontent.com/u/3886280?u=be226484faecf404d51ca99675a0da24224e37d0&v=4)](https://github.com/kihumban)

[kihumban](https://github.com/kihumban) [27 days ago](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12195710)

[@andrewnguonly](https://github.com/andrewnguonly) I am successfully connecting to the API through the Jupyter notebook. For instance I run this code successfully. where the URL is my langgraph cloud API URL.

\`client = get\_sync\_client(url= url)

for chunk in client.runs.stream(

None, # Threadless run

"chat", # Name of assistant. Defined in langgraph.json.

input={

"messages": \[{\
\
"role": "human",\
\
"content": "What is hope forum?",\
\
}\],

},

stream\_mode="updates",

):

print(f"Receiving new event of type: {chunk.event}...")

print(chunk.data)

print("\\n\\n")\`

```notranslate
The app is also running successfully on Langgraph Studio and on the browser on a locally hosted API server (http://localhost:8123). The issue come when I connect to the langgraph cloud server and run the client on the browser. The server is throwing a 403 error - {"Missing authentication headers"} . See the image below.

```

[![image](https://private-user-images.githubusercontent.com/3886280/413154384-55fde50d-0960-42cd-aea3-5f3cf87e6b3a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDE5MTA4ODQsIm5iZiI6MTc0MTkxMDU4NCwicGF0aCI6Ii8zODg2MjgwLzQxMzE1NDM4NC01NWZkZTUwZC0wOTYwLTQyY2QtYWVhMy01ZjNjZjg3ZTZiM2EucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDMxNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAzMTRUMDAwMzA0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MGNhZDg0N2U0Y2NiZTFkNzdkMmZhOTU2NWRiNGQzZGJhODQ4NzAxNzU0NjE3NzQyYzU3NDA5YzBkNDc1ZjhkMyZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.ktmGExXgjW4xOZGcpO7qJAyD0YcBQgfApbi33BeFjs8)](https://private-user-images.githubusercontent.com/3886280/413154384-55fde50d-0960-42cd-aea3-5f3cf87e6b3a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDE5MTA4ODQsIm5iZiI6MTc0MTkxMDU4NCwicGF0aCI6Ii8zODg2MjgwLzQxMzE1NDM4NC01NWZkZTUwZC0wOTYwLTQyY2QtYWVhMy01ZjNjZjg3ZTZiM2EucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDMxNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAzMTRUMDAwMzA0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MGNhZDg0N2U0Y2NiZTFkNzdkMmZhOTU2NWRiNGQzZGJhODQ4NzAxNzU0NjE3NzQyYzU3NDA5YzBkNDc1ZjhkMyZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.ktmGExXgjW4xOZGcpO7qJAyD0YcBQgfApbi33BeFjs8)

What I am missing? I have the paid Startup account.

[![@romanh24](https://avatars.githubusercontent.com/u/70602437?u=e855addcdcc9b2b6f3d9c182d61177c70b126679&v=4)](https://github.com/romanh24)

[romanh24](https://github.com/romanh24) [2 days ago](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12463805)

[@kihumban](https://github.com/kihumban) hi,

I have the same error. How did you fix it?

[![@kihumban](https://avatars.githubusercontent.com/u/3886280?u=be226484faecf404d51ca99675a0da24224e37d0&v=4)kihumban](https://github.com/kihumban) [2 days ago](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12463970)

[@romanh24](https://github.com/romanh24) I reconfigured a couple of the environmental variables. I am presuming you have your backend API on langgraph cloud. Where is your client - local or on the cloud e.g. Vercel? Mine was on Vercel

2

1 reply

[![@romanh24](https://avatars.githubusercontent.com/u/70602437?u=e855addcdcc9b2b6f3d9c182d61177c70b126679&v=4)](https://github.com/romanh24)

[romanh24](https://github.com/romanh24) [2 days ago](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12465364)

[@kihumban](https://github.com/kihumban)

After deploying to the Platform, I updated the .env file on my local machine with the `API URL`(is it correct? screen) from Platform and am using the `useStream()` React hook in my Next.js app. However, I'm seeing the following error in the console:

HTTPError: HTTP 403: {"detail":"Missing authentication headers"}.

I'm currently using `use client`. If there's a shorter or better way to handle this with `use server`, I'd like to try it.

My next step is to deploy to Vercel, but I want to test it locally first.

[![image](https://private-user-images.githubusercontent.com/70602437/421510531-d1bf73d1-b3fe-40b3-9be3-40785c8e15aa.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDE5MTA4ODQsIm5iZiI6MTc0MTkxMDU4NCwicGF0aCI6Ii83MDYwMjQzNy80MjE1MTA1MzEtZDFiZjczZDEtYjNmZS00MGIzLTliZTMtNDA3ODVjOGUxNWFhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzE0VDAwMDMwNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTUyODc3ODkxZTYyY2QyODE1Nzk2NzBlZjMzN2NiZDdmMDJjZTk1NjE4M2I1ZmUwMmNlZWJkY2UwZmMyZDEwOTAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.Sl5GAXtTGyUgwLpuCV32qUW5-SSKKj1zpqkL7RaCwJM)](https://private-user-images.githubusercontent.com/70602437/421510531-d1bf73d1-b3fe-40b3-9be3-40785c8e15aa.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDE5MTA4ODQsIm5iZiI6MTc0MTkxMDU4NCwicGF0aCI6Ii83MDYwMjQzNy80MjE1MTA1MzEtZDFiZjczZDEtYjNmZS00MGIzLTliZTMtNDA3ODVjOGUxNWFhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzE0VDAwMDMwNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTUyODc3ODkxZTYyY2QyODE1Nzk2NzBlZjMzN2NiZDdmMDJjZTk1NjE4M2I1ZmUwMmNlZWJkY2UwZmMyZDEwOTAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.Sl5GAXtTGyUgwLpuCV32qUW5-SSKKj1zpqkL7RaCwJM)

[![@kihumban](https://avatars.githubusercontent.com/u/3886280?u=be226484faecf404d51ca99675a0da24224e37d0&v=4)kihumban](https://github.com/kihumban) [2 days ago](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12465744)

What does your NEXT\_PUBLIC\_API\_URL or equivalent variable reference? Can you try [http://localhost:8123/](http://localhost:8123/) for local deployment

1

1 reply

[![@romanh24](https://avatars.githubusercontent.com/u/70602437?u=e855addcdcc9b2b6f3d9c182d61177c70b126679&v=4)](https://github.com/romanh24)

[romanh24](https://github.com/romanh24) [2 days ago](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12466313)

edited

For local development, I use in the `useStream()` hook:

`NEXT_PUBLIC_LANGGRAPH_API_URL=http://127.0.0.1:2024`

Code:

```notranslate
const thread = useStream<{ messages: Message[] }>({
   apiUrl: process.env.NEXT_PUBLIC_LANGGRAPH_API_URL,
   assistantId: process.env.NEXT_PUBLIC_LANGGRAPH_ASSISTANT_ID || "agentic_rag",
   messagesKey: "messages",
   threadId: threadId,
   onThreadId: setThreadId
 });

```

[![@kihumban](https://avatars.githubusercontent.com/u/3886280?u=be226484faecf404d51ca99675a0da24224e37d0&v=4)kihumban](https://github.com/kihumban) [2 days ago](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12467089)

I have not used the useStream method the way you have it, so I don't know how it's supposed to work. For me I have a langgraph cloud server client object which to make the API calls including creating threads.

`export const createClient = () => { const apiUrl = process.env.NEXT_PUBLIC_API_URL; return new Client({ apiUrl, }); };`

1

1 reply

[![@romanh24](https://avatars.githubusercontent.com/u/70602437?u=e855addcdcc9b2b6f3d9c182d61177c70b126679&v=4)](https://github.com/romanh24)

[romanh24](https://github.com/romanh24) [yesterday](https://github.com/langchain-ai/langgraph/discussions/1585#discussioncomment-12479986)

Thanks for the answer.

The solution is to pass the `apiKey` value with the `process.env.NEXT_PUBLIC_LANGSMITH_API_KEY` or `process.env.NEXT_PUBLIC_LANGRAPH_API_KEY`.

In the `apiUrl` can be `process.env.NEXT_PUBLIC_LANGSMITH_API_URL` or `process.env.NEXT_PUBLIC_LANGGRAPH_API_URL`.

My current code:

```notranslate
const thread = useStream<{ messages: Message[] }>({
   apiUrl: process.env.NEXT_PUBLIC_LANGSMITH_API_URL,
   apiKey: process.env.NEXT_PUBLIC_LANGSMITH_API_KEY,
   assistantId: process.env.NEXT_PUBLIC_LANGGRAPH_ASSISTANT_ID || "agentic_rag",
   messagesKey: "messages",
   threadId: threadId,
   onThreadId: setThreadId
 });

```

WritePreview

[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/ "Styling with Markdown is supported")

[Sign in with GitHub](https://giscus.app/api/oauth/authorize?redirect_uri=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Fdeployment%2Fcloud%2F)