# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

1. Contents
2. [Introduction](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management#introduction)
3. [How to use secrets management](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management#how-to-use-secrets-management)
4. [Prerequisites](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management#prerequisites)
5. [Advanced settings](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management#advanced-settings)
6. [Edit your app's secrets](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management#edit-your-apps-secrets)

# Secrets management for your Community Cloud app

## Introduction

If you are [connecting to data sources](https://docs.streamlit.io/develop/tutorials/databases), you will likely need to handle credentials or secrets. Storing unencrypted secrets in a git repository is a bad practice. If your application needs access to sensitive credentials, the recommended solution is to store those credentials in a file that is not committed to the repository and to pass them as environment variables.

## How to use secrets management

Community Cloud lets you save your secrets within your app's settings. When developing locally, you can use `st.secrets` in your code to read secrets from a `.streamlit/secrets.toml` file. However, this `secrets.toml` file should never be committed to your repository. Instead, when you deploy your app, you can paste the contents of your `secrets.toml` file into the " **Advanced settings**" dialog. You can update your secrets at any time through your app's settings in your workspace.

### Prerequisites

- You should understand how to use `st.secrets` and `secrets.toml`. See [Secrets management](https://docs.streamlit.io/develop/concepts/connections/secrets-management).

### Advanced settings

While deploying your app, you can access " **Advanced settings**" to set your secrets. After your app is deployed, you can view or update your secrets through the app's settings. The deployment workflow is fully described on the next page, but the " **Advanced settings**" dialog looks like this:

![Advanced settings for deploying your app](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-an-app-advanced.png)

Simply copy and paste the contents of your local `secrets.toml` file into the "Secrets" field within the dialog. After you click " **Save**" to commit the changes, that's it!

### Edit your app's secrets

If you need to add or edit your secrets for an app that is already deployed, you can access secrets through your [App settings](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-settings). See [View or update your secrets](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-settings#view-or-update-your-secrets).

[Previous: App dependencies](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies) [Next: Deploy!](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly9kb2NzLnN0cmVhbWxpdC5pbzo0NDM.&hl=en&v=J79K9xgfxwT6Syzx-UyWdD89&size=invisible&cb=rnjm7uv1v6sc)