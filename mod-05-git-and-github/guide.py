# Teacher's guide: Module 05, Git and GitHub
# Every example and exercise answer from this module's lessons, in order.
# Run it from this folder:  python guide.py
#
# This module is about terminal commands and Markdown, not Python. The commands
# are written as comments: read them here, type them in the terminal with her.
# Only the Python review exercises actually run.

import os

print("=" * 50)
print("LESSON: git-basics.md")

print("\n--- Example: installing and checking Git")
# git --version
#   git version 2.43.0   (any version is fine)

print("\n--- Example: telling Git who you are (once per computer)")
# git config --global user.name "Ana Souza"
# git config --global user.email "ana@example.com"
# git config --global init.defaultBranch main
# Use the SAME email as her GitHub account.

print("\n--- Example: three places your files can be")
# Working folder  = items scattered on the table (files as they are now)
# Staging area    = items in the open box (git add)
# Repository      = sealed, labeled boxes on the shelf (git commit)
# The cycle: edit, add, commit. Repeat.

print("\n--- Example: git init")
# cd ~\Projects\notes
# git init
#   Initialized empty Git repository in C:/Users/you/Projects/notes/.git/
# Once per project. Never delete the .git folder by hand.

print("\n--- Example: git status")
# git status
#   On branch main
#   No commits yet
#   Untracked files:
#       notes.py
# "When in doubt, git status." It never changes anything.

print("\n--- Example: git add")
# git add notes.py
# git status
#   Changes to be committed:
#       new file:   notes.py
# git add .     -> adds every changed file in this folder

print("\n--- Example: git commit")
# git commit -m "Add notes program"
#   [main (root-commit) 7780a4a] Add notes program
#    1 file changed, 1 insertion(+)

print("\n--- Example: good commit messages")
# Bad: update / fix / asdf / changes from today
# Good: Add a menu to the notes program / Fix notes being erased on every run
# Rule: "If applied, this commit will ... <message>". One idea per commit.

print("\n--- Example: git log")
# git log
# git log --oneline
#   7780a4a Add notes program
# Space to scroll, q to quit.

print("\n--- Example: git diff")
# (edit notes.py, adding one line)
# git status     -> modified:   notes.py
# git diff
#    print("hi")
#   +print("bye")
# + added, - removed, no sign = unchanged.

print("\n--- Example: .gitignore")
# Contents of the file .gitignore:
#   notes.txt
#   __pycache__/
#   .venv/
#   *.log
# git add .gitignore
# git commit -m "Ignore the notes data file"

print("\n--- Example: the everyday cycle")
# git status
# git add .
# git status
# git commit -m "Describe what changed"
# git log --oneline

print("\n--- Mistake: running Git outside the project folder")
#   fatal: not a git repository (or any of the parent directories): .git
# Fix: pwd, then cd into the project. Or git init if it has no repository yet.

print("\n--- Mistake: committing without adding")
# git commit -m "Add menu"
#   no changes added to commit (use "git add" and/or "git commit -a")
# Fix: git add . first.

print("\n--- Mistake: forgetting -m")
# Git opens Vim (screen full of ~). Esc, type :q! and Enter. Then commit with -m.

print("\n--- Mistake: git init in the wrong place")
# git status lists hundreds of files. Delete only that wrong .git folder,
# then git init inside the real project folder.

print("\n--- Mistake: committing a file you meant to ignore")
# git rm --cached notes.txt
# git commit -m "Stop tracking notes data file"

print("\n--- Exercise 1: which area?")
# A new file recipes.py, nothing else done: UNTRACKED.
# After git add recipes.py it becomes "new file".

print("\n--- Exercise 2: edited after committing")
# "modified: notes.py", under "Changes not staged for commit".
# Not ready: git add notes.py (or git add .) first.

print("\n--- Exercise 3: reading a diff")
#  print("Your notes:")
# -print("1. buy milk")
# +print("1. buy coffee")
#  print("2. call the bank")
# One line replaced: "buy milk" removed, "buy coffee" added.

print("\n--- Exercise 4: the commit that will not happen")
# Missing step: git add.
# cd ~\Projects\notes
# git add .
# git commit -m "Show note count"

print("\n--- Exercise 5: better messages")
# 1. fix         -> Fix crash when notes file does not exist
# 2. more stuff  -> Add menu with add, show and exit options
# 3. (too long)  -> Keep old notes when saving a new one

print("\n--- Exercise 6: your first repository")
# cd ~\Projects
# mkdir git-practice
# cd git-practice
# git init
# git status
# (create hello.py in the editor and save it)
# git status
# git add hello.py
# git commit -m "Add hello program"
# git log --oneline

print("\n--- Exercise 7: a .gitignore for the notes project")
#   notes.txt
#   __pycache__/
#   *.tmp

print("\n--- Exercise 8: three commits for three features")
# git log --oneline, newest first (IDs will differ):
#   c3d9e21 Ignore empty notes
#   8a1f0b4 Show the number of notes
#   7780a4a Add notes program
# Commit AFTER EACH feature, not all at the end.

print("\n--- Review 1: files (module 04)")
# Ask her to predict before running.
with open("log.txt", "w", encoding="utf-8") as file:
    file.write("first\n")

with open("log.txt", "a", encoding="utf-8") as file:
    file.write("second\n")

with open("log.txt", "r", encoding="utf-8") as file:  # noqa: UP015
    print(file.read().splitlines())

os.remove("log.txt")

print("\n--- Review 2: loops (module 02)")
messages = ["Add notes program", "Show the number of notes", "Ignore empty notes"]
for number, message in enumerate(messages, start=1):
    print(f"{number}. {message}")


print()
print("=" * 50)
print("LESSON: github.md")

print("\n--- Example: repository vs remote")
# Repository = project folder with its Git history.
# Remote = another copy of it, usually on GitHub. Main remote nickname: origin.
# Git is the program on the computer. GitHub is the website.

print("\n--- Example: creating a repository on GitHub (website)")
# + (top right) > New repository > name "notes" > Public or Private
# > leave "Add a README file" UNCHECKED > Create repository
# Address: https://github.com/your-username/notes.git

print("\n--- Example: git remote add")
# cd ~\Projects\notes
# git remote add origin https://github.com/your-username/notes.git
# git remote -v
#   origin  https://github.com/your-username/notes.git (fetch)
#   origin  https://github.com/your-username/notes.git (push)

print("\n--- Example: git push")
# git branch -M main
# git push -u origin main
# First time: a browser window opens to log in to GitHub.
# After that, the cycle is:
# git add .
# git commit -m "Describe what changed"
# git push
# Nothing goes online until you push.

print("\n--- Example: git clone")
# cd ~\Projects
# git clone https://github.com/your-username/notes.git
# cd notes

print("\n--- Example: git pull")
# git pull      -> run it before you start working

print("\n--- Example: the README")
# # Notes
#
# A small command line program to save and list quick notes.
#
# ## How to run
#
# python notes.py

print("\n--- Example: viewing history on the website")
# commits (clock icon) = git log. Click a commit to see its diff (green/red).
# Click a file > History = only the commits that changed it.

print("\n--- Example: public or private")
# Settings > Danger Zone > Change visibility.
# Never push passwords, keys or personal data to a public repository.

print("\n--- Example: collaborators")
# Settings > Collaborators > Add people > username > they accept by email.

print("\n--- Mistake: pushing before committing")
# git push
#   Everything up-to-date
# Fix: git add ., git commit -m "...", then git push.

print("\n--- Mistake: the remote already exists")
#   error: remote origin already exists.
# git remote -v
# git remote set-url origin https://github.com/your-username/notes.git

print("\n--- Mistake: push rejected, GitHub has newer commits")
#   ! [rejected]        main -> main (fetch first)
# Fix: git pull, then git push.

print("\n--- Mistake: cloning inside another repository")
# Always cd ~\Projects (a plain folder) before git clone.

print("\n--- Exercise 1: where are my changes?")
# No. The commit is only on her computer until git push.

print("\n--- Exercise 2: clone or pull?")
# 1. New computer: git clone.
# 2. Project already there, collaborator pushed: git pull.

print("\n--- Exercise 3: the forgotten step")
# cd ~\Projects\notes
# git remote add origin https://github.com/your-username/notes.git
# git push -u origin main

print("\n--- Exercise 4: put the notes project online")
# Website: + > New repository > notes > Public > no README > Create repository
# cd ~\Projects\notes
# git remote add origin https://github.com/your-username/notes.git
# git branch -M main
# git push -u origin main

print("\n--- Exercise 5: a README for the notes project")
# README.md:
#   # Notes
#
#   A small program that saves quick notes in a text file and lists them.
#
#   ## How to run
#
#   python notes.py
# git add README.md
# git commit -m "Add README"
# git push

print("\n--- Exercise 6: invite a study partner")
# Settings > Collaborators > Add people > study-buddy > send invitation.
# The friend accepts by email, then:
# git clone https://github.com/your-username/notes.git

print("\n--- Review 1: git status")
# menu.py (new): untracked. notes.py (edited): modified. Neither is staged.

print("\n--- Review 2: functions and return (module 03)")
# Ask her to predict before running.


def repo_url(user, name):
    return f"https://github.com/{user}/{name}.git"


print(repo_url("ana-souza", "notes"))


print()
print("=" * 50)
print("LESSON: markdown.md")
# Open a practice.md and press Ctrl+Shift+V for the preview, side by side.

print("\n--- Example: headings")
# # Main title
# ## Section
# ### Subsection
# Always a space after the #.

print("\n--- Example: paragraphs")
# Consecutive lines = one paragraph. An EMPTY line starts a new one.

print("\n--- Example: emphasis")
# *italic*   **bold**   `code`   ~~crossed out~~

print("\n--- Example: lists")
# - milk
# - eggs
#   - 6 for the cake
# 1. Open the terminal
# 2. Go to the project folder
# - [x] Install Python
# - [ ] Finish module 05

print("\n--- Example: links and images")
# [Python website](https://www.python.org)
# [Next lesson](github.md)
# ![A ceramic bowl](images/bowl.png)

print("\n--- Example: code blocks")
# ```python
# name = "Ana"
# print(f"Hello, {name}!")
# ```

print("\n--- Example: tables")
# | Command      | What it does            |
# |--------------|-------------------------|
# | `git status` | Shows the situation     |
# | `git add .`  | Puts changes in the box |

print("\n--- Example: hidden sections with <details>")
# <details>
# <summary>Show answer</summary>
#
# The answer goes here.
#
# </details>
# Empty line after </summary> and before </details>, or GitHub shows raw symbols.

print("\n--- Mistakes")
# #Notes                -> no space after #: plain text. Fix: # Notes
# list glued to a paragraph -> leave an empty line before the list
# code block never closed   -> everything after it becomes code
# <details> without empty lines -> raw ** and backticks on GitHub

print("\n--- Exercise 1: what will it look like?")
# A "Tasks" heading, a paragraph with "coffee" in bold and "run notes.py" in code font,
# then a numbered list: Wash, Dry.

print("\n--- Exercise 2: three problems")
# # My Recipes          <- 1. space after #
#
# Ingredients:
#                       <- 2. empty line before the list (and after the title)
# - flour
# - sugar
#
# ```python
# print("bake")
# ```                   <- 3. the code block is closed

print("\n--- Exercise 3: your module notes")
# # My Python notes
#
# ## Module 04: Files
#
# - with open(name, "a", encoding="utf-8") as file: opens and closes by itself
# - "w" erases, "a" adds to the end
# - file.read().splitlines() gives a list of lines
#
# ## Module 05: Git and GitHub
#
# - git add . then git commit -m "message"
# - git push sends commits to GitHub
# - git status when in doubt

print("\n--- Exercise 4: a Git cheat sheet table")
# | Command               | What it does                          |
# |-----------------------|---------------------------------------|
# | `git init`            | Starts a repository in this folder    |
# | `git status`          | Shows what changed and what is staged |
# | `git add .`           | Stages all changes                    |
# | `git commit -m "msg"` | Saves a commit with a message         |
# | `git log --oneline`   | Lists commits, one per line           |
# | `git push`            | Sends commits to GitHub               |

print("\n--- Exercise 5: a self-quiz with <details>")
# **Question:** Which mode adds to a file without erasing it?
#
# <details>
# <summary>Answer</summary>
#
# Mode "a" (append).
#
# </details>

print("\n--- Review 1: commit messages")
# Add how to run section to README

print("\n--- Review 2: strings (module 01)")
# Ask her to predict before running.
title = "notes"
print("# " + title.upper())
print(f"Total: {len(title)} letters")
