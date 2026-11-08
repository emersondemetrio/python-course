# Git basics

> **In one sentence:** Git is a program that saves snapshots of your project over time, so you can see what changed, when, and why, and go back to any earlier version.

## Why it matters

Without Git, people end up with folders like `notes.py`, `notes_v2.py`, `notes_final.py`, `notes_final_REALLY.py`. Nobody remembers which one works or what changed between them. With Git, there is only one `notes.py`, and a clean history of every version behind it. Almost every software company in the world uses Git, and GitHub (next file) is built on top of it.

## Analogy

Think of **save points in a video game**. You play, reach a safe spot, and save. If things go badly later, you load the save and try again. Each save has a name and a date.

A Git **commit** is a save point for your project. You decide when to make one, and you write a short message describing it, like "Add a menu to the notes program". Later you can list all your save points, compare two of them, or return to one.

There is one extra idea: before saving, you choose **which changes** go into the save point. Imagine packing a box before mailing it. You put items into the box (that is `git add`), check what is inside, and only then seal and label it (that is `git commit`).

## The idea, step by step

### Installing and checking Git

On **Windows**, download Git from [git-scm.com](https://git-scm.com) and install it with the default options. On **macOS**, run `git --version` in the terminal; if Git is missing, the system offers to install it. On **Linux**, use your package manager (for example `sudo apt install git`).

Check that it works:

```powershell
git --version
```

```text
git version 2.43.0
```

Your version number may be different. That is fine.

### Telling Git who you are (once per computer)

Every commit records who made it. Set your name and email once:

```powershell
git config --global user.name "Ana Souza"
git config --global user.email "ana@example.com"
git config --global init.defaultBranch main
```

- `--global` means "for every project on this computer".
- Use the **same email** as your GitHub account, so GitHub can link your commits to you.
- The last line makes new projects use the name `main` for the main line of history. It is the modern standard, and GitHub uses it too.

### Three places your files can be

Git thinks about your project in three areas. This is the most important idea in this file:

| Area | Box analogy | What it is |
|---|---|---|
| **Working folder** | Items scattered on the table | Your files as they are right now, as you edit them. |
| **Staging area** | Items placed in the open box | Changes you selected for the next commit, with `git add`. |
| **Repository (history)** | Sealed, labeled boxes on the shelf | All the commits saved so far, with `git commit`. |

The everyday cycle is: **edit** files, **add** the changes you want, **commit** them with a message. Repeat.

### `git init`: start tracking a folder

Go into your project folder and turn it into a Git repository:

```powershell
cd ~\Projects\notes
git init
```

```text
Initialized empty Git repository in C:/Users/you/Projects/notes/.git/
```

Git creates a hidden folder called `.git`. That is where the whole history lives. Never edit or delete it by hand: deleting `.git` deletes the history.

Run `git init` **once per project**, never inside a folder that is already a repository.

### `git status`: what is going on?

`git status` is the command you will run most often. It never changes anything, it only tells you the situation. When in doubt, run `git status`.

In a brand new repository with one file, `notes.py`:

```powershell
git status
```

```text
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	notes.py

nothing added to commit but untracked files present (use "git add" to track)
```

**Untracked** means Git sees the file but is not watching it yet. Notice that Git even tells you what to do next: `git add`.

### `git add`: put changes in the box

```powershell
git add notes.py
git status
```

```text
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   notes.py
```

Now `notes.py` is in the staging area: "Changes to be committed". To add **every** changed file at once, use a dot, which means "this folder":

```powershell
git add .
```

### `git commit`: seal the box with a label

```powershell
git commit -m "Add notes program"
```

```text
[main (root-commit) 7780a4a] Add notes program
 1 file changed, 1 insertion(+)
 create mode 100644 notes.py
```

`-m` means "message". The message goes between quotes. `7780a4a` is the commit's ID, a short code Git creates automatically. Yours will be different.

### Writing good commit messages

The message is for future you. In three months, "stuff" or "changes" will tell you nothing. Good messages describe **what** the commit does, in a few words, starting with a verb:

| Bad | Good |
|---|---|
| `update` | `Add a menu to the notes program` |
| `fix` | `Fix notes being erased on every run` |
| `asdf` | `Show the number of notes after the list` |
| `changes from today` | `Ignore empty notes` |

A good rule: the message should complete the sentence "If applied, this commit will...". "If applied, this commit will **add a menu to the notes program**."

Also, keep commits **small**: one idea per commit. It is much easier to understand (and undo) "Ignore empty notes" than a giant commit that changes ten things.

### `git log`: see the history

```powershell
git log
```

```text
commit 7780a4abc46d05932f6e2b22ccc7ee4c362bbe92
Author: Ana Souza <ana@example.com>
Date:   Sun Nov 8 15:24:33 2026 -0300

    Add notes program
```

Newest commits appear first. For a compact version, one line per commit:

```powershell
git log --oneline
```

```text
7780a4a Add notes program
```

If the log is long, Git shows it page by page. Press **Space** to go down and **q** to quit.

### `git diff`: what exactly changed?

Edit `notes.py` again, adding one line. Now `git status` says:

```text
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   notes.py

no changes added to commit (use "git add" and/or "git commit -a")
```

**Modified** means: Git knows this file, and it is different from the last commit. To see the difference line by line:

```powershell
git diff
```

```text
diff --git a/notes.py b/notes.py
index b80e322..e42aa4a 100644
--- a/notes.py
+++ b/notes.py
@@ -1 +1,2 @@
 print("hi")
+print("bye")
```

Lines starting with `+` were added. Lines starting with `-` were removed. Lines without a sign are unchanged context. Reading the diff before committing is a great habit: you check that you are saving only what you meant to.

### `.gitignore`: files Git should not track

Some files should never go into the history: data files that change all the time, passwords, or files that Python creates automatically. Create a text file called exactly `.gitignore` (starting with a dot, no extension) in the project folder, with one name or pattern per line:

```text
notes.txt
__pycache__/
.venv/
*.log
```

- `notes.txt`: your personal notes are data, not code.
- `__pycache__/`: a folder Python creates by itself to run faster.
- `.venv/`: a folder you will meet in module 07.
- `*.log`: the `*` means "anything", so every file ending in `.log`.

Then commit the `.gitignore` itself, so the rule is saved in the project:

```powershell
git add .gitignore
git commit -m "Ignore the notes data file"
```

### The everyday cycle, all together

```powershell
git status
git add .
git status
git commit -m "Describe what changed"
git log --oneline
```

Status, add, status, commit. Checking `status` before and after `add` helps you catch surprises.

## Common mistakes

### Running Git outside the project folder

```text
fatal: not a git repository (or any of the parent directories): .git
```

You are in a folder that is not a repository. Run `pwd` to see where you are, then `cd` into the project folder. If the project really has no repository yet, run `git init` there.

### Committing without adding

```powershell
git commit -m "Add menu"
```

```text
no changes added to commit (use "git add" and/or "git commit -a")
```

You edited files but did not put them in the box. **Fix:** `git add .` first, then commit.

### Forgetting `-m`

If you run `git commit` without `-m`, Git opens a text editor in the terminal and waits for a message. It can feel like the terminal froze. If it is the **Vim** editor (the screen is full of `~` signs): press `Esc`, type `:q!` and press Enter to leave without committing. Then commit again with `-m "message"`.

### Running `git init` in the wrong place

If you run `git init` in your home folder or in `Projects`, Git starts tracking **everything** inside it. `git status` will then list hundreds of files. **Fix:** delete the `.git` folder that was created in the wrong place (only that one), then run `git init` inside the actual project folder.

### Committing a file you meant to ignore

Adding a name to `.gitignore` does not remove a file that was **already committed**. **Fix:** tell Git to stop tracking it (the file stays on your computer):

```powershell
git rm --cached notes.txt
git commit -m "Stop tracking notes data file"
```

## Exercises

These exercises are about Git commands and their messages. Answer in writing, then try them in a practice folder (for example `Projects\git-practice`) to confirm.

### Predict the output

#### Exercise 1: Which area?

You created a new file `recipes.py` and did nothing else. Which word will `git status` use to describe it: **untracked**, **modified** or **new file**?

<details>
<summary>Show answer</summary>

**Untracked.** Git has never seen this file in a commit, and you have not added it. After `git add recipes.py` it becomes **new file** (in "Changes to be committed").

</details>

#### Exercise 2: Edited after committing

`notes.py` was committed yesterday. Today you changed one line. What does `git status` say about it, and is it ready to be committed?

<details>
<summary>Show answer</summary>

It says **modified: notes.py**, under "Changes not staged for commit". It is **not** ready: you must `git add notes.py` (or `git add .`) first.

</details>

#### Exercise 3: Reading a diff

What changed in this file?

```text
@@ -1,3 +1,3 @@
 print("Your notes:")
-print("1. buy milk")
+print("1. buy coffee")
 print("2. call the bank")
```

<details>
<summary>Show answer</summary>

One line was replaced: `print("1. buy milk")` was removed (`-`) and `print("1. buy coffee")` was added (`+`). The first and last lines did not change.

</details>

### Fix the bug

#### Exercise 4: The commit that will not happen

Someone ran these commands and got "no changes added to commit". What is missing?

```powershell
cd ~\Projects\notes
git commit -m "Show note count"
```

<details>
<summary>Show answer</summary>

The `git add` step. The changes were never put in the staging area:

```powershell
cd ~\Projects\notes
git add .
git commit -m "Show note count"
```

</details>

#### Exercise 5: Better messages

Rewrite these commit messages so that a person reading the history understands them.

1. `fix`
2. `more stuff`
3. `Changed the mode from w to a in save_note because notes were disappearing every time I ran the program`

<details>
<summary>Show answer</summary>

Possible answers:

1. `Fix crash when notes file does not exist`
2. `Add menu with add, show and exit options`
3. `Keep old notes when saving a new one`

The third one was too long. The details (mode `w` vs `a`) can be seen in the diff; the message should say **what** the change does, in a few words.

</details>

### Write it

#### Exercise 6: Your first repository

Write the full sequence of commands to: go to `Projects`, create a folder `git-practice`, enter it, start a repository, check the status, create a file `hello.py` (in the editor), add it, commit it with a good message, and see the history in one line per commit.

<details>
<summary>Show answer</summary>

```powershell
cd ~\Projects
mkdir git-practice
cd git-practice
git init
git status
# create hello.py in the editor and save it
git status
git add hello.py
git commit -m "Add hello program"
git log --oneline
```

</details>

#### Exercise 7: A .gitignore for the notes project

Write a `.gitignore` that ignores the notes data file `notes.txt`, the `__pycache__` folder, and every file ending in `.tmp`.

<details>
<summary>Show answer</summary>

```text
notes.txt
__pycache__/
*.tmp
```

</details>

#### Exercise 8: Three commits for three features

Take your `notes` project from module 04. Make it a repository and record its history in **three separate commits**: first the basic program, then "show the count", then "ignore empty notes". Use `git log --oneline` at the end. What should you see?

<details>
<summary>Show answer</summary>

Something like this (your IDs will be different), newest first:

```text
c3d9e21 Ignore empty notes
8a1f0b4 Show the number of notes
7780a4a Add notes program
```

The trick is to commit **after each feature**, not all at the end.

</details>

## Review

#### Review 1: files (module 04)

What does this print?

```python
with open("log.txt", "w", encoding="utf-8") as file:
    file.write("first\n")

with open("log.txt", "a", encoding="utf-8") as file:
    file.write("second\n")

with open("log.txt", "r", encoding="utf-8") as file:
    print(file.read().splitlines())
```

<details>
<summary>Show answer</summary>

Output:

```text
['first', 'second']
```

`"w"` created the file with one line, `"a"` added a second one, and `splitlines()` returned both as a list.

</details>

#### Review 2: loops (module 02)

Write a loop that prints each commit message from this list, numbered from 1.

<!-- no-verify -->
```python
messages = ["Add notes program", "Show the number of notes", "Ignore empty notes"]
```

<details>
<summary>Show answer</summary>

```python
messages = ["Add notes program", "Show the number of notes", "Ignore empty notes"]
for number, message in enumerate(messages, start=1):
    print(f"{number}. {message}")
```

Output:

```text
1. Add notes program
2. Show the number of notes
3. Ignore empty notes
```

</details>

## Recap

- A commit is a save point of your project, with a message, an author and a date.
- The cycle is: edit, `git add`, `git commit -m "message"`. Use `git status` before and after.
- Working folder, staging area, history: `add` moves changes into the box, `commit` seals it.
- `git log --oneline` shows the history; `git diff` shows what changed line by line.
- `.gitignore` lists files Git should never track, like data files and `__pycache__/`.

**Next:** [github.md](github.md)
