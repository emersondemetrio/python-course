# Habits that keep your work tidy

> **In one sentence:** software engineering is not only writing code, it is also the small habits (where files live, how they are named, how you take notes, how you keep history) that make your work easy to find, run and share.

## Why it matters

Most beginner frustration does not come from Python. It comes from "where did I save that file?", "why does the terminal not find my folder?", "what did I learn last week?". A few simple rules, decided once, make these problems disappear.

## Analogy

Think of a well-organized kitchen. Knives always go in the same drawer. Spices are labeled. You never have to stop and think "where do I put the pan?", because the answer was decided long ago.

That is the idea behind **convention over configuration**: instead of making a new decision every time, you follow an agreed rule. Fewer decisions means more energy for what matters, which is the cooking (or, here, the code).

## The idea, step by step

### One home for all your projects

Create **one** folder called `Projects` inside your home folder, and put every course file and every project inside it. Always.

```text
C:\Users\ana\Projects        (Windows)
/Users/ana/Projects          (macOS)
```

To create it from the terminal:

```powershell
PS C:\Users\ana> mkdir Projects
PS C:\Users\ana> cd Projects
PS C:\Users\ana\Projects>
```

`mkdir` means **make directory**. From now on, the first thing you do in every study session is `cd Projects`.

### Convention over configuration

You just used a convention: "projects live in `Projects`". There is no technical reason for this specific name. The value is in **always doing the same thing**, so you never have to decide or remember.

Programmers use conventions everywhere: Python files end in `.py`, the main documentation file of a project is called `README.md`, folders that hold tests are called `tests`. When everyone follows the same conventions, anyone can open a project and find their way around.

### Naming files and folders

Follow these rules for anything related to code:

- **No spaces.** Use `-` or `_` instead: `python-course`, `shopping_list.py`.
- **No accents or special characters:** no `ç`, `ã`, `é`, `!`, `?`, `&`. Write `notes`, not `anotações`.
- **Lowercase.** It avoids confusion, since some systems treat `Notes` and `notes` as different names.
- **Descriptive names.** `shopping_list.py` tells you what is inside. `test2_final_new.py` does not.

| Avoid | Prefer |
|---|---|
| `My Projects` | `projects` |
| `aula 1.py` | `class_01.py` |
| `anotações.md` | `notes.md` |
| `final FINAL v2.py` | `shopping_list.py` |

Why? Because the terminal treats spaces as separators (you saw this in [terminal.md](terminal.md)), and some tools still break on accents. Python files have one extra rule: their names must not start with a number, and must not have a `-`, if you ever want to import them from another file (module 07). So for `.py` files, use `_`: `shopping_list.py`.

### Organizing folders

Inside `Projects`, give each topic or project its own folder:

```text
Projects/
├── python-course/
│   ├── class-01/
│   │   └── hello.py
│   ├── class-02/
│   │   └── variables.py
│   └── notes/
│       ├── terminal.md
│       └── python.md
└── ceramics-studio/
```

A folder whose only job is to hold other files, like `class-01`, is sometimes called an **organizer folder**.

### Opening the editor from the terminal

Your editor can open a whole folder, so you see all its files in the sidebar. The fastest way is from the terminal:

```powershell
PS C:\Users\ana> cd Projects\python-course
PS C:\Users\ana\Projects\python-course> cursor .
```

Remember from [terminal.md](terminal.md): `.` means "this folder". So `cursor .` means "open Cursor here". With VS Code, the command is `code .`.

Useful shortcuts in the editor:

- **Ctrl + B** shows or hides the sidebar with the files.
- **Ctrl + S** saves the current file.
- **Ctrl + `** (the backtick key) opens the built-in terminal.

### Taking notes in Markdown

**Markdown** is a simple way to format text using plain characters. Files end in `.md`. This whole course is written in Markdown.

```markdown
# Big title

## Smaller title

### Even smaller title

Normal text. **Bold text.**

- A list item
- Another list item

Code inside a sentence: `print("hi")`
```

For a block of code, put three backticks before and after it, with the language name:

````markdown
```python
print("Hello")
```
````

In Cursor and VS Code, press **Ctrl + Shift + V** to open the **preview** and see the formatted result.

Taking notes after each study session, **in your own words**, is one of the best ways to remember what you learned. A `notes` folder with one file per topic works well.

### Git and GitHub, in two sentences

- **Git** is a tool that saves the history of your project, like a "save game" you can go back to at any moment.
- **GitHub** is a website where you store that history online, to keep it safe and share it with others.

You will learn both properly in [module 05](../module-05-git-and-github/). For now, it is enough to create an account at [github.com](https://github.com/).

## Common mistakes

### Saving files in random places

You save `hello.py` on the Desktop one day, in Downloads the next, and in Documents the week after. Then the terminal "cannot find" your files.

**Why:** there is no single place to look.

**Fix:** everything goes in `Projects`. If you already have files spread around, move them now.

### Spaces in names

```powershell
PS C:\Users\ana\Projects> python my program.py
python: can't open file 'C:\\Users\\ana\\Projects\\my': [Errno 2] No such file or directory
```

**Why:** the terminal split `my program.py` into two parts, and Python tried to open a file called `my`.

**Fix:** rename the file to `my_program.py`.

### Opening a single file instead of the folder

You double-click a `.py` file, the editor opens it, but the sidebar is empty and the built-in terminal starts in some other folder.

**Why:** the editor opened the **file**, not the **folder**.

**Fix:** open the folder with `cursor .` (or `code .`) from the terminal, or with **File → Open Folder**.

## Exercises

### Predict the output

#### Exercise 1: Good name or bad name?

For each name, say whether it follows the rules, and fix the ones that do not.

```text
shopping_list.py
Minhas Receitas
café.py
class-03
2nd try.py
```

<details>
<summary>Show answer</summary>

| Name | OK? | Better |
|---|---|---|
| `shopping_list.py` | Yes | |
| `Minhas Receitas` | No: space, capitals | `recipes` |
| `café.py` | No: accent | `coffee.py` |
| `class-03` | Yes (it is a folder) | |
| `2nd try.py` | No: space, starts with a number | `second_try.py` |

</details>

#### Exercise 2: What does `cursor .` open?

You are in `C:\Users\ana\Projects\python-course\class-02` and type `cursor .`. Which folder opens in the editor?

<details>
<summary>Show answer</summary>

```text
C:\Users\ana\Projects\python-course\class-02
```

The `.` always means "the folder I am in right now".

</details>

#### Exercise 3: Markdown preview

How will this look in the preview?

```markdown
# Groceries

- eggs
- **milk**
```

<details>
<summary>Show answer</summary>

A big title "Groceries", followed by a list with two items: "eggs" in normal text and "milk" in **bold**.

</details>

### Fix the bug

#### Exercise 4: The messy folder

Your `Projects` folder looks like this. Rename things so they follow the rules.

```text
Projects/
├── Aula 1/
│   └── Olá Mundo.py
└── anotações python.md
```

<details>
<summary>Show answer</summary>

```text
Projects/
├── class-01/
│   └── hello_world.py
└── notes/
    └── python.md
```

No spaces, no accents, lowercase, `_` in Python file names, and the notes got their own folder.

</details>

### Write it

#### Exercise 5: Set up your workbench

Using only the terminal:

1. Go to your home folder.
2. Create `Projects` (if it does not exist yet) and go into it.
3. Create a folder `python-course` and go into it.
4. Create a folder `notes`.
5. Open the editor in `python-course`.

<details>
<summary>Show answer</summary>

```powershell
cd ~
mkdir Projects
cd Projects
mkdir python-course
cd python-course
mkdir notes
cursor .
```

`~` is a shortcut for your home folder, and works in PowerShell too. If `mkdir Projects` says the folder already exists, that is fine, just continue.

</details>

#### Exercise 6: Your first notes file

Create `notes/terminal.md` with:

- a title `# Terminal`,
- a list of the commands you know, each with a short explanation in your own words,
- a code block showing how to run a Python file.

Open the preview to check it.

<details>
<summary>Show answer</summary>

````markdown
# Terminal

- `pwd`: shows the folder I am in
- `ls`: lists what is inside the folder
- `cd folder`: goes into a folder
- `cd ..`: goes up one folder

## Running Python

```powershell
python hello.py
```
````

Yours will be different, and it should be: the point is to write it in **your** words.

</details>

## Review

#### Review 1: Where does `cd ..` take you?

You are in `C:\Users\ana\Projects\python-course\notes`. What do you type to get back to `Projects`?

<details>
<summary>Show answer</summary>

```powershell
cd ..\..
```

One `..` takes you to `python-course`, the second one to `Projects`. Running `cd ..` twice works too.

</details>

#### Review 2: White dot

You changed your file, ran it, and the old version ran. What happened?

<details>
<summary>Show answer</summary>

You did not save. The white dot on the editor tab means unsaved changes. Press Ctrl + S and run again (see [python.md](python.md)).

</details>

## Recap

- All projects live in **one** `Projects` folder. That is **convention over configuration**: decide once, never think about it again.
- Names: **no spaces, no accents, lowercase**, descriptive. Use `_` in Python file names.
- Open the editor on a **folder** with `cursor .` or `code .`.
- Take notes in **Markdown** (`.md`): `#` for titles, `-` for lists, backticks for code. Preview with Ctrl + Shift + V.
- **Git** keeps the history of your project, **GitHub** keeps it online. Coming in module 05.

**Next:** [Module 01 · Building blocks](../module-01-building-blocks/)
