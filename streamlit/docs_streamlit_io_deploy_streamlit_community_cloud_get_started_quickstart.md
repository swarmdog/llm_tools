# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

1. Contents
2. [Prerequisites](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart#prerequisites)
3. [Sign up for Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart#sign-up-for-streamlit-community-cloud)
4. [Add access to your public repositories](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart#add-access-to-your-public-repositories)
5. [Optional: Add access to private repositories](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart#optional-add-access-to-private-repositories)
6. [Create a new app from a template](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart#create-a-new-app-from-a-template)
7. [Edit your app in GitHub Codespaces](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart#edit-your-app-in-github-codespaces)
8. [Publish your changes](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart#publish-your-changes)
9. [Stop or delete your codespace](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart#stop-or-delete-your-codespace)

# Quickstart

This is a concise set of steps to create your Streamlit Community Cloud account, deploy a sample app, and start editing it with GitHub Codespaces. For other options and complete explanations, start with [Create your account](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/create-your-account).

You will sign in to your GitHub account during this process. Community Cloud will use the email from your GitHub account to create your Community Cloud account. For other sign-in options, see [Create your account](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/create-your-account).

## Prerequisites

- You must have a GitHub account.

## Sign up for Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io/).
2. Click " **Continue to sign-in**."
3. Click " **Continue with GitHub**."
4. Enter your GitHub credentials and follow GitHub's authentication prompts.
5. Fill in your account information, and click " **I accept**" at the bottom.

## Add access to your public repositories

1. In the upper-left corner, click " **Workspaces _warning_**."

![Connect your GitHub account to a new Community Cloud account](https://docs.streamlit.io/images/streamlit-community-cloud/workspace-unconnected-setup.png)

1. From the drop down, click " **Connect GitHub account**."
2. Enter your GitHub credentials and follow GitHub's authentication prompts.
3. Click " **Authorize streamlit**."

![Authorize Community Cloud to connect to your GitHub account](https://docs.streamlit.io/images/streamlit-community-cloud/GitHub-auth1-none.png)

## Optional: Add access to private repositories

1. In the upper-left corner, click on your GitHub username.

![Access your workspace settings](https://docs.streamlit.io/images/streamlit-community-cloud/workspace-empty-menu.png)

1. From the drop down, click " **Settings**."
2. On the left side of the dialog, select " **Linked accounts**."
3. Under "Source control," click " **Connect here _arrow\_forward_**."
4. Click " **Authorize streamlit**."

![Authorize Community Cloud to connect to your private GitHub repositories](https://docs.streamlit.io/images/streamlit-community-cloud/GitHub-auth2-none.png)

## Create a new app from a template

1. In the upper-right corner, click " **Create app**."

![Create a new app from your workspace in Streamlit Community Cloud](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-empty-new-app.png)

1. When asked "Do you already have an app?" click " **Nope, create one from a template**."
2. From the list of templates on the left, select " **Blank app**."
3. At the bottom, select the option to " **Open GitHub Codespaces...**"
4. At the bottom, click " **Deploy**."

## Edit your app in GitHub Codespaces

1. Wait for GitHub to set up your codespace.

It can take several minutes to fully initialize your codespace. After the Visual Studio Code editor appears in your codespace, it can take several minutes to install Python and start the Streamlit server. When complete, a split screen view displays a code editor on the left and a running app on the right. The code editor opens two tabs by default: the repository's readme file and the app's entrypoint file.

![Your new GitHub Codespace](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-template-blank-codespace.png)

2. Go to the app's entrypoint file ( `streamlit_app.py`) in the left pane, and change line 3 by adding "Streamlit" inside `st.title`.


`-st.title("🎈 My new app")
+st.title("🎈 My new Streamlit app")
`


Files are automatically saved in your codespace with each edit.

3. A moment after typing a change, your app on the right side will display a rerun prompt. Click " **Always rerun**."

![Edit the title of your sample Streamlit app](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-template-blank-codespace-edit.png)

If the rerun prompt disappears before you click it, you can hover over the overflow menu icon ( _more\_vert_) to bring it back.

4. Optional: Continue to make edits and observe the changes within seconds.


## Publish your changes

1. In the left navigation bar, click the source control icon.

![See your deployed Streamlit app](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-template-blank-codespace-edit-source-control.png)

1. In the source control sidebar on the left, enter a name for your commit.
2. Click " **_check_ Commit**."

![See your deployed Streamlit app](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-template-blank-codespace-edit-commit.png)

1. To stage and commit all your changes, in the confirmation dialog, click " **Yes**." Your changes are committed locally in your codespace.

2. To push your commit to GitHub, in the source control sidebar on the left, click " **_cached_ 1 _arrow\_upward_**."

3. To push commits to "origin/main," in the confirmation dialog, click " **OK**."

Your changes are now saved to your GitHub repository. Community Cloud will immediately reflect the changes in your deployed app.

4. Optional: To see your updated, published app, return to the " **My apps**" section of your workspace at [share.streamlit.io](https://share.streamlit.io/), and click on your app.


## Stop or delete your codespace

When you stop interacting with your codespace, GitHub will generally stop your codespace for you. However, the surest way to avoid undesired use of your capacity is to stop or delete your codespace when you are done.

1. Go to [github.com/codespaces](https://github.com/codespaces). At the bottom of the page, all your codespaces are listed. Click the overflow menu icon ( _more\_horiz_) for your codespace.

![Stop or delete your GitHub Codespace](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-hello-codespace-manage.png)

2. If you want to return to your work later, click " **Stop codespace**." Otherwise, click " **Delete**."

![Stop your GitHub codespace](https://docs.streamlit.io/images/streamlit-community-cloud/codespace-menu.png)

3. Congratulations! You just deployed an app to Streamlit Community Cloud. 🎉 Return to your workspace at [share.streamlit.io/](https://share.streamlit.io/) and [deploy another Streamlit app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).

![See your deployed Streamlit app](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-template-blank-edited.png)


[Previous: Get started](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started) [Next: Create your account](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/create-your-account)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly9kb2NzLnN0cmVhbWxpdC5pbzo0NDM.&hl=en&v=J79K9xgfxwT6Syzx-UyWdD89&size=invisible&cb=m2hfmp7gb5zn)