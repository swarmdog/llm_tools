# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

1. Contents
2. [No dependency file](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/upgrade-streamlit#no-dependency-file)
3. [With a dependency file](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/upgrade-streamlit#with-a-dependency-file)

# Upgrade your app's Streamlit version on Streamlit Community Cloud

Want to use a cool new Streamlit feature but your app on Streamlit Community Cloud is running an old version of the Streamlit library? If that's you, don't worry! Here's how to upgrade your app's Streamlit version, based on how you manage your [app dependencies](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies):

## No dependency file

When there is no dependencies file in your repository, your app will use the lastest Streamlit version that existed when it was last rebooted. In this case, simply [reboot your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app) and Community Cloud will install the latest version.

You may want to avoid getting into this situation if your app depends on a specific version of Streamlit. That is why we encourage you to use a dependency file and pin your desired version of Streamlit.

## With a dependency file

When your app includes a dependency file, reboot your app or change your dependency file as follows:

- If Streamlit is not included in your dependency file, reboot the app as described above.

Note that we don't recommend having an incomplete dependency file since `pip` won't be able to include `streamlit` when resolving compatible versions of your dependencies.

- If Streamlit is included in your dependency file, but the version is not pinned or capped, reboot the app as described above.

When Community Cloud reboots your app, it will re-resolve your dependency file. Your app will then have the latest version of all dependencies that are consistent with your dependency file.

- If Streamlit is included in your dependency file, and the version is pinned (e.g., `streamlit==1.37.0`), update your dependency file.

When you commit a change to your dependency file in your repository, Community Cloud will detect the change and automatically resolve the new dependencies. This is how you add, remove, or change all Python dependencies in general. You don't need to manually reboot your app, but you can if you want to.


[Previous: Upgrade Python](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/upgrade-python) [Next: Share your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly9kb2NzLnN0cmVhbWxpdC5pbzo0NDM.&hl=en&v=J79K9xgfxwT6Syzx-UyWdD89&size=invisible&cb=chv122qho4e4)