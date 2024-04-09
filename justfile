set shell := ["cmd.exe", "-c"]
notebooks_dir := "notebooks"

install:
    poetry install

env-info:
    poetry env info -p

chenv:
    poetry config virtualenvs.in-project true

lab:
    jupyter notebook --notebook-dir={{ notebooks_dir }}

typo:
    codespell -w
