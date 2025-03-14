# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

1. Contents
2. [Get the most out of app indexability](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/indexability#get-the-most-out-of-app-indexability)
3. [Make sure your app is public](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/indexability#make-sure-your-app-is-public)
4. [Choose a custom subdomain early](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/indexability#choose-a-custom-subdomain-early)
5. [Choose a descriptive app title](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/indexability#choose-a-descriptive-app-title)
6. [Customize your app's meta description](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/indexability#customize-your-apps-meta-description)
7. [What does my indexed app look like?](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/indexability#what-does-my-indexed-app-look-like)
8. [What if I don't want my app to be indexed?](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/indexability#what-if-i-dont-want-my-app-to-be-indexed)

# SEO and search indexability

When you deploy a public app to Streamlit Community Cloud, it is automatically indexed by search engines like Google and Bing on a weekly basis. 🎈 This means that anyone can find your app by [searching for its custom subdomain](https://www.google.com/search?q=traingenerator.streamlit.app) (e.g. "traingenerator.streamlit.app") or by searching for the app's title.

## Get the most out of app indexability

Here are some tips to help you get the most out of app indexability:

1. [Make sure your app is public](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/indexability#make-sure-your-app-is-public)
2. [Choose a custom subdomain early](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/indexability#choose-a-custom-subdomain-early)
3. [Choose a descriptive app title](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/indexability#choose-a-descriptive-app-title)
4. [Customize your app's meta description](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/indexability#customize-your-apps-meta-description)

### Make sure your app is public

All public apps hosted on Community Cloud are indexed by search engines. If your app is private, it will not be indexed by search engines. To make your private app public, read [Share your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app).

### Choose a custom subdomain early

Community Cloud automatically generates a subdomain for your app if you do not choose one. However, you can change your subdomain at any time! Custom subdomains modify your app URLs to reflect your app content, personal branding, or whatever you’d like. To learn how to change your app's subdomain, see [View or change your app's URL](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-settings#view-or-change-your-apps-url).

By choosing a custom subdomain, you can use it to help people find your app. For example, if you're deploying an app that generates training data, you might choose a subdomain like `traingenerator.streamlit.app`. This makes it easy for people to find your app by searching for "training generator" or "train generator streamlit app."

We recommend choosing a custom subdomain when you deploy your app. This ensures that your app is indexed by search engines using your custom subdomain, rather than the automatically generated one. If you choose a custom subdomain later, your app may be indexed multiple times—once using the default subdomain and once using your custom subdomain. In this case, your old URL will result in a 404 error which can confuse users who are searching for your app.

### Choose a descriptive app title

The meta title of your app is the text that appears in search engine results. It is also the text that appears in the browser tab when your app is open. By default, the meta title of your app is the same as the title of your app. However, you can customize the meta title of your app by setting the [`st.set_page_config`](https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config) parameter `page_title` to a custom string. For example:

`st.set_page_config(page_title="Traingenerator")
`

This will change the meta title of your app to "Traingenerator." This makes it easier for people to find your app by searching for "Traingenerator" or "train generator streamlit app":

![](https://docs.streamlit.io/images/streamlit-community-cloud/indexability-app-title.png)

Google search results for "train generator streamlit app"

### Customize your app's meta description

Meta descriptions are the short descriptions that appear in search engine results. Search engines use the meta description to help users understand what your app is about.

From our observations, search engines seem to favor the content in both `st.header` and `st.text` over `st.title`. If you put a description at the top of your app under `st.header` or `st.text`, there’s a good chance search engines will use this for the meta description.

## What does my indexed app look like?

If you're curious about what your app looks like in search engine results, you can type the following into Google Search:

`site:<your-custom-subdomain>.streamlit.app
`

Example: `site:traingenerator.streamlit.app`

![](https://docs.streamlit.io/images/streamlit-community-cloud/indexability-search-result.png)

Google search results for "site:traingenerator.streamlit.app"

## What if I don't want my app to be indexed?

If you don't want your app to be indexed by search engines, you can make it private. Read [Share your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app) to learn more about making your app private. Note: each workspace can only have one private app. If you want to make your app private, you must first delete any other private app in your workspace or make it public.

That said, Community Cloud is an open and free platform for the community to deploy, discover, and share Streamlit apps and code with each other. As such, we encourage you to make your app public so that it can be indexed by search engines and discovered by other Streamlit users and community members.

[Previous: Embed your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app) [Next: Share previews](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/share-previews)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly9kb2NzLnN0cmVhbWxpdC5pbzo0NDM.&hl=en&v=J79K9xgfxwT6Syzx-UyWdD89&size=invisible&cb=wsj5qaxj58zv)