# pip and virtual environments

> **In one sentence:** `pip` installs code written by other people (libraries), and a virtual environment is a private box for each project, so the libraries of one project never mix with another.

## Why it matters

Python comes with many useful modules (`json`, `random`, `math`), but the world has written much more: libraries to build websites, talk to databases, call AI models, draw charts. You will use several of them in the next modules: `pytest` for tests, `flask` for the web, and a library to talk to an AI model. To use them you need to install them, and to install them **safely** you need a virtual environment. Without one, sooner or later two projects will need different versions of the same library and one of them will break.

## Analogy

A **library** is like a ready-made ingredient you buy at the store instead of making from scratch, like puff pastry. **PyPI** (the Python Package Index, at [pypi.org](https://pypi.org)) is the store. **pip** is the person who goes to the store and brings the ingredient home.

A **virtual environment** is a separate pantry for each recipe you are working on. The cake project has its own pantry with its own flour; the bread project has another. If the cake needs a special flour, buying it does not change the bread's pantry. And if you mess up one pantry, you can throw it away and build a new one in a minute.

`requirements.txt` is the shopping list taped to the pantry door: it says exactly what this project needs, so anyone (including you, on another computer) can fill a new pantry with the same things.

## The idea, step by step

### Libraries, PyPI and pip

- A **library** (also called a **package**) is code someone else wrote and shared, so you can `import` it.
- **PyPI** is the public website where those libraries are published. It has hundreds of thousands of them.
- **pip** is the tool, installed together with Python, that downloads libraries from PyPI and installs them for you.

You can check that pip is there:

```console
PS C:\Users\you\Projects> python -m pip --version
pip 24.0 from C:\Python312\Lib\site-packages\pip (python 3.12)
```

### Always use `python -m pip`

You will see both `pip install something` and `python -m pip install something` on the internet. Prefer the second. Your computer may have more than one Python installed, and `pip` alone might belong to a different one. `python -m pip` means "the pip that belongs to **this** python", so the library goes exactly where your program will look for it.

### The problem without a virtual environment

If you just run `python -m pip install flask` right now, flask is installed **globally**: in the one shared place for your whole computer. That seems convenient, until:

- Project A needs version 2 of a library, and project B needs version 3. Only one can be installed globally.
- You install many things to try them, and a year later you have no idea which project needs what.
- At work, your computer may not even let you install globally.

The solution is one virtual environment per project.

### Creating a virtual environment

Inside your project folder, run:

```powershell
python -m venv .venv
```

This creates a folder called `.venv` inside your project. It contains a private copy of Python and a private place for libraries. `venv` is the module that does this, and `.venv` is the name of the folder. You can choose any name, but `.venv` is the convention: everyone uses it, so tools like Cursor recognize it automatically.

<!-- no-verify -->
```text
my-project/
├── .venv/        <- the private pantry (do not edit it by hand)
└── main.py
```

### Activating it

Creating is not enough: you must **activate** the environment in your terminal, so that `python` and `pip` point to the private copy.

On **Windows (PowerShell)**:

```powershell
.venv\Scripts\Activate.ps1
```

On **macOS or Linux**:

```bash
source .venv/bin/activate
```

When it works, the prompt changes. You will see `(.venv)` at the start of the line:

```console
PS C:\Users\you\Projects\my-project> .venv\Scripts\Activate.ps1
(.venv) PS C:\Users\you\Projects\my-project>
```

That `(.venv)` is your signal: "everything I install now goes into this project's pantry". To leave the environment, type `deactivate`.

Important: activation lasts only for **that terminal window**. If you close it and open a new one, activate again. Make it a habit: `cd` into the project, activate, then work.

### Installing a library

With the environment active:

```console
(.venv) PS C:\Users\you\Projects\my-project> python -m pip install requests
Collecting requests
...
Successfully installed certifi-2024.8.30 charset-normalizer-3.4.0 idna-3.10 requests-2.32.3 urllib3-2.2.3
```

You asked for one library and pip installed five. That is normal: `requests` needs other libraries to work (its **dependencies**), and pip brings them too.

Now `import requests` works in your programs, **but only while this environment is active**.

To see what is installed in the environment:

```console
(.venv) PS C:\Users\you\Projects\my-project> python -m pip list
Package            Version
------------------ ---------
certifi            2024.8.30
charset-normalizer 3.4.0
idna               3.10
pip                24.0
requests           2.32.3
urllib3            2.2.3
```

To remove one: `python -m pip uninstall requests`.

### `requirements.txt`: the shopping list

A project should say which libraries it needs. The convention is a text file called `requirements.txt`, one library per line. You can write it by hand:

<!-- no-verify -->
```text
requests
pytest
```

Or you can ask pip to write the exact list of everything installed, with versions, using `freeze`:

```console
(.venv) PS C:\Users\you\Projects\my-project> python -m pip freeze > requirements.txt
```

`>` means "instead of showing the result on the screen, write it into this file". The file will look like:

<!-- no-verify -->
```text
certifi==2024.8.30
charset-normalizer==3.4.0
idna==3.10
requests==2.32.3
urllib3==2.2.3
```

`==` pins the exact version, so everyone gets the same thing.

Now, on another computer (or after deleting `.venv`), anyone can rebuild the environment with:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

`-r` means "read the list from this file".

### `.venv` does not go into Git

The `.venv` folder is big, full of files that pip can recreate at any time, and specific to your computer. It should **never** be committed. `requirements.txt` **should** be committed: it is small and it is the recipe to rebuild everything.

Add this to your `.gitignore` file (module 05):

<!-- no-verify -->
```text
.venv/
__pycache__/
```

`__pycache__` is a folder Python creates to speed things up. It can always be recreated, so it does not go into Git either.

### The full routine for a new project

```powershell
mkdir my-project
cd my-project
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install pytest
python -m pip freeze > requirements.txt
```

Then create `.gitignore` with `.venv/` inside, and start coding. In Cursor, if it asks "Select interpreter", choose the one inside `.venv`.

### Using a library: a first taste

Once a library is installed, you use it like any module. For example, `requests` downloads web pages (you will learn it properly in module 10):

<!-- no-verify -->
```python
import requests

response = requests.get("https://example.com")
print(response.status_code)
```

```console
(.venv) PS C:\Users\you\Projects\my-project> python main.py
200
```

How do you learn a library you have never seen? Look it up on [pypi.org](https://pypi.org): each library page has a link to its documentation, which usually starts with a short "Quickstart" example. Start there.

## Common mistakes

### "running scripts is disabled on this system" (Windows)

```console
PS C:\Users\you\Projects\my-project> .venv\Scripts\Activate.ps1
.venv\Scripts\Activate.ps1 : File C:\Users\you\Projects\my-project\.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system.
```

This is the most common problem on Windows. For safety, PowerShell blocks scripts by default, and `Activate.ps1` is a script. You can allow scripts that you created yourself, only for your user, with:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Answer `Y` if it asks. `RemoteSigned` means "run scripts made on this computer; scripts downloaded from the internet must be signed". You only need to do this once. On a work computer, this may be blocked by the IT team; if so, ask them, or use the Command Prompt instead of PowerShell with `.venv\Scripts\activate.bat`.

### `ModuleNotFoundError` after installing

<!-- error -->
```python
import requests_library_that_is_not_installed
```

```text
Traceback (most recent call last):
ModuleNotFoundError: No module named 'requests_library_that_is_not_installed'
```

You installed the library, but Python says it does not exist. Almost always, one of these:

- **The environment is not active** in this terminal. Look for `(.venv)` at the start of the prompt. If it is not there, activate.
- **You installed with a different Python.** Use `python -m pip install ...` in the same terminal where you run `python main.py`.
- **Cursor is using another interpreter.** Check the Python version shown in the bottom bar of Cursor and select the one in `.venv`.

### Committing the `.venv` folder

You run `git status` and see thousands of new files inside `.venv`. Do not commit them. Add `.venv/` to `.gitignore` first. If you already committed it, remove it from Git (but not from your disk) with `git rm -r --cached .venv`, then commit.

### Forgetting to update `requirements.txt`

You installed a new library, your program works, you push it. Your friend clones it, runs `pip install -r requirements.txt`, and gets `ModuleNotFoundError`. The list was old. After installing something new, run `python -m pip freeze > requirements.txt` again and commit the change.

## Exercises

### Predict the output

#### Exercise 1: Which pip?

You have two terminals open. In terminal 1 the prompt starts with `(.venv)`. In terminal 2 it does not. In terminal 1 you run `python -m pip install pytest`. Then, in terminal 2, inside the same folder, you run `python -m pytest`. What happens?

<details>
<summary>Show answer</summary>

Terminal 2 says something like `No module named pytest`. pytest was installed inside `.venv`, but terminal 2 is not using the environment, so it uses the global Python, where pytest is not installed. Activate the environment in terminal 2 too.

</details>

#### Exercise 2: Read the requirements

What does this `requirements.txt` say, and what command installs it?

<!-- no-verify -->
```text
flask==3.0.3
pytest==8.3.3
```

<details>
<summary>Show answer</summary>

The project needs flask version 3.0.3 and pytest version 8.3.3, exactly. With the environment active, install both with:

```powershell
python -m pip install -r requirements.txt
```

</details>

### Fix the bug

#### Exercise 3: The forgotten step

Someone runs these commands in a brand new terminal and gets `ModuleNotFoundError: No module named 'pytest'` at the end. What is missing?

```powershell
cd my-project
python -m venv .venv
python -m pip install pytest
deactivate
.venv\Scripts\Activate.ps1
python -m pytest
```

<details>
<summary>Show answer</summary>

The environment was not activated **before** installing. pytest went to the global Python (or failed). Then the environment was activated, and inside it pytest does not exist. (`deactivate` also had nothing to deactivate.) The correct order:

```powershell
cd my-project
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install pytest
python -m pytest
```

</details>

### Write it

#### Exercise 4: Set up a project from zero

On your computer, in your `Projects` folder:

1. Create a folder `weather-app` and enter it.
2. Create a virtual environment called `.venv` and activate it.
3. Install `pytest`.
4. Save the list of libraries to `requirements.txt`.
5. Create a `.gitignore` that ignores `.venv/` and `__pycache__/`.
6. Run `python -m pip list` and check pytest is there.

Write down the commands you used.

<details>
<summary>Show answer</summary>

On Windows (PowerShell):

```powershell
cd ~\Projects
mkdir weather-app
cd weather-app
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install pytest
python -m pip freeze > requirements.txt
python -m pip list
```

For the `.gitignore`, create the file in Cursor with two lines:

<!-- no-verify -->
```text
.venv/
__pycache__/
```

On macOS or Linux, the only differences are `cd ~/Projects` and `source .venv/bin/activate`.

</details>

#### Exercise 5: Rebuild from the list

Delete the `.venv` folder of the previous exercise (you can do it in the Cursor sidebar). Now rebuild the environment using only `requirements.txt`. Why can we delete `.venv` without fear?

<details>
<summary>Show answer</summary>

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

We can delete it without fear because `.venv` has nothing we wrote: everything in it was downloaded by pip and can be downloaded again. The important part, the list of what the project needs, is in `requirements.txt`. That is also why `.venv` stays out of Git and `requirements.txt` goes in.

</details>

## Review

#### Review 1: Testing (previous file)

What are the two naming rules pytest uses to find tests?

<details>
<summary>Show answer</summary>

The file name starts with `test_` (like `test_prices.py`), and each test function name starts with `test_` (like `def test_discount_of_half():`).

</details>

#### Review 2: Modules (this module)

You want to practice with the `json` module, so you create a file called `json.py` with `import json` inside. What goes wrong, and how do you fix it?

<details>
<summary>Show answer</summary>

`import json` imports **your** file, because Python looks in your folder first. Your file does not have `dumps` or `loads`, so you get an `AttributeError`. Rename your file to something like `json_practice.py` (and delete the `__pycache__` folder if one appeared).

</details>

## Recap

- A library is shared code. PyPI is where libraries live. pip installs them. Always use `python -m pip`.
- One virtual environment per project: `python -m venv .venv`, then activate it (`.venv\Scripts\Activate.ps1` on Windows, `source .venv/bin/activate` on macOS/Linux). Look for `(.venv)` in the prompt.
- `python -m pip freeze > requirements.txt` saves the list; `python -m pip install -r requirements.txt` rebuilds it.
- `.venv/` goes in `.gitignore`; `requirements.txt` goes into Git.
- On Windows, if activation is blocked, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once.

**Next:** [Module 08: Objects](../mod-08-objects/README.md)
