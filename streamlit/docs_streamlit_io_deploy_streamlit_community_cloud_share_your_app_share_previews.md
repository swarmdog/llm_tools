# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

1. Contents
2. [Titles](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/share-previews#titles)
3. [Descriptions](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/share-previews#descriptions)
4. [Preview images](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/share-previews#preview-images)
5. [Switching your app from public to private](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/share-previews#switching-your-app-from-public-to-private)

# Share previews

Social media sites generate a card with a title, preview image, and description when you share a link. This feature is called a "share preview." In the same way, when you share a link to a public Streamlit app on social media, a share preview is also generated. Here's an example of a share preview for a public Streamlit app posted on Twitter:

![](https://docs.streamlit.io/images/streamlit-community-cloud/share-preview-twitter-annotated.png)

Share preview for a public Streamlit app

_push\_pin_

#### Note

Share previews are generated only for public apps deployed on Streamlit Community Cloud.

## Titles

The title is the text that appears at the top of the share preview. The text also appears in the browser tab when you visit the app. You should set the title to something that will make sense to your app's audience and describe what the app does. It is best practice to keep the title concise, ideally under 60 characters.

There are two ways to set the title of a share preview:

1. Set the `page_title` parameter in [`st.set_page_config()`](https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config) to your desired title. E.g.:


`import streamlit as st
st.set_page_config(page_title="My App")
# ... rest of your app
`

2. If you don't set the `page_title` parameter, the title of the share preview will be the name of your app's GitHub repository. For example, the default title for an app hosted on GitHub at [github.com/jrieke/traingenerator](https://github.com/jrieke/traingenerator) will be "traingenerator".


## Descriptions

The description is the text that appears below the title in the share preview. The description should summarize what the app does and ideally should be under 100 characters.

Streamlit pulls the description from the README in the app's GitHub repository. If there is no README, the description will default to:

_This app was built in Streamlit! Check it out and visit [https://streamlit.io](https://streamlit.io/) for more awesome community apps. 🎈_

![](https://docs.streamlit.io/images/streamlit-community-cloud/share-preview-private-app.png)

Default share preview when a description is missing

If you want your share previews to look great and want users to share your app and click on your links, you should write a good description in the README of your app’s GitHub repository.

## Preview images

Streamlit Community Cloud takes a screenshot of your app once a day and uses it as the preview image, unlike titles and descriptions which are pulled directly from your app's code or GitHub repository. This screenshot may take up to 24 hours to update.

### Switching your app from public to private

If you initially made your app public and later decided to make it private, we will stop generating share previews for the app. However, it may take up to 24 hours for the share previews to stop appearing.

[Previous: Search indexability](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/indexability) [Next: Manage your account](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly9kb2NzLnN0cmVhbWxpdC5pbzo0NDM.&hl=en&v=J79K9xgfxwT6Syzx-UyWdD89&size=invisible&cb=dlkajzh3r25h)