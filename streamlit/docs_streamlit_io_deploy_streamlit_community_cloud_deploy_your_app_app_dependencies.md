# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

1. Contents
2. [Add Python dependencies](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies)
3. [Other Python package managers](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#other-python-package-managers)
4. [apt-get dependencies](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#apt-get-dependencies)

# App dependencies for your Community Cloud app

The main reason that apps fail to build properly is because Streamlit Community Cloud can't find your dependencies! There are two kinds of dependencies your app might have: Python dependencies and external dependencies. Python dependencies are other Python packages (just like Streamlit!) that you `import` into your script. External dependencies are less common, but they include any other software your script needs to function properly. Because Community Cloud runs on Linux, these will be Linux dependencies installed with `apt-get` outside the Python environment.

For your dependencies to be installed correctly, make sure you:

1. Add a [requirements file](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies) for Python dependencies.
2. Optional: To manage any external dependencies, add a `packages.txt` file.

_push\_pin_

#### Note

Python requirements files should be placed either in the root of your repository or in the same
directory as your app's entrypoint file.

## Add Python dependencies

With each `import` statement in your script, you are bringing in a Python dependency. You need to tell Community Cloud how to install those dependencies through a Python package manager. We recommend using a `requirements.txt` file, which is based on `pip`.

You should _not_ include [built-in Python libraries](https://docs.python.org/3/py-modindex.html) like `math`, `random`, or `distutils` in your `requirements.txt` file. These are a part of Python and aren't installed separately. Also, Community Cloud has `streamlit` installed by default. You don't strictly need to include `streamlit` unless you want to pin or restrict the version. If you deploy an app without a `requirements.txt` file, your app will run in an environment with just `streamlit` (and its dependencies) installed.

_priority\_high_

#### Important

The version of Python you use is important! Built-in libraries change between versions of Python and other libraries may have specific version requirements, too. Whenever Streamlit supports a new version of Python, Community Cloud quickly follows to default to that new version of Python. Always develop your app in the same version of Python you will use to deploy it. For more information about setting the version of Python when you deploy your app, see [Optional: Configure secrets and Python version](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy#optional-configure-secrets-and-python-version).

If you have a script like the following, no extra dependencies would be needed since `pandas` and `numpy` are installed as direct dependencies of `streamlit`. Similarly, `math` and `random` are built into Python.

`import streamlit as st
import pandas as pd
import numpy as np
import math
import random
st.write("Hi!")
`

However, a valid `requirements.txt` file would be:

`streamlit
pandas
numpy
`

Alternatively, if you needed to specify certain versions, another valid example would be:

`streamlit==1.24.1
pandas>2.0
numpy<=1.25.1
`

In the above example, `streamlit` is pinned to version `1.24.1`, `pandas` must be strictly greater than version 2.0, and `numpy` must be at-or-below version 1.25.1. Each line in your `requirements.txt` file is effectively what you would like to `pip install` into your cloud environment.

_star_

#### Tip

To learn about limitations of Community Cloud's Python environments, see [Community Cloud status and limitations](https://docs.streamlit.io/deploy/streamlit-community-cloud/status#python-environments).

### Other Python package managers

There are other Python package managers in addition to `pip`. If you want to consider alternatives to using a `requirements.txt` file, Community Cloud will use the first dependency file it finds. Community Cloud will search the directory where your entrypoint file is, then it will search the root of your repository. In each location, dependency files are prioritized in the following order:

| Recognized Filename | Python Package Manager |
| --- | --- |
| `uv.lock` | [uv](https://docs.astral.sh/uv/concepts/projects/sync/) |
| `Pipfile` | [pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html) |
| `environment.yml` | [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually) |
| `requirements.txt` | [pip](https://pip.pypa.io/en/stable/user_guide/#requirements-files)† |
| `pyproject.toml` | [poetry](https://python-poetry.org/docs/basic-usage/) |

† For efficiency, Community Cloud will attempt to process `requirements.txt` with `uv`, but will fall back to `pip` if needed. `uv` is generally faster and more efficient than `pip`.

_priority\_high_

#### Warning

You should only use one dependency file for your app. If you include more than one (e.g. `requirements.txt` and `environment.yaml`), only the first file encountered will be used as described above, with any dependency file in your entrypoint file's directory taking precedence over any dependency file in the root of your repository.

## apt-get dependencies

For many apps, a `packages.txt` file is not required. However, if your script requires any software to be installed that is not a Python package, you need a `packages.txt` file. Community Cloud is built on Debian Linux. Anything you want to `apt-get install` must go in your `packages.txt` file. To browse available packages that can be installed, see the Debian 11 ("bullseye") [package list](https://packages.debian.org/bullseye/).

If `packages.txt` exists in the root directory of your repository we automatically detect it, parse it, and install the listed packages. You can read more about apt-get in [Linux documentation](https://linux.die.net/man/8/apt-get).

Add **apt-get** dependencies to `packages.txt` — one package name per line. For example, [`mysqlclient`](https://github.com/PyMySQL/mysqlclient) is a Python package which requires additional software be installed to function. A valid `packages.txt` file to enable `mysqlclient` would be:

`    build-essential
    pkg-config
    default-libmysqlclient-dev
`

[Previous: File organization](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization) [Next: Secrets management](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly9kb2NzLnN0cmVhbWxpdC5pbzo0NDM.&hl=en&v=J79K9xgfxwT6Syzx-UyWdD89&size=invisible&cb=neucd46251ug)