"""Teacher's guide for module 05: Git and GitHub.

Every command, Markdown snippet and exercise answer from this module's lessons,
ready to show in class. Git and Markdown items are shown only (as comments):
type them live in a practice folder. The few Python review items also run.

Usage (from this folder):
    uv run guide.py                      list sections and items
    uv run guide.py git_basics           show every item in a section
    uv run guide.py git_basics.ex06      show one item
    uv run guide.py all                  show everything
"""

import builtins
import contextlib
import inspect
import os
import sys
import tempfile
import textwrap

SECTIONS: dict[str, dict[str, tuple]] = {}


def item(section, name, note="", run=True):
    """Register a function as a guide item: `section.name`, with a teaching note.

    Use run=False for code that should only be shown (servers, network, API keys,
    third-party libraries): the guide prints it without executing it.
    """

    def register(fn):
        SECTIONS.setdefault(section, {})[name] = (fn, note, run)
        return fn

    return register


@contextlib.contextmanager
def typed(*answers):
    """Simulate a person typing `answers` into input(), echoing them like a terminal."""
    queue = list(answers)
    original = builtins.input

    def fake_input(prompt=""):
        value = queue.pop(0)
        print(f"{prompt}{value}")
        return value

    builtins.input = fake_input
    try:
        yield
    finally:
        builtins.input = original


@contextlib.contextmanager
def scratch_folder():
    """Run file examples inside a throwaway folder, so nothing is left behind."""
    previous = os.getcwd()
    with tempfile.TemporaryDirectory() as folder:
        os.chdir(folder)
        try:
            yield folder
        finally:
            os.chdir(previous)


def show(section, name):
    fn, note, run = SECTIONS[section][name]
    source = inspect.getsource(fn)
    body = source.split(":\n", 1)[1] if source.lstrip().startswith(("@", "def")) else source
    body = textwrap.dedent(body.split('"""', 2)[-1] if fn.__doc__ else body).strip("\n")
    title = fn.__doc__.strip() if fn.__doc__ else name
    print(f"\n=== {section}.{name}: {title}")
    if note:
        print(f"Teacher note: {note}")
    print("--- code")
    print(body)
    if not run:
        print("--- (shown only: run it in a project, see the lesson)")
        return
    print("--- output")
    try:
        fn()
    except Exception as error:  # noqa: BLE001 - broken-on-purpose examples show their error
        print(f"{type(error).__name__}: {error}")


def main(args):
    if not args:
        for section, items in SECTIONS.items():
            print(f"{section}: {', '.join(items)}")
        return
    target = args[0]
    if target == "all":
        for section, items in SECTIONS.items():
            for name in items:
                show(section, name)
        return
    section, _, name = target.partition(".")
    if section not in SECTIONS or (name and name not in SECTIONS[section]):
        print(f"Unknown item: {target}. Run without arguments to see the list.")
        sys.exit(1)
    for each in [name] if name else SECTIONS[section]:
        show(section, each)


# --------------------------------------------------------------------------
# git-basics.md
# Git items are terminal commands, shown as comments (run=False).
# Type them live in a practice folder, for example Projects\git-practice.


@item("git_basics", "install_check", "Her version number may differ. That is fine.", run=False)
def git_install_check():
    """Installing and checking Git"""
    # Windows: download from https://git-scm.com, install with default options
    # macOS:   run git --version, accept the install offer
    # Linux:   sudo apt install git
    #
    # > git --version
    # git version 2.43.0
    pass


@item("git_basics", "config", "Same email as her GitHub account. Run once per computer.", run=False)
def git_config():
    """Telling Git who you are (once per computer)"""
    # > git config --global user.name "Ana Souza"
    # > git config --global user.email "ana@example.com"
    # > git config --global init.defaultBranch main
    #
    # --global = for every project on this computer
    pass


@item("git_basics", "three_areas", "The most important idea. Draw the three boxes.", run=False)
def git_three_areas():
    """Three places your files can be"""
    # Working folder  -> items scattered on the table   (your files right now)
    # Staging area    -> items placed in the open box   (git add)
    # Repository      -> sealed, labeled boxes on shelf (git commit)
    #
    # Everyday cycle: edit -> git add -> git commit. Repeat.
    pass


@item("git_basics", "init", "Once per project. Never edit or delete the .git folder.", run=False)
def git_init():
    """git init: start tracking a folder"""
    # > cd ~\Projects\notes
    # > git init
    # Initialized empty Git repository in C:/Users/you/Projects/notes/.git/
    pass


@item("git_basics", "status_untracked", "Point out that Git tells you the next command.", run=False)
def git_status_untracked():
    """git status in a new repository: untracked"""
    # > git status
    # On branch main
    #
    # No commits yet
    #
    # Untracked files:
    #   (use "git add <file>..." to include in what will be committed)
    #         notes.py
    #
    # nothing added to commit but untracked files present (use "git add" to track)
    pass


@item("git_basics", "add", "Now it says new file, under Changes to be committed.", run=False)
def git_add():
    """git add: put changes in the box"""
    # > git add notes.py
    # > git status
    # On branch main
    #
    # No commits yet
    #
    # Changes to be committed:
    #   (use "git rm --cached <file>..." to unstage)
    #         new file:   notes.py
    #
    # Add every changed file at once (the dot means "this folder"):
    # > git add .
    pass


@item("git_basics", "commit", "-m means message. Her commit ID will be different.", run=False)
def git_commit():
    """git commit: seal the box with a label"""
    # > git commit -m "Add notes program"
    # [main (root-commit) 7780a4a] Add notes program
    #  1 file changed, 1 insertion(+)
    #  create mode 100644 notes.py
    pass


@item("git_basics", "messages", "Rule: complete 'If applied, this commit will...'", run=False)
def git_messages():
    """Writing good commit messages"""
    # Bad                  Good
    # update               Add a menu to the notes program
    # fix                  Fix notes being erased on every run
    # asdf                 Show the number of notes after the list
    # changes from today   Ignore empty notes
    #
    # Start with a verb. One idea per commit.
    pass


@item("git_basics", "log", "Space goes down, q quits the long log.", run=False)
def git_log():
    """git log: see the history"""
    # > git log
    # commit 7780a4abc46d05932f6e2b22ccc7ee4c362bbe92
    # Author: Ana Souza <ana@example.com>
    # Date:   Sun Nov 8 15:24:33 2026 -0300
    #
    #     Add notes program
    #
    # > git log --oneline
    # 7780a4a Add notes program
    pass


@item(
    "git_basics",
    "diff",
    "+ added, - removed, no sign is context. Read diffs before committing.",
    run=False,
)
def git_diff():
    """git diff: what exactly changed?"""
    # After editing notes.py again:
    # > git status
    # Changes not staged for commit:
    #         modified:   notes.py
    #
    # > git diff
    # diff --git a/notes.py b/notes.py
    # --- a/notes.py
    # +++ b/notes.py
    # @@ -1 +1,2 @@
    #  print("hi")
    # +print("bye")
    pass


@item(
    "git_basics", "gitignore", "Data, generated folders and secrets stay out of history.", run=False
)
def git_gitignore():
    """.gitignore: files Git should not track"""
    # File named exactly .gitignore in the project folder:
    #   notes.txt
    #   __pycache__/
    #   .venv/
    #   *.log
    #
    # > git add .gitignore
    # > git commit -m "Ignore the notes data file"
    pass


@item("git_basics", "cycle", "Status before and after add catches surprises.", run=False)
def git_cycle():
    """The everyday cycle, all together"""
    # > git status
    # > git add .
    # > git status
    # > git commit -m "Describe what changed"
    # > git log --oneline
    pass


@item("git_basics", "mistake_outside_repo", "Fix: pwd, then cd into the project.", run=False)
def git_mistake_outside_repo():
    """Common mistake: running Git outside the project folder"""
    # fatal: not a git repository (or any of the parent directories): .git
    pass


@item("git_basics", "mistake_commit_without_add", "Fix: git add . first.", run=False)
def git_mistake_commit_without_add():
    """Common mistake: committing without adding"""
    # > git commit -m "Add menu"
    # no changes added to commit (use "git add" and/or "git commit -a")
    pass


@item("git_basics", "mistake_no_m", "Show the Vim escape once so she is not scared.", run=False)
def git_mistake_no_m():
    """Common mistake: forgetting -m"""
    # > git commit
    # (an editor opens; if the screen is full of ~ signs, it is Vim)
    # Press Esc, type :q! and press Enter to leave without committing.
    # Then: git commit -m "message"
    pass


@item(
    "git_basics",
    "mistake_init_wrong_place",
    "Delete only the .git created in the wrong place.",
    run=False,
)
def git_mistake_init_wrong_place():
    """Common mistake: running git init in the wrong place"""
    # git init in your home folder or in Projects tracks EVERYTHING inside it.
    # git status then lists hundreds of files.
    # Fix: delete that one .git folder, then git init inside the real project.
    pass


@item(
    "git_basics",
    "mistake_already_committed",
    "The file stays on disk; Git stops tracking it.",
    run=False,
)
def git_mistake_already_committed():
    """Common mistake: committing a file you meant to ignore"""
    # .gitignore does not remove a file that was already committed.
    # > git rm --cached notes.txt
    # > git commit -m "Stop tracking notes data file"
    pass


@item("git_basics", "ex01", "Predict. Answer: untracked.", run=False)
def git_ex01():
    """Exercise 1: which area?"""
    # New file recipes.py, nothing else done.
    # Answer: untracked. After git add recipes.py it becomes "new file".
    pass


@item("git_basics", "ex02", "Predict. Answer: modified, and NOT ready.", run=False)
def git_ex02():
    """Exercise 2: edited after committing"""
    # Answer: "modified: notes.py" under "Changes not staged for commit".
    # Not ready: git add notes.py (or git add .) first.
    pass


@item("git_basics", "ex03", "Predict. One line replaced.", run=False)
def git_ex03():
    """Exercise 3: reading a diff"""
    # @@ -1,3 +1,3 @@
    #  print("Your notes:")
    # -print("1. buy milk")
    # +print("1. buy coffee")
    #  print("2. call the bank")
    #
    # Answer: "buy milk" was removed (-), "buy coffee" was added (+).
    # The first and last lines did not change.
    pass


@item("git_basics", "ex04", "Fix the bug. The missing step is git add.", run=False)
def git_ex04():
    """Exercise 4: the commit that will not happen"""
    # > cd ~\Projects\notes
    # > git add .
    # > git commit -m "Show note count"
    pass


@item(
    "git_basics",
    "ex05",
    "Fix the bug. Any message that says WHAT the change does is fine.",
    run=False,
)
def git_ex05():
    """Exercise 5: better messages"""
    # fix          -> Fix crash when notes file does not exist
    # more stuff   -> Add menu with add, show and exit options
    # (very long)  -> Keep old notes when saving a new one
    #
    # The details (w vs a) are in the diff; the message stays short.
    pass


@item("git_basics", "ex06", "Write it. Let her type it all in a real practice folder.", run=False)
def git_ex06():
    """Exercise 6: your first repository"""
    # > cd ~\Projects
    # > mkdir git-practice
    # > cd git-practice
    # > git init
    # > git status
    # (create hello.py in the editor and save it)
    # > git status
    # > git add hello.py
    # > git commit -m "Add hello program"
    # > git log --oneline
    pass


@item("git_basics", "ex07", "Write it. * means anything.", run=False)
def git_ex07():
    """Exercise 7: a .gitignore for the notes project"""
    # notes.txt
    # __pycache__/
    # *.tmp
    pass


@item("git_basics", "ex08", "Write it. Commit after EACH feature, not all at the end.", run=False)
def git_ex08():
    """Exercise 8: three commits for three features"""
    # > git log --oneline
    # c3d9e21 Ignore empty notes
    # 8a1f0b4 Show the number of notes
    # 7780a4a Add notes program
    #
    # (her IDs will be different; newest first)
    pass


@item("git_basics", "review01", "Review of module 04. Ask her to predict before running.")
def git_review01():
    """Review 1: files"""
    with scratch_folder():
        with open("log.txt", "w", encoding="utf-8") as file:
            file.write("first\n")

        with open("log.txt", "a", encoding="utf-8") as file:
            file.write("second\n")

        with open("log.txt", encoding="utf-8") as file:
            print(file.read().splitlines())


@item("git_basics", "review02", "Review of module 02. enumerate with start=1.")
def git_review02():
    """Review 2: loops"""
    messages = ["Add notes program", "Show the number of notes", "Ignore empty notes"]
    for number, message in enumerate(messages, start=1):
        print(f"{number}. {message}")


# --------------------------------------------------------------------------
# github.md


@item("github", "repo_vs_remote", "Git is the notebook system, GitHub is the library.", run=False)
def github_repo_vs_remote():
    """Repository vs remote"""
    # repository = project folder + its Git history
    # remote     = another copy of it, usually on GitHub, nicknamed "origin"
    # Git is a program on your computer; GitHub is a website.
    pass


@item("github", "create_repo", "Do it live on github.com. Leave README unchecked.", run=False)
def github_create_repo():
    """Creating a repository on GitHub"""
    # 1. Log in at github.com
    # 2. + (top right) > New repository
    # 3. Name without spaces: notes
    # 4. Public or Private
    # 5. Leave "Add a README file" UNCHECKED (the project already exists locally)
    # 6. Create repository
    #
    # Address: https://github.com/your-username/notes.git
    pass


@item("github", "remote_add", "Once per project. git remote -v checks it.", run=False)
def github_remote_add():
    """Connecting your local repo: git remote add"""
    # > cd ~\Projects\notes
    # > git remote add origin https://github.com/your-username/notes.git
    # > git remote -v
    # origin  https://github.com/your-username/notes.git (fetch)
    # origin  https://github.com/your-username/notes.git (push)
    pass


@item("github", "push", "Nothing goes online until you push. -u remembers the pairing.", run=False)
def github_push():
    """Sending your commits: git push"""
    # > git branch -M main
    # > git push -u origin main
    # (first time: a browser opens to log in to GitHub)
    #
    # From now on:
    # > git add .
    # > git commit -m "Describe what changed"
    # > git push
    pass


@item("github", "clone", "Use it when the project is NOT on this computer yet.", run=False)
def github_clone():
    """Getting a copy of a repository: git clone"""
    # > cd ~\Projects
    # > git clone https://github.com/your-username/notes.git
    # > cd notes
    pass


@item("github", "pull", "Habit: git pull before you start working.", run=False)
def github_pull():
    """Receiving new commits: git pull"""
    # > git pull
    pass


@item("github", "readme", "The README is the front page of the repository.", run=False)
def github_readme():
    """The README"""
    # README.md:
    #   # Notes
    #
    #   A small command line program to save and list quick notes.
    #
    #   ## How to run
    #
    #   python notes.py
    pass


@item(
    "github", "history_on_site", "Open her repo and click through commits and History.", run=False
)
def github_history_on_site():
    """Viewing history on the website"""
    # commits (clock icon) -> same as git log
    # click a commit       -> its diff, green added, red removed
    # file > History       -> only the commits that changed that file
    pass


@item("github", "visibility", "Never push passwords, keys or personal data.", run=False)
def github_visibility():
    """Public or private, and changing it later"""
    # Settings > bottom (Danger Zone) > Change visibility
    # Anything pushed stays in the history, even if deleted later.
    pass


@item(
    "github", "collaborators", "This is how she would get push access to a shared repo.", run=False
)
def github_collaborators():
    """Working with someone: collaborators"""
    # Repository > Settings > Collaborators > Add people > username
    # They accept the email invitation, then: git clone, commit, git push
    # You: git pull to get their work
    pass


@item("github", "mistake_push_before_commit", "No new commits = nothing to send.", run=False)
def github_mistake_push_before_commit():
    """Common mistake: pushing before committing"""
    # > git push
    # Everything up-to-date
    #
    # Fix: git add . > git commit -m "..." > git push
    pass


@item(
    "github", "mistake_remote_exists", "Ran remote add twice. Check with git remote -v.", run=False
)
def github_mistake_remote_exists():
    """Common mistake: the remote already exists"""
    # error: remote origin already exists.
    #
    # If the address is wrong:
    # > git remote set-url origin https://github.com/your-username/notes.git
    pass


@item("github", "mistake_rejected", "Someone (maybe her, on the website) pushed first.", run=False)
def github_mistake_rejected():
    """Common mistake: push rejected because GitHub has newer commits"""
    #  ! [rejected]        main -> main (fetch first)
    # error: failed to push some refs to 'https://github.com/your-username/notes.git'
    #
    # Fix: git pull, then git push
    pass


@item("github", "mistake_clone_inside", "Always cd ~\\Projects before cloning.", run=False)
def github_mistake_clone_inside():
    """Common mistake: cloning inside another repository"""
    # git clone inside an existing project = a repository inside a repository.
    # Fix: cd ~\Projects (a plain folder) first, then clone.
    pass


@item("github", "ex01", "Predict. Answer: no, commits are local until git push.", run=False)
def github_ex01():
    """Exercise 1: where are my changes?"""
    # Answer: NO. The commit exists only on her computer until git push.
    pass


@item("github", "ex02", "Predict. New computer = clone; already have it = pull.", run=False)
def github_ex02():
    """Exercise 2: clone or pull?"""
    # 1. New computer          -> git clone
    # 2. Collaborator pushed   -> git pull
    pass


@item("github", "ex03", "Fix the bug. The remote was never added.", run=False)
def github_ex03():
    """Exercise 3: the forgotten step"""
    # > cd ~\Projects\notes
    # > git remote add origin https://github.com/your-username/notes.git
    # > git push -u origin main
    pass


@item("github", "ex04", "Write it. Website steps first, then the terminal.", run=False)
def github_ex04():
    """Exercise 4: put the notes project online"""
    # Website: + > New repository > notes > Public > README unchecked > Create
    #
    # > cd ~\Projects\notes
    # > git remote add origin https://github.com/your-username/notes.git
    # > git branch -M main
    # > git push -u origin main
    #
    # Refresh the repository page to see the files.
    pass


@item("github", "ex05", "Write it. Then add, commit, push.", run=False)
def github_ex05():
    """Exercise 5: a README for the notes project"""
    # README.md:
    #   # Notes
    #
    #   A small program that saves quick notes in a text file and lists them.
    #
    #   ## How to run
    #
    #   python notes.py
    #
    # > git add README.md
    # > git commit -m "Add README"
    # > git push
    pass


@item("github", "ex06", "Write it. Mirror of how you would invite her.", run=False)
def github_ex06():
    """Exercise 6: invite a study partner"""
    # Repository > Settings > Collaborators > Add people > study-buddy > invite
    # The friend accepts by email, then:
    # > git clone https://github.com/your-username/notes.git
    pass


@item("github", "review01", "Review of git-basics. One untracked, one modified.", run=False)
def github_review01():
    """Review 1: Git status"""
    # menu.py  (new)            -> untracked
    # notes.py (edited, known)  -> modified
    # Neither is staged yet.
    pass


@item("github", "review02", "Review of module 03. The function RETURNS the string; print shows it.")
def github_review02():
    """Review 2: functions and return"""

    def repo_url(user, name):
        return f"https://github.com/{user}/{name}.git"

    print(repo_url("ana-souza", "notes"))


# --------------------------------------------------------------------------
# markdown.md
# Markdown items are shown as comments. Type them in practice.md with the
# preview open (Ctrl+Shift+V) next to it.


@item("markdown", "headings", "Space after #. One # title, then ## sections.", run=False)
def md_headings():
    """Headings"""
    #   # Main title
    #   ## Section
    #   ### Subsection
    pass


@item(
    "markdown",
    "paragraphs",
    "Consecutive lines join; an empty line starts a new paragraph.",
    run=False,
)
def md_paragraphs():
    """Paragraphs and line breaks"""
    #   This is the first paragraph.
    #   This line joins the first paragraph.
    #
    #   This is a second paragraph.
    pass


@item(
    "markdown",
    "emphasis",
    "Backticks for anything that is code, a command or a file name.",
    run=False,
)
def md_emphasis():
    """Emphasis"""
    #   *italic* or _italic_
    #   **bold**
    #   `code inside a sentence`
    #   ~~crossed out~~
    pass


@item(
    "markdown", "lists", "Indent with spaces for a sub-list. Task lists work on GitHub.", run=False
)
def md_lists():
    """Lists"""
    #   - milk
    #   - eggs
    #     - 6 for the cake
    #     - 6 for breakfast
    #   - bread
    #
    #   1. Open the terminal
    #   2. Go to the project folder
    #   3. Run the program
    #
    #   - [x] Install Python
    #   - [ ] Finish module 05
    pass


@item("markdown", "links_images", "An image is a link with ! in front.", run=False)
def md_links_images():
    """Links and images"""
    #   [Python website](https://www.python.org)
    #   [Next lesson](github.md)
    #   ![A ceramic bowl](images/bowl.png)
    pass


@item("markdown", "code_blocks", "Language name after the backticks gives colors.", run=False)
def md_code_blocks():
    """Code blocks"""
    #   ```python
    #   name = "Ana"
    #   print(f"Hello, {name}!")
    #   ```
    #
    #   ```powershell
    #   python notes.py
    #   ```
    pass


@item("markdown", "tables", "Columns do not need to line up in the text.", run=False)
def md_tables():
    """Tables"""
    #   | Command      | What it does              |
    #   |--------------|---------------------------|
    #   | `git status` | Shows the situation       |
    #   | `git add .`  | Puts changes in the box   |
    pass


@item("markdown", "details", "The empty lines inside are required on GitHub.", run=False)
def md_details():
    """Hidden sections with details"""
    #   <details>
    #   <summary>Show answer</summary>
    #
    #   The answer goes here. It can have **bold**, lists and code.
    #
    #   </details>
    pass


@item("markdown", "mistake_no_space", "Fix: # Notes", run=False)
def md_mistake_no_space():
    """Common mistake: no space after #"""
    #   #Notes      -> shows as plain text
    #   # Notes     -> a heading
    pass


@item("markdown", "mistake_list_glued", "Fix: an empty line before the list.", run=False)
def md_mistake_list_glued():
    """Common mistake: lists glued to a paragraph"""
    #   My shopping list:
    #   - milk
    #   - eggs
    pass


@item(
    "markdown",
    "mistake_unclosed_code",
    "Every opening ``` needs a closing ``` on its own line.",
    run=False,
)
def md_mistake_unclosed_code():
    """Common mistake: code block never closed"""
    # Forget the closing three backticks and EVERYTHING after becomes code.
    pass


@item("markdown", "mistake_details_glued", "Raw ** and backticks appear on GitHub.", run=False)
def md_mistake_details_glued():
    """Common mistake: details without empty lines"""
    #   <details><summary>Show answer</summary>**bold** here</details>
    #
    # Fix: empty line after </summary> and before </details>.
    pass


@item("markdown", "ex01", "Predict. Ask her to describe it before opening the preview.", run=False)
def md_ex01():
    """Exercise 1: what will it look like?"""
    #   ## Tasks
    #
    #   Buy **coffee** and `run notes.py`.
    #
    #   1. Wash
    #   2. Dry
    #
    # Answer: a section heading "Tasks"; a paragraph with "coffee" in bold and
    # "run notes.py" in code font; a numbered list with Wash and Dry.
    pass


@item(
    "markdown",
    "ex02",
    "Fix the bug. Three problems: space, empty lines, unclosed block.",
    run=False,
)
def md_ex02():
    """Exercise 2: three problems"""
    #   # My Recipes
    #
    #   Ingredients:
    #
    #   - flour
    #   - sugar
    #
    #   ```python
    #   print("bake")
    #   ```
    #
    # 1. Missing space after #
    # 2. Missing empty line before the list (and after the title)
    # 3. The code block was never closed
    pass


@item("markdown", "ex03", "Write it. Her content will differ; check the structure.", run=False)
def md_ex03():
    """Exercise 3: your module notes"""
    #   # My Python notes
    #
    #   ## Module 04: Files
    #
    #   - `with open(name, "a", encoding="utf-8") as file:` closes by itself
    #   - `"w"` erases, `"a"` adds to the end
    #   - `file.read().splitlines()` gives a list of lines
    #
    #   ```python
    #   with open("notes.txt", "a", encoding="utf-8") as file:
    #       file.write("buy coffee\n")
    #   ```
    #
    #   ## Module 05: Git and GitHub
    #
    #   - `git add .` then `git commit -m "message"`
    #   - `git push` sends commits to GitHub
    #   - `git status` when in doubt
    pass


@item("markdown", "ex04", "Write it. At least five commands.", run=False)
def md_ex04():
    """Exercise 4: a Git cheat sheet table"""
    #   | Command               | What it does                          |
    #   |-----------------------|---------------------------------------|
    #   | `git init`            | Starts a repository in this folder    |
    #   | `git status`          | Shows what changed and what is staged |
    #   | `git add .`           | Stages all changes                    |
    #   | `git commit -m "msg"` | Saves a commit with a message         |
    #   | `git log --oneline`   | Lists commits, one per line           |
    #   | `git push`            | Sends commits to GitHub               |
    pass


@item("markdown", "ex05", "Write it. Push it and click the answer on GitHub together.", run=False)
def md_ex05():
    """Exercise 5: a self-quiz with details"""
    #   **Question:** Which mode adds to a file without erasing it?
    #
    #   <details>
    #   <summary>Answer</summary>
    #
    #   Mode `"a"` (append).
    #
    #   </details>
    pass


@item("markdown", "review01", "Review of git-basics. Starts with a verb.", run=False)
def md_review01():
    """Review 1: commit messages"""
    # Add how to run section to README
    pass


@item("markdown", "review02", "Review of module 01. Ask her to predict before running.")
def md_review02():
    """Review 2: strings"""
    title = "notes"
    print("# " + title.upper())
    print(f"Total: {len(title)} letters")


if __name__ == "__main__":
    main(sys.argv[1:])
