# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](https://docs.streamlit.io/develop/api-reference/www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

1. Contents
2. [Caching](https://docs.streamlit.io/develop/api-reference/caching-and-state#caching)
3. [Browser and server state](https://docs.streamlit.io/develop/api-reference/caching-and-state#browser-and-server-state)
4. [Deprecated commands](https://docs.streamlit.io/develop/api-reference/caching-and-state#deprecated-commands)

# Caching and state

Optimize performance and add statefulness to your app!

## Caching

Streamlit provides powerful [cache primitives](https://docs.streamlit.io/develop/concepts/architecture/caching) for data and global resources. They allow your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations.

[**Cache data** \\
Function decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).\\
\\
`@st.cache_data\\
def long_function(param1, param2):\\
# Perform expensive computation here or\\
# fetch data from the web here\\
return data\\
`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data) [**Cache resource** \\
Function decorator to cache functions that return global resources (e.g. database connections, ML models).\\
\\
`@st.cache_resource\\
def init_model():\\
# Return a global resource here\\
return pipeline(\\
    "sentiment-analysis",\\
    model="distilbert-base-uncased-finetuned-sst-2-english"\\
)\\
`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource)

## Browser and server state

Streamlit re-executes your script with each user interaction. Widgets have built-in statefulness between reruns, but Session State lets you do more!

[**Context** \\
`st.context` provides a read-only interface to access cookies and headers.\\
\\
`st.context.cookies\\
st.context.headers\\
`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.context) [**Session State** \\
Save data between reruns and across pages.\\
\\
`st.session_state["foo"] = "bar"\\
`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state) [**Query parameters** \\
Get, set, or clear the query parameters that are shown in the browser's URL bar.\\
\\
`st.query_params[key] = value\\
st.query_params.clear()\\
`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.query_params)

## Deprecated commands

[_delete_\\
**Get query parameters** \\
Get query parameters that are shown in the browser's URL bar.\\
\\
`param_dict = st.experimental_get_query_params()\\
`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.experimental_get_query_params) [_delete_\\
**Set query parameters** \\
Set query parameters that are shown in the browser's URL bar.\\
\\
`st.experimental_set_query_params(\\
{"show_all"=True, "selected"=["asia", "america"]}\\
)\\
`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.experimental_set_query_params)[Previous: Execution flow](https://docs.streamlit.io/develop/api-reference/execution-flow) [Next: st.cache\_data](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly9kb2NzLnN0cmVhbWxpdC5pbzo0NDM.&hl=en&v=J79K9xgfxwT6Syzx-UyWdD89&size=invisible&cb=vaofuf95gjqr)