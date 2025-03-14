# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

1. Contents
2. [Delete, rename, redeploy](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/rename-your-app#delete-rename-redeploy)
3. [Regain access when you've already made changes to your app's GitHub coordinates](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/rename-your-app#regain-access-when-youve-already-made-changes-to-your-apps-github-coordinates)

# Rename or change your app's GitHub coordinates

Streamlit Community Cloud identifies apps by their GitHub coordinates (owner, repository, branch, entrypoint file path). If you move or rename one of these coordinates without preparation, you will lose access to administer any associated app.

## Delete, rename, redeploy

If you need to rename your repository, move your entrypoint file, or otherwise change a deployed app's GitHub coordinates, do the following:

1. Delete your app.
2. Make your desired changes in GitHub.
3. Redeploy your app.

## Regain access when you've already made changes to your app's GitHub coordinates

If you have changed a repository so that Community Cloud can no longer find your app on GitHub, your app will be missing or shown as view-only. View-only means that you can't edit, reboot, delete, or view settings for your app. You can only access analytics.

You may be able to regain control as follows:

1. Revert the change you made to your app so that Community Cloud can see the owner, repository, branch, and entrypoint file it expects.

2. Sign out of Community Cloud and GitHub.

3. Sign back in to Community Cloud and GitHub.

4. If you have regained access, delete your app. Proceed with your original change, and redeploy your app.

If this does not restore access to your app, please [contact Snowflake support](https://docs.streamlit.io/knowledge-base/deploy/how-to-submit-a-support-case-for-streamlit-community-cloud) for assistance. They can delete your disconnected apps so you can redeploy them. For the quickest help, please provide a complete list of your affected apps by URL.


[Previous: Reboot your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app) [Next: Upgrade Python](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/upgrade-python)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly9kb2NzLnN0cmVhbWxpdC5pbzo0NDM.&hl=en&v=J79K9xgfxwT6Syzx-UyWdD89&size=invisible&cb=w0k28dx71kyf)