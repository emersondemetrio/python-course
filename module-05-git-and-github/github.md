# GitHub

> **In one sentence:** GitHub is a website that keeps a copy of your Git repository online, so it is backed up, visible to others, and easy to work on together.

## Why it matters

Your Git history lives in the `.git` folder on **your** computer. If the computer breaks, the history is gone. And nobody else can see or help with your code. GitHub solves both: it stores a copy online, shows your code and its history in the browser, and lets other people download it, suggest changes, or work with you. For a programmer, a GitHub profile is also a portfolio: it shows what you have built.

## Analogy

Think of a recipe notebook you keep at home (your **local repository**) and a shared copy kept in a library (the **remote repository** on GitHub). After you write new recipes at home, you take them to the library to update the shared copy (**push**). If a friend added recipes to the library copy, you bring them home (**pull**). Someone new can photocopy the whole library copy to start their own notebook (**clone**).

Git is the notebook system. GitHub is the library.

## The idea, step by step

### Repository vs remote

- A **repository** (or "repo") is a project folder with its Git history.
- A **remote** is another copy of that same repository, somewhere else, usually on GitHub. Your local repo knows the remote by a short nickname. By tradition, the main remote is called **`origin`**.

Git and GitHub are different things: Git is the program on your computer, GitHub is a company and website. You can use Git without GitHub, but not GitHub without Git.

### Creating a repository on GitHub

1. Log in at [github.com](https://github.com).
2. Click the **+** in the top right corner, then **New repository**.
3. Give it a name with no spaces, like `notes`.
4. Choose **Public** (anyone can see it) or **Private** (only you and people you invite).
5. If you already have a project on your computer, leave "Add a README file" **unchecked**, so the online repo starts empty.
6. Click **Create repository**.

GitHub then shows a page with commands. The address of your repository looks like this:

```text
https://github.com/your-username/notes.git
```

### Connecting your local repo: `git remote add`

In the terminal, inside your project folder (which already has commits from the previous file):

```powershell
cd ~\Projects\notes
git remote add origin https://github.com/your-username/notes.git
git remote -v
```

```text
origin  https://github.com/your-username/notes.git (fetch)
origin  https://github.com/your-username/notes.git (push)
```

`git remote add origin <address>` means "remember this address under the nickname `origin`". `git remote -v` lists the remotes, so you can check. You do this **once per project**.

### Sending your commits: `git push`

```powershell
git branch -M main
git push -u origin main
```

- `git branch -M main` makes sure your main line of history is called `main`. If it already is, nothing changes.
- `git push -u origin main` sends the commits of `main` to `origin`. The `-u` makes Git remember this pairing, so next time you can just type `git push`.

The first time, Git asks you to log in. On Windows, a browser window usually opens: log in to GitHub there and authorize. After that, Git remembers you.

Refresh the repository page on GitHub: your files are there.

From now on, the cycle becomes:

```powershell
git add .
git commit -m "Describe what changed"
git push
```

Commits are made on your computer. **Nothing goes online until you push.**

### Getting a copy of a repository: `git clone`

To download a repository from GitHub (yours, or someone else's public one) into a new folder:

```powershell
cd ~\Projects
git clone https://github.com/your-username/notes.git
cd notes
```

`clone` creates the folder, downloads all files **and** the whole history, and sets up `origin` automatically. Use it when the project is not on your computer yet, for example on a new computer.

### Receiving new commits: `git pull`

If the online copy has commits that you do not have (because someone else pushed, or you pushed from another computer, or you edited a file directly on the GitHub website), bring them to your computer:

```powershell
git pull
```

A good habit: run `git pull` before you start working, so you start from the newest version.

### The README

When you open a repository on GitHub, the file `README.md` is shown on the front page. It is the welcome sign of your project. A simple README answers:

- What is this project?
- How do I run it?

```text
# Notes

A small command line program to save and list quick notes.

## How to run

python notes.py
```

The `.md` means Markdown, a simple text format. You will learn it in the next file. Add the README, commit and push it like any other file.

### Viewing history on the website

On your repository page on GitHub:

- Click **commits** (near the top, with a clock icon) to see the list of commits, the same as `git log`.
- Click any commit to see its diff, with added lines in green and removed lines in red.
- Click any file, then **History**, to see only the commits that changed that file.

### Public or private, and changing it later

A **public** repository can be seen by anyone on the internet (only you and collaborators can change it). A **private** one is invisible to others. To change it later: open the repository, go to **Settings**, scroll to the bottom ("Danger Zone"), and use **Change visibility**.

Never put passwords, keys or personal data in a public repository. Anything pushed stays in the history, even if you delete the file later.

### Working with someone: collaborators

To let another person push to your repository:

1. Open the repository on GitHub and go to **Settings**.
2. Click **Collaborators** in the left menu.
3. Click **Add people** and type their GitHub username.
4. They receive an invitation by email and must accept it.

Then they `git clone` the repository, make commits, and `git push`. You `git pull` to get their work.

## Common mistakes

### Pushing before committing

```powershell
git push
```

```text
Everything up-to-date
```

You edited files but only pushed. Git says everything is up to date because **there are no new commits** to send. **Fix:** `git add .`, `git commit -m "..."`, then `git push`.

### The remote already exists

```text
error: remote origin already exists.
```

You ran `git remote add origin ...` twice. Check with `git remote -v`. If the address is wrong, fix it with:

```powershell
git remote set-url origin https://github.com/your-username/notes.git
```

### Push rejected because GitHub has newer commits

```text
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/your-username/notes.git'
```

The online copy has commits you do not have (maybe you edited the README on the website). **Fix:** `git pull` first, then `git push`.

### Cloning inside another repository

If you run `git clone` while inside an existing project folder, you end up with a repository inside a repository, which confuses Git. **Fix:** always `cd ~\Projects` (or another plain folder) before cloning.

## Exercises

### Predict the output

#### Exercise 1: Where are my changes?

You edited `notes.py`, ran `git add .` and `git commit -m "Add menu"`, then closed the computer. Is the change on GitHub?

<details>
<summary>Show answer</summary>

**No.** The commit exists only on your computer. It goes to GitHub only after `git push`.

</details>

#### Exercise 2: Clone or pull?

For each situation, which command do you use: `git clone` or `git pull`?

1. You bought a new computer and want your `notes` project on it.
2. You already have the project, but a collaborator pushed new commits yesterday.

<details>
<summary>Show answer</summary>

1. `git clone`: the project is not on this computer yet.
2. `git pull`: the project is there, you only need the new commits.

</details>

### Fix the bug

#### Exercise 3: The forgotten step

Someone created an empty repository on GitHub and ran this inside their project, which already has commits. The push fails because Git does not know where `origin` is. What is missing?

```powershell
cd ~\Projects\notes
git push -u origin main
```

<details>
<summary>Show answer</summary>

The remote was never added:

```powershell
cd ~\Projects\notes
git remote add origin https://github.com/your-username/notes.git
git push -u origin main
```

</details>

### Write it

#### Exercise 4: Put the notes project online

Your `notes` project already has commits (from the previous file). Write every step to put it on GitHub as a public repository, including what to click on the website.

<details>
<summary>Show answer</summary>

On the website: **+** > **New repository**, name `notes`, **Public**, leave "Add a README file" unchecked, **Create repository**.

In the terminal:

```powershell
cd ~\Projects\notes
git remote add origin https://github.com/your-username/notes.git
git branch -M main
git push -u origin main
```

Then refresh the repository page to see the files.

</details>

#### Exercise 5: A README for the notes project

Write a `README.md` for the notes project with a title, one sentence about what it does, and a "How to run" section. Commit it and push it. Which commands do you use after writing the file?

<details>
<summary>Show answer</summary>

A possible README:

```text
# Notes

A small program that saves quick notes in a text file and lists them.

## How to run

python notes.py
```

Then:

```powershell
git add README.md
git commit -m "Add README"
git push
```

</details>

#### Exercise 6: Invite a study partner

List the steps to let a friend with the GitHub username `study-buddy` push to your `notes` repository.

<details>
<summary>Show answer</summary>

Repository page > **Settings** > **Collaborators** > **Add people** > type `study-buddy` > send the invitation. Your friend accepts the invitation from their email, then runs `git clone https://github.com/your-username/notes.git`.

</details>

## Review

#### Review 1: Git status (git-basics.md)

You created `menu.py` and edited `notes.py`, which was already committed. You have not run `git add`. How does `git status` describe each file?

<details>
<summary>Show answer</summary>

`menu.py` is **untracked** (Git has never seen it). `notes.py` is **modified** (known, but different from the last commit). Neither is staged yet.

</details>

#### Review 2: functions and return (module 03)

What does this print?

```python
def repo_url(user, name):
    return f"https://github.com/{user}/{name}.git"


print(repo_url("ana-souza", "notes"))
```

<details>
<summary>Show answer</summary>

Output:

```text
https://github.com/ana-souza/notes.git
```

The function builds a string with an f-string and returns it; `print` shows it.

</details>

## Recap

- GitHub keeps an online copy (a **remote**, usually called `origin`) of your Git repository.
- Connect once with `git remote add origin <address>`, then `git push -u origin main`. After that, just `git push`.
- Commits are local until you push. `git pull` brings new commits from GitHub; `git clone` downloads a project for the first time.
- `README.md` is the front page of your repository: say what the project is and how to run it.
- Public repositories are visible to everyone: never push passwords or personal data.

**Next:** [markdown.md](markdown.md)
