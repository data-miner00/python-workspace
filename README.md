# Python Workspace

A personal workspace to deal with data quickly, inspired by my colleague.

## Installation

For Nix users, initiate the Nix shell by running the `develop` command. This step is optional.

```
nix develop
```

Poetry is required to manage the virtual environment and packages. If Poetry is not installed globally on your system, run the following Pip install command. Nix users can skip this step as the dependency is already installed.

```
pip install poetry
```

After that, install and create a virtual environment for the project workspace.

```
poetry install
```

## Features

To execute these command line features, we'll need to activate the environment to our current command line.

```
poetry shell
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

## Useful Links

- [Poetry Docs](https://python-poetry.org/docs/cli/)
- [Jupyter Docs](https://docs.jupyter.org/en/latest/)
- [Ruff Configuration](https://docs.astral.sh/ruff/configuration/)
- [Codespell GitHub](https://github.com/codespell-project/codespell)
