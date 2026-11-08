# Milestone 2: A repository

## Goal

Put Atanor under Git and publish it on your GitHub account. From now on, every milestone ends with a commit.

## Requires

Module 5: `git init`, `status`, `add`, `commit`, `log`, `.gitignore`, Markdown and GitHub.

## What you will build

- A local Git repository inside your `atanor` folder.
- A `.gitignore` that keeps your personal data out of Git.
- A `README.md` that explains the app.
- A repository on GitHub with your first commit in it.

## Steps

### Step 1: Start the repository

Open the terminal in the `atanor` folder and start a Git repository. Then check its status.

<details>
<summary>Show answer</summary>

```powershell
cd ~\Projects\atanor
git init
git status
```

```console
Initialized empty Git repository in C:/Users/you/Projects/atanor/.git/
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        atanor.py
        pieces.txt
```

"Untracked" means Git sees the files but is not keeping their history yet.

If the branch is called `master` instead of `main`, run `git branch -M main` once.

</details>

### Step 2: Keep your data out of Git

`pieces.txt` is **your data**, not part of the program. Someone who downloads your app should start with an empty list, not with your pieces. Create a file called `.gitignore` (the name starts with a dot) and tell Git to ignore `pieces.txt`.

<details>
<summary>Show answer</summary>

Content of `.gitignore`:

```text
# My personal data
pieces.txt
pieces.json
*.db

# Python creates these automatically
__pycache__/
.venv/
```

Run `git status` again: `pieces.txt` disappeared from the list. The file is still on your computer, Git just pretends it does not exist.

We already listed `pieces.json`, `*.db`, `__pycache__/` and `.venv/` because they will appear in the next milestones.

</details>

### Step 3: Write the README

Create `README.md` with:

1. A title.
2. One sentence saying what the app does.
3. A "How to run" section with the command.
4. A "Status" section saying which milestone you are in.

<details>
<summary>Show answer</summary>

````markdown
# Atanor

A small program to catalog my ceramic pieces.

## How to run

```powershell
python atanor.py
```

## Status

Milestone 2 of 8: pieces are saved in a text file.
````

Open the Markdown preview in Cursor to see how it looks.

</details>

### Step 4: The first commit

Add the files and make the first commit.

<details>
<summary>Show answer</summary>

```powershell
git add atanor.py .gitignore README.md
git status
git commit -m "Save and list ceramic pieces in a text file"
git log --oneline
```

```console
a1b2c3d (HEAD -> main) Save and list ceramic pieces in a text file
```

Your hash (`a1b2c3d`) will be different. Every commit has its own.

</details>

### Step 5: Create the repository on GitHub

On github.com, click **New repository**:

- Name: `atanor`
- Public
- Do **not** add a README, `.gitignore` or license (you already have them).

GitHub then shows the commands to connect your folder to it.

<details>
<summary>Show answer</summary>

```powershell
git remote add origin https://github.com/YOUR-USER/atanor.git
git push -u origin main
```

- `remote add origin` tells your local repository where its online copy lives. `origin` is just the usual nickname.
- `push -u origin main` sends your commits. The `-u` remembers the destination, so next time `git push` alone is enough.

Refresh the page on GitHub: your files and the README are there.

</details>

### Step 6: The everyday cycle

Change something small (for example, the message `Saved!` to `Piece saved!`) and go through the full cycle.

<details>
<summary>Show answer</summary>

```powershell
git status
git diff
git add atanor.py
git commit -m "Make the save message clearer"
git push
```

`git diff` shows exactly what changed before you commit. Get used to reading it: it is your last chance to catch a mistake.

</details>

## Checkpoint

- `git log --oneline` shows at least two commits.
- Your GitHub page shows `atanor.py`, `.gitignore` and `README.md`.
- `pieces.txt` is **not** on GitHub.

## Commit

```powershell
git commit -m "Add README and .gitignore"
```

## Stretch goals

#### Stretch 1: A good commit message

Which of these messages is best, and why?

1. `changes`
2. `fixed stuff in atanor`
3. `Ask for the technique when saving a piece`

<details>
<summary>Show answer</summary>

Number 3. It says **what** the commit does, in a few words, starting with a verb. In six months, `git log` will be readable like a list of everything you did. "changes" says nothing.

</details>

#### Stretch 2: Look at the past

Use `git log` to find your first commit and `git show` to see what it contained.

<details>
<summary>Show answer</summary>

```powershell
git log --oneline
git show a1b2c3d
```

Replace `a1b2c3d` with the hash of your first commit. Press `q` to leave the viewer.

</details>

**Next:** [Milestone 3: JSON records](03-json-records.md)
