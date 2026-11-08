# uv and ruff

> **In one sentence:** uv installs Python, creates your project and installs the libraries it needs, and ruff checks and tidies your code automatically.

## Why it matters

Sooner or later you will want code that other people wrote: a library to build a website, to talk to a database, to test your programs. You need a reliable way to install those libraries, to keep each project's libraries separate, and to let someone else recreate your project exactly. uv does all of that with a handful of short commands. ruff then keeps your code clean and consistent, so you spend your attention on what the code does, not on spaces and commas.

## Analogy

Think of each project as a **kitchen**. uv is the person who sets up the kitchen for you: it brings the right stove (the Python version), stocks the pantry with the ingredients the recipe needs (the libraries), and writes down the exact shopping list, with brands and sizes, so anyone can set up an identical kitchen later.

ruff is the **spell checker and auto-indent** of your code. A spell checker underlines mistakes as you write (that is ruff's **linter**), and an auto-format button makes the text look tidy and consistent (that is ruff's **formatter**). Neither one writes the recipe for you. They only make sure it is written well.

## The idea, step by step

### Libraries and PyPI

A **library** (also called a **package**) is code someone else wrote and shared so you can use it. Python already comes with many libraries, like `random`, `json` and `datetime`. That collection is called the **standard library**, and you can `import` it right away.

Thousands of other libraries live on **PyPI** (the Python Package Index, [pypi.org](https://pypi.org)), a free public catalog. `flask` (websites), `requests` (talking to other websites) and `pytest` (tests) all live there. To use them, you first have to download and install them. That is uv's job.

### What uv is, and why not pip

**uv** is one tool that does everything around a Python project:

- installs Python itself, in the version you need;
- creates a project folder with the right files;
- creates the project's **virtual environment**: a private folder (`.venv`) where the project's libraries live, so that two projects never fight over different versions of the same library;
- installs and removes libraries, and records them in a list;
- runs your code inside that environment.

You will see many tutorials online that use **pip**, the older installer that comes with Python. pip only installs libraries; for everything else you need extra tools and extra steps (creating and "activating" the virtual environment by hand, keeping a list up to date yourself). uv does all of it, and it is much faster. That is why this course uses uv.

### Installing uv

You install uv once per computer. In **Windows PowerShell**:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

On **macOS or Linux**:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close the terminal and open a new one, then check that it worked:

```console
PS C:\Users\you> uv --version
uv 0.11.32
```

Your version number will probably be different. That is fine.

### Installing Python with uv

If you do not have Python yet, or want a newer version, uv can install it:

```powershell
uv python install
```

You do not have to remember where it went. uv finds it by itself whenever you run a project.

### Creating a project: `uv init`

Go to your projects folder and create a new project:

```console
PS C:\Users\you\Projects> uv init shop
Initialized project `shop` at `C:\Users\you\Projects\shop`
PS C:\Users\you\Projects> cd shop
```

uv creates a folder with these files:

<!-- no-verify -->
```text
shop/
├── .python-version   # which Python version this project uses
├── README.md         # a description of the project, for people
├── main.py           # a first program, ready to run
└── pyproject.toml    # the project's "ID card": name, Python version, libraries
```

It also starts a Git repository and a `.gitignore` for you if the folder is not inside one already.

`pyproject.toml` is a plain text file. Right after `uv init` it looks like this:

```toml
[project]
name = "shop"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = []
```

`dependencies` is the list of libraries the project needs. It is empty for now.

### Running code: `uv run`

Instead of `python main.py`, you now type:

```console
PS C:\Users\you\Projects\shop> uv run main.py
Using CPython 3.12.8
Creating virtual environment at: .venv
Hello from shop!
```

The first time, uv creates the virtual environment (`.venv`) on its own. You never have to "activate" anything: `uv run` always uses the project's environment. If you see `(.venv)` and `activate` in online tutorials, that is the manual way uv saves you from.

### Adding and removing libraries: `uv add` and `uv remove`

```console
PS C:\Users\you\Projects\shop> uv add requests
Resolved 6 packages in 412ms
Installed 5 packages in 38ms
 + requests==2.32.3
 ...
```

uv downloads `requests` (and the libraries `requests` itself needs), installs it in `.venv`, and writes it in `pyproject.toml`:

```toml
dependencies = [
    "requests>=2.32.3",
]
```

To remove a library: `uv remove requests`.

Some libraries are only for **you, the developer**, not for the program itself: tools to test or check code. Add them with `--dev`:

```powershell
uv add --dev pytest
```

They go into a separate list in `pyproject.toml`, called `dev`.

### `pyproject.toml` and `uv.lock`: both go into Git

After `uv add`, a new file appears: `uv.lock`.

- `pyproject.toml` says **what** the project needs, in general terms: "requests, version 2.32.3 or newer". You read and edit this one.
- `uv.lock` records the **exact** versions that were installed, of every library and of the libraries they depend on. uv writes it; you never edit it by hand.

Both go into Git. With them, anyone gets exactly the same libraries you have. The `.venv` folder, on the other hand, does **not** go into Git: it is big, it is different on each computer, and it can always be recreated. `uv init` already lists it in `.gitignore`:

```text
.venv/
```

### Cloning someone's project: `uv sync`

When you clone a project that uses uv, its `.venv` is not there (it was never committed). One command rebuilds it from `pyproject.toml` and `uv.lock`:

```console
PS C:\Users\you\Projects> git clone https://github.com/someone/shop
PS C:\Users\you\Projects> cd shop
PS C:\Users\you\Projects\shop> uv sync
```

In fact, `uv run` also does this automatically when something is missing. `uv sync` is just the explicit way.

### A one-off: `uv run --with`

Sometimes you want to try a library in a single script without adding it to any project:

```powershell
uv run --with requests try_requests.py
```

uv installs `requests` in a temporary place just for this run. Nothing changes in `pyproject.toml`.

### If you see pip in a tutorial

Most tutorials online still use pip. Translate them like this:

| You see | You type |
|---|---|
| `pip install flask` | `uv add flask` |
| `pip install pytest` (a tool for you) | `uv add --dev pytest` |
| `python app.py` | `uv run app.py` |
| `pytest` | `uv run pytest` |
| `python -m venv .venv` and `activate` | nothing: uv does it for you |
| `pip install -r requirements.txt` | `uv sync` |
| `requirements.txt` | `pyproject.toml` + `uv.lock` |

### ruff: checking your code

A **linter** reads your code without running it and points out problems: an import you never use, a variable that does not exist, a comparison that is probably a mistake. ruff is a very fast linter (and formatter) for Python. Add it as a developer tool:

```powershell
uv add --dev ruff
```

Imagine this file:

<!-- no-verify -->
```python
# prices.py
import random


def with_tax(price):
    total = price * 1.10
    return round(price * 1.10, 2)
```

Ask ruff to check it:

```console
PS C:\Users\you\Projects\shop> uv run ruff check
prices.py:2:8: F401 [*] `random` imported but unused
prices.py:6:5: F841 Local variable `total` is assigned to but never used
Found 2 errors.
[*] 1 fixable with the `--fix` option.
```

Each line says the file, the line and the column, a code (`F401`), and what is wrong. Neither problem breaks the program, but both are clutter that confuses whoever reads the code next (including future you).

Problems marked `[*]` can be fixed automatically:

```powershell
uv run ruff check --fix
```

### ruff: formatting your code

A **formatter** rewrites the *layout* of your code, never what it does: spaces around `=`, blank lines between functions, quotes, long lines. Before:

<!-- no-verify -->
```python
def area(width,height):
    return width*height
items=['cup','plate']
```

Run:

```powershell
uv run ruff format
```

After:

<!-- no-verify -->
```python
def area(width, height):
    return width * height


items = ["cup", "plate"]
```

Same program, easier to read. Because everybody's code ends up formatted the same way, nobody has to argue about style.

### Configuring ruff in `pyproject.toml`

ruff works with no configuration at all. If you want to change something, add a `[tool.ruff]` section to `pyproject.toml`. This course itself uses:

```toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "W", "B", "I", "UP"]
```

`line-length` is the longest line allowed. `select` picks families of rules: for example `F` finds mistakes like unused imports, and `I` keeps imports in order. You do not need to understand every family now; start with these and adjust later.

### ruff in the editor

Install the **Ruff** extension in Cursor or VS Code (Extensions panel, search "Ruff", the one by Astral). Then turn on **Format On Save** in the settings (search "format on save"). From then on, problems are underlined while you type, and every `Ctrl+S` formats the file.

### Convention over configuration, again

In module 00 you met **convention over configuration**: agreeing on a default (all projects in `Projects`, no spaces in names) so you stop making the same small decisions over and over. uv and ruff are the same idea for code. Every project has the same shape (`pyproject.toml`, `uv.lock`, `.venv`), runs with the same command (`uv run`), and is formatted the same way (`ruff format`). Open any uv project and you already know where everything is.

## Common mistakes

### `uv` is not recognized

```console
PS C:\Users\you> uv --version
uv : The term 'uv' is not recognized as the name of a cmdlet, function, script file, or operable program.
```

The terminal was opened **before** uv was installed, so it does not know about it yet. **Fix:** close the terminal, open a new one, try again. If it still fails, run the installer again and read its last lines: it tells you which folder it added to the PATH.

### Running with `python` instead of `uv run`

```console
PS C:\Users\you\Projects\shop> python try_requests.py
ModuleNotFoundError: No module named 'requests'
```

You installed `requests` with `uv add`, so it lives in the project's `.venv`. Plain `python` uses the Python of your computer, which knows nothing about `.venv`. **Fix:** `uv run try_requests.py`.

### Running uv commands in the wrong folder

`uv add` and `uv run` look for `pyproject.toml` in the current folder (and the folders above it). If you are in `Projects` instead of `Projects\shop`, uv says there is no project, or changes the wrong one. **Fix:** check where you are with `pwd` and `cd` into the project folder first.

### Committing the `.venv` folder

If `git status` lists hundreds of files inside `.venv`, it is missing from `.gitignore`. **Fix:** add the line `.venv/` to `.gitignore` before committing. Commit `pyproject.toml` and `uv.lock` instead: they are enough to rebuild everything.

### Editing `uv.lock` by hand

`uv.lock` is written by uv. If you edit it, the next `uv sync` may fail or undo your change. **Fix:** change libraries only with `uv add` and `uv remove`.

## Exercises

### Predict the output

#### Exercise 1: Which files go into Git?

A uv project contains: `main.py`, `pyproject.toml`, `uv.lock`, `.venv/`, `.python-version`, `README.md`, `__pycache__/`. Which ones do you commit?

<details>
<summary>Show answer</summary>

Commit `main.py`, `pyproject.toml`, `uv.lock`, `.python-version` and `README.md`.

Do not commit `.venv/` (big, different on each computer, rebuilt by `uv sync`) or `__pycache__/` (files Python creates by itself).

</details>

#### Exercise 2: What changes in `pyproject.toml`?

You run these commands, in this order, in a new project. What does the `dependencies` list contain at the end?

```powershell
uv add requests
uv add flask
uv add --dev ruff
uv remove requests
```

<details>
<summary>Show answer</summary>

Only `flask`. `requests` was added and then removed, and `ruff` went to the separate `dev` list because of `--dev`.

</details>

#### Exercise 3: Read the ruff report

What is ruff complaining about?

```text
report.py:1:8: F401 [*] `json` imported but unused
report.py:9:5: F841 Local variable `count` is assigned to but never used
```

<details>
<summary>Show answer</summary>

1. Line 1 imports `json`, but the file never uses it. `uv run ruff check --fix` removes the line.
2. Line 9 creates a variable `count` that is never read afterwards. Either the line is useless (delete it) or you forgot to use `count` somewhere (a real bug). ruff cannot know which, so it does not fix it for you.

</details>

### Fix the bug

#### Exercise 4: The tutorial from the internet

A tutorial says:

```bash
python -m venv .venv
source .venv/bin/activate
pip install flask
python app.py
```

Rewrite it the uv way, starting from a new project called `site`.

<details>
<summary>Show answer</summary>

```powershell
uv init site
cd site
uv add flask
uv run app.py
```

No virtual environment commands: `uv add` and `uv run` create and use `.venv` automatically.

</details>

#### Exercise 5: It worked on my computer

Your friend cloned your project and typed `python main.py`. She got `ModuleNotFoundError: No module named 'requests'`. What should she type instead?

<details>
<summary>Show answer</summary>

```powershell
uv run main.py
```

`uv run` notices that `.venv` is missing, rebuilds it from `pyproject.toml` and `uv.lock` (like `uv sync`), and then runs the program inside it.

</details>

### Write it

#### Exercise 6: A project from zero

Write the commands to: create a project `notes-app`, enter it, add `requests` as a library and `ruff` and `pytest` as developer tools, then check and format all the code.

<details>
<summary>Show answer</summary>

```powershell
uv init notes-app
cd notes-app
uv add requests
uv add --dev ruff pytest
uv run ruff check
uv run ruff format
```

You can add several libraries in one `uv add`.

</details>

#### Exercise 7: Format by hand, then check

Format this code the way `ruff format` would, by hand. Then run the real `ruff format` on it and compare.

<!-- no-verify -->
```python
def total(prices,tax):
    return sum(prices)*(1+tax)
basket=[2.5,4.0,1.25]
print(total(basket,0.1))
```

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
def total(prices, tax):
    return sum(prices) * (1 + tax)


basket = [2.5, 4.0, 1.25]
print(total(basket, 0.1))
```

Spaces after commas and around operators, and two blank lines after a function. The program itself does exactly the same thing.

</details>

## Review

#### Review 1: Exceptions (previous file)

What does this print?

```python
def parse_price(text):
    try:
        return float(text)
    except ValueError:
        return None


print(parse_price("4.50"))
print(parse_price("free"))
```

<details>
<summary>Show answer</summary>

```text
4.5
None
```

`"free"` cannot become a `float`, so `float` raises `ValueError`, and the `except` block returns `None`.

</details>

#### Review 2: Modules (this module)

A project has `prices.py` with a function `with_tax`. Write the line, in `main.py`, that imports only that function. Then write the command to run `main.py` in a uv project.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
from prices import with_tax
```

```powershell
uv run main.py
```

</details>

## Recap

- **uv** installs Python, creates the project (`uv init`), installs libraries (`uv add`, `uv add --dev`) and runs code (`uv run`). No need to activate anything.
- `pyproject.toml` lists what the project needs; `uv.lock` records the exact versions. Both go into Git. `.venv/` does not.
- After cloning a project, `uv sync` (or just `uv run`) rebuilds `.venv`.
- **ruff** checks code (`uv run ruff check`, `--fix`) and formats it (`uv run ruff format`). Install the Ruff extension and turn on format on save.
- Tutorials with pip translate directly: `pip install x` becomes `uv add x`, `python file.py` becomes `uv run file.py`.

**Next:** [Testing](testing.md)
