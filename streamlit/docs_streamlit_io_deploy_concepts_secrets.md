# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](https://docs.streamlit.io/deploy/concepts/www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

# Managing secrets when deploying your app

If you are connecting to data sources or external services, you will likely be handling secret information like credentials or keys. Secret information should be stored and transmitted in a secure manner. When you deploy your app, ensure that you understand your platform's features and mechanisms for handling secrets so you can follow best practice.

Avoid saving secrets directly in your code and keep `.gitignore` updated to prevent accidentally committing a local secret to your repository. For helpful reminders, see [Security reminders](https://docs.streamlit.io/develop/concepts/connections/security-reminders).

If you are using Streamlit Community Cloud, [Secrets management](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) allows you save environment variables and store secrets outside of your code. If you are using another platform designed for Streamlit, check if they have a built-in mechanism for working with secrets. In some cases, they may even support `st.secrets` or securely uploading your `secrets.toml` file.

For information about using `st.connection` with environment variables, see [Global secrets, managing multiple apps and multiple data stores](https://docs.streamlit.io/develop/concepts/connections/connecting-to-data#global-secrets-managing-multiple-apps-and-multiple-data-stores).

[Previous: Dependencies](https://docs.streamlit.io/deploy/concepts/dependencies) [Next: Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly9kb2NzLnN0cmVhbWxpdC5pbzo0NDM.&hl=en&v=J79K9xgfxwT6Syzx-UyWdD89&size=invisible&cb=xzya0ovf6k1z)