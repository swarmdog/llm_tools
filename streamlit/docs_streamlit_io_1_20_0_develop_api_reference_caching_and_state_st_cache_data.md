# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](https://docs.streamlit.io/1.20.0/develop/api-reference/caching-and-state/www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

_priority\_high_

#### Warning

You are reading the documentation for Streamlit version 1.20.0, but [1.43.0](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data) is the latest version available.

1. Contents
2. [st.cache\_data](https://docs.streamlit.io/1.20.0/develop/api-reference/caching-and-state/st.cache_data#stcache_data)
3. [st.cache\_data.clear](https://docs.streamlit.io/1.20.0/develop/api-reference/caching-and-state/st.cache_data#stcache_dataclear)
4. [Example](https://docs.streamlit.io/1.20.0/develop/api-reference/caching-and-state/st.cache_data#example)
5. [CachedFunc.clear](https://docs.streamlit.io/1.20.0/develop/api-reference/caching-and-state/st.cache_data#cachedfuncclear)
6. [Using Streamlit commands in cached functions](https://docs.streamlit.io/1.20.0/develop/api-reference/caching-and-state/st.cache_data#using-streamlit-commands-in-cached-functions)
7. [Static elements](https://docs.streamlit.io/1.20.0/develop/api-reference/caching-and-state/st.cache_data#static-elements)
8. [Input widgets](https://docs.streamlit.io/1.20.0/develop/api-reference/caching-and-state/st.cache_data#input-widgets)

_star_

#### Tip

This page only contains information on the `st.cache_data` API. For a deeper dive into caching and how to use it, check out [Caching](https://docs.streamlit.io/develop/concepts/architecture/caching).

## st.cache\_data

Streamlit VersionVersion 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0Streamlit in Snowflake

Decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).

Cached objects are stored in "pickled" form, which means that the return
value of a cached function must be pickleable. Each caller of the cached
function gets its own copy of the cached data.

You can clear a function's cache with `func.clear()` or clear the entire
cache with `st.cache_data.clear()`.

To cache global resources, use `st.cache_resource` instead. Learn more
about caching at [https://docs.streamlit.io/library/advanced-features/caching](https://docs.streamlit.io/library/advanced-features/caching).

| Function signature [\[source\]](https://github.com/streamlit/streamlit/blob/1.20.0/lib/streamlit/runtime/caching/cache_data_api.py#L378 "View st.cache_data source code on GitHub") |
| --- |
| st.cache\_data(func=None, \*, ttl, max\_entries, show\_spinner, persist, experimental\_allow\_widgets) |
| --- |
| Parameters |
| func(callable) | The function to cache. Streamlit hashes the function's source code. |
| ttl(float or timedelta or None) | The maximum number of seconds to keep an entry in the cache, or<br>None if cache entries should not expire. The default is None.<br>Note that ttl is incompatible with `persist="disk"` \- `ttl` will be<br>ignored if `persist` is specified. |
| max\_entries(int or None) | The maximum number of entries to keep in the cache, or None<br>for an unbounded cache. (When a new entry is added to a full cache,<br>the oldest cached entry will be removed.) The default is None. |
| show\_spinner(boolean or string) | Enable the spinner. Default is True to show a spinner when there is<br>a "cache miss" and the cached data is being created. If string,<br>value of show\_spinner param will be used for spinner text. |
| persist(str or boolean or None) | Optional location to persist cached data to. Passing "disk" (or True)<br>will persist the cached data to the local disk. None (or False) will disable<br>persistence. The default is None. |
| experimental\_allow\_widgets(boolean) | Allow widgets to be used in the cached function. Defaults to False.<br>Support for widgets in cached functions is currently experimental.<br>Setting this parameter to True may lead to excessive memory use since the<br>widget value is treated as an additional input parameter to the cache.<br>We may remove support for this option at any time without notice. |

#### Example

> ```python
> import streamlit as st
>
> @st.cache_data
> def fetch_and_clean_data(url):
>     # Fetch data from URL here, and then clean it up.
>     return data
>
> d1 = fetch_and_clean_data(DATA_URL_1)
> # Actually executes the function, since this is the first time it was
> # encountered.
>
> d2 = fetch_and_clean_data(DATA_URL_1)
> # Does not execute the function. Instead, returns its previously computed
> # value. This means that now the data in d1 is the same as in d2.
>
> d3 = fetch_and_clean_data(DATA_URL_2)
> # This is a different URL, so the function executes.
> ```
>
> Copy
>
> To set the `persist` parameter, use this command as follows:
>
> ```python
> import streamlit as st
>
> @st.cache_data(persist="disk")
> def fetch_and_clean_data(url):
>     # Fetch data from URL here, and then clean it up.
>     return data
> ```
>
> Copy
>
> By default, all parameters to a cached function must be hashable.
> Any parameter whose name begins with `_` will not be hashed. You can use
> this as an "escape hatch" for parameters that are not hashable:
>
> ```python
> import streamlit as st
>
> @st.cache_data
> def fetch_and_clean_data(_db_connection, num_rows):
>     # Fetch data from _db_connection here, and then clean it up.
>     return data
>
> connection = make_database_connection()
> d1 = fetch_and_clean_data(connection, num_rows=10)
> # Actually executes the function, since this is the first time it was
> # encountered.
>
> another_connection = make_database_connection()
> d2 = fetch_and_clean_data(another_connection, num_rows=10)
> # Does not execute the function. Instead, returns its previously computed
> # value - even though the _database_connection parameter was different
> # in both calls.
> ```
>
> Copy
>
> A cached function's cache can be procedurally cleared:
>
> ```python
> import streamlit as st
>
> @st.cache_data
> def fetch_and_clean_data(_db_connection, num_rows):
>     # Fetch data from _db_connection here, and then clean it up.
>     return data
>
> fetch_and_clean_data.clear()
> # Clear all cached entries for this function.
> ```
>
> Copy

_priority\_high_

#### Warning

`st.cache_data` implicitly uses the `pickle` module, which is known to be insecure. Anything your cached function returns is pickled and stored, then unpickled on retrieval. Ensure your cached functions return trusted values because it is possible to construct malicious pickle data that will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode or that could have been tampered with. **Only load data you trust**.

## st.cache\_data.clear

Streamlit VersionVersion 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0Streamlit in Snowflake

Clear all in-memory and on-disk data caches.

| Function signature [\[source\]](https://github.com/streamlit/streamlit/blob/1.20.0/lib/streamlit/runtime/caching/cache_data_api.py#L541 "View st.cache_data.clear source code on GitHub") |
| --- |
| st.cache\_data.clear(self) |
| --- |

#### Example

In the example below, pressing the "Clear All" button will clear memoized values from all functions decorated with `@st.cache_data`.

`import streamlit as st
@st.cache_data
def square(x):
    return x**2
@st.cache_data
def cube(x):
    return x**3
if st.button("Clear All"):
    # Clear values from *all* all in-memory and on-disk data caches:
    # i.e. clear values from both square and cube
    st.cache_data.clear()
`

## CachedFunc.clear

Streamlit VersionVersion 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0Streamlit in Snowflake

_priority\_high_

#### Warning

This method did not exist in version `1.20.0` of Streamlit.

## Using Streamlit commands in cached functions

### Static elements

Since version 1.16.0, cached functions can contain Streamlit commands! For example, you can do this:

`@st.cache_data
def get_api_data():
    data = api.get(...)
    st.success("Fetched data from API!")  # 👈 Show a success message
    return data
`

As we know, Streamlit only runs this function if it hasn’t been cached before. On this first run, the `st.success` message will appear in the app. But what happens on subsequent runs? It still shows up! Streamlit realizes that there is an `st.` command inside the cached function, saves it during the first run, and replays it on subsequent runs. Replaying static elements works for both caching decorators.

You can also use this functionality to cache entire parts of your UI:

`@st.cache_data
def show_data():
    st.header("Data analysis")
    data = api.get(...)
    st.success("Fetched data from API!")
    st.write("Here is a plot of the data:")
    st.line_chart(data)
    st.write("And here is the raw data:")
    st.dataframe(data)
`

### Input widgets

You can also use [interactive input widgets](https://docs.streamlit.io/develop/api-reference/widgets) like `st.slider` or `st.text_input` in cached functions. Widget replay is an experimental feature at the moment. To enable it, you need to set the `experimental_allow_widgets` parameter:

`@st.cache_data(experimental_allow_widgets=True)  # 👈 Set the parameter
def get_data():
    num_rows = st.slider("Number of rows to get")  # 👈 Add a slider
    data = api.get(..., num_rows)
    return data
`

Streamlit treats the slider like an additional input parameter to the cached function. If you change the slider position, Streamlit will see if it has already cached the function for this slider value. If yes, it will return the cached value. If not, it will rerun the function using the new slider value.

Using widgets in cached functions is extremely powerful because it lets you cache entire parts of your app. But it can be dangerous! Since Streamlit treats the widget value as an additional input parameter, it can easily lead to excessive memory usage. Imagine your cached function has five sliders and returns a 100 MB DataFrame. Then we’ll add 100 MB to the cache for _every permutation_ of these five slider values – even if the sliders do not influence the returned data! These additions can make your cache explode very quickly. Please be aware of this limitation if you use widgets in cached functions. We recommend using this feature only for isolated parts of your UI where the widgets directly influence the cached return value.

_priority\_high_

#### Warning

Support for widgets in cached functions is currently experimental. We may change or remove it anytime without warning. Please use it with care!

_push\_pin_

#### Note

Two widgets are currently not supported in cached functions: `st.file_uploader` and `st.camera_input`. We may support them in the future. Feel free to [open a GitHub issue](https://github.com/streamlit/streamlit/issues) if you need them!

[Previous: Caching & state](https://docs.streamlit.io/develop/api-reference/caching-and-state) [Next: st.cache\_resource](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly9kb2NzLnN0cmVhbWxpdC5pbzo0NDM.&hl=en&v=J79K9xgfxwT6Syzx-UyWdD89&size=invisible&cb=z0pes876y62s)