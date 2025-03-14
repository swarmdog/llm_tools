# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

1. Contents
2. [Add access to an organization](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/manage-your-github-connection#add-access-to-an-organization)
3. [Revoke and reauthorize](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/manage-your-github-connection#revoke-and-reauthorize)
4. [Granting previously denied access](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/manage-your-github-connection#granting-previously-denied-access)
5. [Rename your GitHub account or repositories](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/manage-your-github-connection#rename-your-github-account-or-repositories)

# Manage your GitHub connection

If you have created an account but not yet connected GitHub, see [Connect your GitHub account](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account).

If you have already connected your GitHub account but still need to allow Streamlit Community Cloud to access private repositories, see [Optional: Add access to private repositories](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account#optional-add-access-to-private-repositories).

## Add access to an organization

If you are in an organization, you can grant or request access to that organization when you connect your GitHub account. For more information, see [Organization access](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account#organization-access).

If your GitHub account is already connected, you can remove permissions in your GitHub settings and force Streamlit to reprompt for GitHub authorization the next time you sign in to Community Cloud.

### Revoke and reauthorize

1. From your workspace, click on your workspace name in the upper-right corner. To sign out of Community Cloud, click " **Sign out**."
![Sign out of Streamlit Community Cloud](https://docs.streamlit.io/images/streamlit-community-cloud/account-sign-out.png)
2. Go to your GitHub application settings at [github.com/settings/applications](https://github.com/settings/applications).

3. Find the "Streamlit" application, and click on the three dots ( _more\_horiz_) to open the overflow menu.

If you have ever signed in to Community Cloud using GitHub, you will also see the "Streamlit Community Cloud" application in your GitHub account. The "Streamlit" application manages repository access. The "Streamlit Community Cloud" application is only for managing your identity (email) on Community Cloud. You only need to revoke access to the "Streamlit" application.

4. Click " **Revoke**."

![Revoke access for Streamlit to access your GitHub account](https://docs.streamlit.io/images/streamlit-community-cloud/GitHub-revoke.png)

5. Click " **I understand, revoke access**."


![Confirm to revoke access for Streamlit to your GitHub account](https://docs.streamlit.io/images/streamlit-community-cloud/GitHub-revoke-confirm.png)

1. Return to [share.streamlit.io](https://share.streamlit.io/) and sign in. You will be prompted to authorize GitHub as explained in [Connect GitHub](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account#organization-access).

### Granting previously denied access

If an organization owner has restricted Streamlit's access or restricted all OAuth applications, they may need to directly modify their permissions in GitHub. If an organization has restricted Streamlit's access, a red X ( _close_) will appear next to the organization when you are prompted to authorize with your GitHub account.

![Denied authorization for Streamlit to access your GitHub account](https://docs.streamlit.io/images/streamlit-community-cloud/GitHub-auth-denied-XL.png)

See GitHub's documentation on [OAuth apps and organizations](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations).

## Rename your GitHub account or repositories

Community Cloud identifies apps by their GitHub coordinates (owner, repository, branch, entrypoint file path). If you rename your account or repository from which you've deployed an app, you will lose access to administer the app. To learn more, see [Rename your app in GitHub](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/rename-your-app).

[Previous: Workspace settings](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/workspace-settings) [Next: Update your email](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/update-your-email)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly9kb2NzLnN0cmVhbWxpdC5pbzo0NDM.&hl=en&v=J79K9xgfxwT6Syzx-UyWdD89&size=invisible&cb=yqmdonrsaxr8)