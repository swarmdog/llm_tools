# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](https://docs.streamlit.io/deploy/streamlit-community-cloud/www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

01. Contents
02. [Manage your app from your workspace](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#manage-your-app-from-your-workspace)
03. [Sort your apps](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#sort-your-apps)
04. [App overflow menus](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#app-overflow-menus)
05. [Manage your app directly from your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#manage-your-app-directly-from-your-app)
06. [Cloud logs](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#cloud-logs)
07. [App chrome](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#app-chrome)
08. [Manage your app in GitHub](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#manage-your-app-in-github)
09. [Update your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#update-your-app)
10. [Add or remove dependencies](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#add-or-remove-dependencies)
11. [App resources and limits](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#app-resources-and-limits)
12. [Resource limits](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#resource-limits)
13. [Good for the world](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#good-for-the-world)
14. [Optimizing your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#optimizing-your-app)
15. [Developer view](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#developer-view)
16. [App hibernation](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#app-hibernation)

# Manage your app

You can manage your deployed app from your workspace at [share.streamlit.io](https://share.streamlit.io/) or directly from `<your-custom-subdomain>.streamlit.app`. You can view, deploy, delete, reboot, or favorite an app.

## Manage your app from your workspace

Streamlit Community Cloud is organized into workspaces, which automatically group your apps according to their repository's owner in GitHub. Your workspace is indicated in the upper-left corner. For more information, see [Switching workspaces](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/explore-your-workspace#switching-workspaces).

To deploy or manage any app, always switch to the workspace matching the repository's owner first.

### Sort your apps

If you have many apps in your workspace, you can pin apps to the top by marking them as favorite ( _star_). For more information, see [Favorite your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/favorite-your-app).

### App overflow menus

Each app has a menu accessible from the overflow icon ( _more\_vert_) to the right.

- **Edit with Codespaces** — See [Edit your app with GitHub Codespaces](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/edit-your-app#edit-your-app-with-github-codespaces)
- **Reboot** — See [Reboot your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app)
- **Delete** — See [Delete your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/delete-your-app)
- **Analytics** — See [App analytics](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-analytics)
- **Settings** — See [App settings](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-settings)

![App overflow menu in your workspace](https://docs.streamlit.io/images/streamlit-community-cloud/workspace-app-overflow.png)

If you have view-only access to an app, all options in the app's menu will be disabled except analytics.

![View-only app overflow menu in your workspace](https://docs.streamlit.io/images/streamlit-community-cloud/workspace-view-only.png)

## Manage your app directly from your app

You can manage your deployed app directly from the app itself! Just make sure you are signed in to Community Cloud, and then visit your app.

### Cloud logs

1. From your app at `<your-custom-subdomain>.streamlit.app`, click " **Manage app**" in the lower-right corner.
![Access Cloud logs from Manage app in the lower-right corner of your app](https://docs.streamlit.io/images/streamlit-community-cloud/cloud-logs-open.png)
2. Once you've clicked on " **Manage app**", you will be able to view your app's logs. This is your primary place to troubleshoot any issues with your app.
![Streamlit Community Cloud logs](https://docs.streamlit.io/images/streamlit-community-cloud/cloud-logs.png)
3. You can access more developer options by clicking the overflow icon ( _more\_vert_) at the bottom of your Cloud logs. To conveniently download your logs, click " **Download log**."
![Download your Streamlit Community Cloud logs](https://docs.streamlit.io/images/streamlit-community-cloud/cloud-logs-menu-download.png)

Other options accessible from Cloud logs are:

- **Analytics** — See [App analytics](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-analytics).
- **Reboot app** — See [Reboot your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app).
- **Delete app** — See [Delete your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/delete-your-app).
- **Settings** — See [App settings](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-settings).
- **Your apps** — Takes you to your [app workspace](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#manage-your-app-from-your-workspace).
- **Documentation** — Takes you to our documentation.
- **Support** — Takes you to [our forums](https://discuss.streamlit.io/)!

![](https://docs.streamlit.io/images/streamlit-community-cloud/cloud-logs-menu-XL.png)

### App chrome

From your app at `<your-custom-subdomain>.streamlit.app`, you can always access the [app chrome](https://docs.streamlit.io/develop/concepts/architecture/app-chrome) just like you can when developing locally. The option to deploy your app is removed, but you can still clear your cache from here.

![App menus in Streamlit Community Cloud](https://docs.streamlit.io/images/streamlit-community-cloud/app-menu.png)

## Manage your app in GitHub

### Update your app

Your GitHub repository is the source for your app, so that means that any time you push an update to your repository you'll see it reflected in the app in almost real time. Try it out!

Streamlit also smartly detects whether you touched your dependencies, in which case it will automatically do a full redeploy for you—which will take a little more time. But since most updates don't involve dependency changes, you should usually see your app update in real time.

### Add or remove dependencies

To add or remove dependencies at any point, just update `requirements.txt` (Python dependenciess) or `packages.txt` (Linux dependencies), and commit the changes to your repository on GitHub. Community Cloud detects the change in your dependencies and automatically triggers (re)installation.

It is best practice to pin your Streamlit version in `requirements.txt`. Otherwise, the version may be auto-upgraded at any point without your knowledge, which could lead to undesired results (e.g. when we deprecate a feature in Streamlit).

## App resources and limits

### Resource limits

All Community Cloud users have access to the same resources and are subject to the same limits. These limits may change at any time without notice. If your app meets or exceeds its limits, it may slow down from throttling or become nonfunctional. The limits as of February 2024 are approximately as follows:

- CPU: 0.078 cores minimum, 2 cores maximum
- Memory: 690MB minimum, 2.7GBs maximum
- Storage: No minimum, 50GB maximum

Symptoms that your app is running out of resources include the following:

- Your app is running slowly.
- Your app displays "🤯 This app has gone over its resource limits."
- Your app displays "😦 Oh no."

### Good for the world

Streamlit offers increased resources for apps with good-for-the-world use cases. Generally, these apps are used by an educational institution or nonprofit organization, are part of an open-source project, or benefit the world in some way. If your app is **not** primarily used by a for-profit company you can [apply for increased resources](https://info.snowflake.com/streamlit-resource-increase-request.html).

### Optimizing your app

If your app is running slow or showing the error pages mentioned above, we first highly recommend going through and implementing the suggestions in the following blog posts to prevent your app from hitting the resource limits and to detect if your Streamlit app leaks memory:

- [Common app problems: Resource limits](https://blog.streamlit.io/common-app-problems-resource-limits/)
- [3 steps to fix app memory leaks](https://blog.streamlit.io/3-steps-to-fix-app-memory-leaks/)

If your app exceeds its resource limits, developers and viewers alike will see "😦 Oh no."

![App state: Oh no. Error running your app.](https://docs.streamlit.io/images/streamlit-community-cloud/app-state-oh-no.png)

If see "😦 Oh no." when viewing your app, first check your Cloud logs for any specific errors. If there are no errors in your Cloud logs you are likely dealing with a resource issue.

#### Developer view

If you are signed in to a developer account for an app over its limits, you can access " **Manage app**" from the lower-right corner of the app to reboot it and clear its memory. " **Manage app**" will be red and have a warning icon ( _error_).

![Developer view: Oh no. Error running your app.](https://docs.streamlit.io/images/streamlit-community-cloud/app-state-oh-no-developer.png)

### App hibernation

All apps without traffic for one weekday will go to sleep. The system checks apps for inactivity throughout each day as follows:

- Tuesday through Friday: All apps without traffic for 24 hours (one day) will go to sleep.
- Saturday through Monday: All apps without traffic for 72 hours (three days) will go to sleep.

Community Cloud hibernates apps to conserve resources and allow the best communal use of the platform. To keep your app awake, simply visit the app or commit to your app's repository, even if it's an empty commit!

When someone visits a sleeping app, they will see the sleeping page:

![App state: Zzzz. This app has gone to sleep due to inactivity.](https://docs.streamlit.io/images/streamlit-community-cloud/app-state-zzzz.png)

To wake the app up, click " **Yes, get this app back up!**" This can be done by _anyone_ who has access to view the app, not just the app developer!

You can see which of your apps are asleep from your workspace. Sleeping apps have a moon icon ( _bedtime_) to the right.

![App state: Zzzz. This app has gone to sleep due to inactivity](https://docs.streamlit.io/images/streamlit-community-cloud/workspace-sleeping-app.png)[Previous: Deploy your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app) [Next: App analytics](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-analytics)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly9kb2NzLnN0cmVhbWxpdC5pbzo0NDM.&hl=en&v=J79K9xgfxwT6Syzx-UyWdD89&size=invisible&cb=plh6f0cukmit)