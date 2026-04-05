import marimo

__generated_with = "0.22.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import requests

    print('hello from marimo')
    return (mo,)


@app.cell
def _(mo):
    x = mo.ui.slider(1, 10)
    x
    return (x,)


@app.cell
def _(x):
    print(f"The value of x is {x.value}")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
