# Modules

> **In one sentence:** a module is just a `.py` file, and `import` lets one file use the functions and variables written in another.

## Why it matters

Imagine a recipe book where every recipe, every tip and every shopping list is written on one endless page. You could find things, but it would hurt. As your programs grow, the same thing happens with code. Modules let you put related code in its own file with a clear name, and use it from anywhere. You have already used modules that come with Python, like `random`, `json` and `os`. In this lesson you will create your own.

## Analogy

Think of a kitchen. You do not keep the knives, the spices and the plates in one big box. You have a drawer for knives, a shelf for spices, a cupboard for plates. When you need cinnamon, you go to the spice shelf.

Each `.py` file is a drawer with a label. `import spices` means "I will use things from the spices drawer". And a **package** is a whole cupboard: a folder with several drawers inside.

## The idea, step by step

### Importing a module that comes with Python

You already know this. `import` makes the whole module available, and you use its things with a dot:

```python
import random
import math

print(math.sqrt(16))
print(math.pi > 3)
```

Output:

```text
4.0
True
```

`math.sqrt` reads as "the `sqrt` function that lives inside `math`". The module name works like a label, so you always know where something came from.

### Importing only what you need with `from`

If you only need one or two things, `from ... import ...` brings them in directly, without the module name in front:

```python
from math import sqrt, pi

print(sqrt(25))
print(round(pi, 2))
```

Output:

```text
5.0
3.14
```

Both ways work. `import math` keeps things clearly labeled (`math.sqrt`). `from math import sqrt` is shorter. When you are not sure, prefer `import math`: someone reading your code will always know where `sqrt` came from.

### Your own module

Here is the big idea: **any `.py` file you write is a module**. Create a folder with two files:

<!-- no-verify -->
```text
recipes/
├── conversions.py
└── main.py
```

In `conversions.py`, put some useful functions:

<!-- no-verify -->
```python
# conversions.py

GRAMS_PER_CUP = 120

def cups_to_grams(cups):
    return cups * GRAMS_PER_CUP

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
```

In `main.py`, import and use them:

<!-- no-verify -->
```python
# main.py
import conversions

flour = conversions.cups_to_grams(2)
oven = conversions.celsius_to_fahrenheit(180)

print(f"Flour: {flour} g")
print(f"Oven: {oven} F")
```

Run `main.py` from inside the `recipes` folder:

```console
PS C:\Users\you\Projects\recipes> python main.py
Flour: 240 g
Oven: 356.0 F
```

Notice:

- You write `import conversions`, **without** `.py`.
- Python looks for `conversions.py` in the **same folder** as the file you are running. That is why you run it from inside `recipes`.
- You can also write `from conversions import cups_to_grams`.

Now `main.py` is short and tells a story, and the details of each conversion live in their own drawer.

### `if __name__ == "__main__":`

There is a surprise waiting. Imagine you added a quick test at the bottom of `conversions.py`:

<!-- no-verify -->
```python
# conversions.py
def cups_to_grams(cups):
    return cups * 120

print("Testing:", cups_to_grams(1))
```

Now run `main.py` again:

```console
PS C:\Users\you\Projects\recipes> python main.py
Testing: 120
Flour: 240 g
```

The test line ran even though you ran `main.py`! When Python imports a file, it **runs the whole file** from top to bottom. Defining functions is harmless, but any `print` or other action at the top level runs too.

The fix is this famous line:

<!-- no-verify -->
```python
# conversions.py
def cups_to_grams(cups):
    return cups * 120

if __name__ == "__main__":
    print("Testing:", cups_to_grams(1))
```

Every file has a hidden variable called `__name__` (two underscores on each side). When you run a file directly (`python conversions.py`), Python sets its `__name__` to `"__main__"`. When the file is imported by another file, `__name__` is the file's name, `"conversions"`. So the `if` means: "run this only when this file is the one being run, not when it is imported".

You can see it yourself:

```python
print(__name__)
```

Output:

```text
__main__
```

A common habit is to put the "start" of a program inside a function called `main()`, and call it from this `if`:

<!-- no-verify -->
```python
# main.py
import conversions

def main():
    print(f"Flour: {conversions.cups_to_grams(2)} g")

if __name__ == "__main__":
    main()
```

### Packages: folders of modules

When you have many modules, group them in a folder. A folder of modules with a file called `__init__.py` inside is a **package**. The `__init__.py` file can be completely empty; its presence tells Python "this folder is a package".

<!-- no-verify -->
```text
kitchen/
├── main.py
└── tools/
    ├── __init__.py
    ├── conversions.py
    └── timers.py
```

From `main.py`, you import with a dot between the folder and the file:

<!-- no-verify -->
```python
# main.py
from tools import conversions
from tools.timers import minutes_to_seconds

print(conversions.cups_to_grams(2))
print(minutes_to_seconds(3))
```

Read `from tools.timers import minutes_to_seconds` as "from the `timers` drawer inside the `tools` cupboard, bring me `minutes_to_seconds`".

### Exploring a module with `dir()` and `help()`

When you meet a new module, you can ask it what it has:

```python
import math

names = [n for n in dir(math) if not n.startswith("_")]
print(names[:5])
```

Output:

```text
['acos', 'acosh', 'asin', 'asinh', 'atan']
```

`dir(math)` lists everything inside. `help(math.sqrt)` shows the documentation of one function. Try them in the interactive Python (type `python` in the terminal).

## Common mistakes

### Naming your file like a Python module

You create a file called `random.py` to practice with the `random` module:

<!-- no-verify -->
```python
# random.py  (your file)
import random
print(random.choice(["tea", "coffee"]))
```

```console
PS C:\Users\you\Projects> python random.py
AttributeError: module 'random' has no attribute 'choice' (consider renaming 'C:\Users\you\Projects\random.py' since it has the same name as the standard library module named 'random' and prevents importing that standard library module)
```

Python looks for modules in your folder **first**. So `import random` imported **your** `random.py`, which has no `choice`. Rename your file to something like `random_practice.py`, and delete any `__pycache__` folder that appeared next to it. The same goes for `json.py`, `math.py`, `os.py`, `test.py` and so on.

### Running from the wrong folder

```console
PS C:\Users\you\Projects> python main.py
C:\Python312\python.exe: can't open file 'C:\\Users\\you\\Projects\\main.py': [Errno 2] No such file or directory
```

The terminal is in `Projects`, but `main.py` lives in `Projects\recipes`. Python looked for `main.py` in the current folder and did not find it. Use `pwd` to see where you are and `ls` to see what is there, then `cd recipes` and run `python main.py` again.

If instead you see `ModuleNotFoundError: No module named 'conversions'`, check that `conversions.py` is spelled exactly right and is in the **same folder** as `main.py`.

### Writing `.py` in the import

<!-- error -->
```python
import json.py
```

```text
Traceback (most recent call last):
ModuleNotFoundError: No module named 'json.py'
```

The import uses the module name, not the file name. Write `import json` (or `import conversions`).

### Forgetting the module name

<!-- error -->
```python
import math
print(sqrt(9))
```

```text
Traceback (most recent call last):
NameError: name 'sqrt' is not defined
```

With `import math`, you must write `math.sqrt(9)`. To use `sqrt` alone, import it with `from math import sqrt`.

## Exercises

### Predict the output

#### Exercise 1: Two ways to import

<!-- no-verify -->
```python
import math
from math import floor

print(math.ceil(2.1))
print(floor(2.9))
```

<details>
<summary>Hint</summary>

`ceil` rounds up (to the ceiling), `floor` rounds down (to the floor).

</details>

<details>
<summary>Show answer</summary>

```python
import math
from math import floor

print(math.ceil(2.1))
print(floor(2.9))
```

Output:

```text
3
2
```

</details>

#### Exercise 2: What runs on import?

You have these two files in the same folder. What appears when you run `python app.py`?

<!-- no-verify -->
```python
# greetings.py
def hello(name):
    return f"Hello, {name}!"

print("greetings loaded")

if __name__ == "__main__":
    print(hello("tester"))
```

<!-- no-verify -->
```python
# app.py
import greetings

print(greetings.hello("Ana"))
```

<details>
<summary>Show answer</summary>

```console
PS C:\Users\you\Projects> python app.py
greetings loaded
Hello, Ana!
```

The `print("greetings loaded")` is at the top level, so it runs on import. The line inside `if __name__ == "__main__":` does not, because `greetings.py` was imported, not run directly. If you ran `python greetings.py`, you would see `greetings loaded` and `Hello, tester!`.

</details>

### Fix the bug

#### Exercise 3: Missing name

Fix this program in two different ways: once by changing the `import` line, once by changing the `print` line.

<!-- no-verify -->
```python
import random
print(choice(["red", "green", "blue"]))
```

<details>
<summary>Show answer</summary>

Way 1, change the import:

<!-- no-verify -->
```python
from random import choice
print(choice(["red", "green", "blue"]))
```

Way 2, change the print:

<!-- no-verify -->
```python
import random
print(random.choice(["red", "green", "blue"]))
```

</details>

### Write it

#### Exercise 4: Your first module

Create a folder `shop` with two files:

1. `prices.py` with a function `with_tax(price)` that returns the price plus 10%, and a function `format_price(price)` that returns a string like `"$ 11.00"` (use `f"$ {price:.2f}"`).
2. `main.py` that imports `prices`, calculates the price of an item that costs 10, and prints it formatted.

Run `main.py` from inside the `shop` folder.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# prices.py
def with_tax(price):
    return price * 1.10

def format_price(price):
    return f"$ {price:.2f}"
```

<!-- no-verify -->
```python
# main.py
import prices

final = prices.with_tax(10)
print(prices.format_price(final))
```

```console
PS C:\Users\you\Projects\shop> python main.py
$ 11.00
```

`:.2f` inside the braces means "show this number with 2 decimal places".

</details>

#### Exercise 5: Add a `main()`

Change `main.py` from the previous exercise so the code lives in a function `main()`, called from `if __name__ == "__main__":`. Then add a quick self-test at the bottom of `prices.py`, protected by the same `if`, so it only runs when you run `python prices.py`.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# prices.py
def with_tax(price):
    return price * 1.10

def format_price(price):
    return f"$ {price:.2f}"

if __name__ == "__main__":
    print(format_price(with_tax(100)))
```

<!-- no-verify -->
```python
# main.py
import prices

def main():
    final = prices.with_tax(10)
    print(prices.format_price(final))

if __name__ == "__main__":
    main()
```

`python main.py` prints `$ 11.00`. `python prices.py` prints `$ 110.00`.

</details>

## Review

#### Review 1: JSON (module 06)

Write the load-or-start-empty function `load_notes()` that returns the list saved in `notes.json`, or an empty list if the file does not exist yet.

<details>
<summary>Show answer</summary>

```python
import json
import os

def load_notes():
    if not os.path.exists("notes.json"):
        return []
    with open("notes.json", "r", encoding="utf-8") as file:
        return json.load(file)

print(load_notes())
```

Output:

```text
[]
```

This function is a great candidate for its own module, like `storage.py`.

</details>

#### Review 2: Comprehensions (module 06)

Rewrite as a list comprehension:

<!-- no-verify -->
```python
files = ["main.py", "notes.txt", "prices.py", "photo.jpg"]
python_files = []
for f in files:
    if f.endswith(".py"):
        python_files.append(f)
print(python_files)
```

<details>
<summary>Show answer</summary>

```python
files = ["main.py", "notes.txt", "prices.py", "photo.jpg"]
python_files = [f for f in files if f.endswith(".py")]
print(python_files)
```

Output:

```text
['main.py', 'prices.py']
```

</details>

## Recap

- A module is a `.py` file. `import name` (no `.py`) uses it as `name.thing`; `from name import thing` uses it as `thing`.
- Python looks for your modules in the folder of the file you run. Run from inside the project folder.
- Importing runs the whole file. Put "run only when executed directly" code under `if __name__ == "__main__":`.
- A package is a folder with an `__init__.py`. Import with dots: `from tools.timers import minutes_to_seconds`.
- Never name your files like Python modules (`random.py`, `json.py`, `test.py`).

**Next:** [Exceptions](exceptions.md)
