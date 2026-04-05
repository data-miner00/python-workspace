# Python Workspace

A personal workspace to deal with data quickly, inspired by my colleague.

## Installation

For Nix users, initiate the Nix shell by running the `develop` command. This step is optional.

```
nix develop
```

Non-nix users are required to have UV preinstalled.

```
uv --version
```

After that, install and create a virtual environment for the project workspace.

```
uv pip install -r pyproject.toml
```

## Features

To execute these command line features, we'll need to activate the environment to our current command line.

```
source .venv/bin/activate
```

### Execute Codes

The code within the `src/work` can be execute easily with the Python command.

```
python src/work
```

This is possible because of the `__main__.py` file, which serves as the entry point for the executable scripts.

### Jupyter Notebook

Run interactive session for Python with Jupyter Notebook.

```
jupyter notebook --notebook-dir="notebooks"
```

This will automatically open the Jupyter Notebook UI in the browser with the url `localhost:8888`.

### Pytest

Unit tests are located at the `tests` folder. Pytest will be able to execute the tests correctly.

```
pytest
```

### Codespell

Typos for spellings can be checked with codespell.

```
codespell
```

The `.codespellrc` file provides a way to customize the behaviour.

### Linting

Ruff is used for linting Python codes.

```
ruff check .
```

### Formatting

Automated formatting of the codes to improve readability can be done by using Black.

```
black .
```

isort is used to sort imports alphabetically and separate to sections automatically.

```
isort .
```

## Enforce Rules (Not Recommended)

To ensure that the codebase is clean and free of trivial issues such as extra space or overlooked typos, the rules can be enforced before every commit to examine the codebase. `pre-commit` can be installed from Pip and it's included in Nix.

```
pip install pre-commit
```

After that, install the hooks by running

```
pre-commit install
```

It should now run the checks listed in `.pre-commit-config.yaml` file upon each attempted commit.

## Useful Links

- [uv](https://docs.astral.sh/uv/)
- [Poetry Docs](https://python-poetry.org/docs/cli/)
- [Jupyter Docs](https://docs.jupyter.org/en/latest/)
- [Ruff Configuration](https://docs.astral.sh/ruff/configuration/)
- [Codespell GitHub](https://github.com/codespell-project/codespell)
- [isort](https://pycqa.github.io/isort/)
