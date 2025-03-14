# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

# Upgrade your app's Python version on Community Cloud

Dependencies within Python can be upgraded in place by simply changing your environment configuration file (typically `requirements.txt`). However, Python itself can't be changed after deployment.

When you deploy an app, you can select the version of Python through the " **Advanced settings**" dialog. After you have deployed an app, you must delete it and redeploy it to change the version of Python it uses.

1. Take note of your app's settings:


   - Current, custom subdomain.
   - GitHub coordinates (repository, branch, and entrypoint file path).
   - Secrets.

When you delete an app, its custom subdomain is immediately available for reuse.

2. [Delete your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/delete-your-app).

3. [Deploy your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).
1. On the deployment page, select your app's GitHub coordinates.
2. Set your custom domain to match your deleted instance.
3. Click " **Advanced settings**."
4. Choose your desired version of Python.
5. Optional: If your app had secrets, re-enter them.
6. Click " **Save**."
7. Click " **Deploy**."

In a few minutes, Community Cloud will redirect you to your redployed app.

[Previous: Rename your app in GitHub](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/rename-your-app) [Next: Upgrade Streamlit](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/upgrade-streamlit)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly9kb2NzLnN0cmVhbWxpdC5pbzo0NDM.&hl=en&v=J79K9xgfxwT6Syzx-UyWdD89&size=invisible&cb=5sodfs97eqzq)