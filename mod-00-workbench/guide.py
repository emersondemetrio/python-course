"""Teacher's guide for module 00: The workbench.

Every example and every exercise answer from this module's lessons, ready to
show in class. Each item prints its own code and then runs it.

Usage (from this folder):
    uv run guide.py                  list sections and items
    uv run guide.py python           run every item in a section
    uv run guide.py python.ex03      run one item
    uv run guide.py all              run everything
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
# Items: one section per lesson file, in reading order.


def run_source(code):
    """Run code that may not even parse (syntax errors), and show the error like Python."""
    try:
        exec(compile(code, "<example>", "exec"), {})
    except SyntaxError as error:
        print(f"SyntaxError: {error.msg}")


# ===== terminal.md (terminal commands: shown only, run them in a real terminal)


@item("terminal", "prompt", "Point at the path: it tells you where you are.", run=False)
def terminal_prompt():
    """The prompt"""
    # Windows (PowerShell):   PS C:\Users\ana>
    # macOS / Linux:          ana@laptop:~$


@item("terminal", "pwd_ls_cd", "Always: where am I (pwd), what is here (ls), then cd.", run=False)
def terminal_pwd_ls_cd():
    """pwd, ls and cd"""
    # PS C:\Users\ana> pwd
    # C:\Users\ana
    # PS C:\Users\ana> ls
    # Desktop   Documents   Projects
    # PS C:\Users\ana> cd Projects
    # PS C:\Users\ana\Projects>


@item("terminal", "cd_up", "Each .. goes up one level; . means 'right here'.", run=False)
def terminal_cd_up():
    """cd .. and cd ."""
    # PS C:\Users\ana\Projects> cd ..
    # PS C:\Users\ana>
    # PS C:\Users\ana> cd Projects\course
    # PS C:\Users\ana\Projects\course> cd ..\..
    # PS C:\Users\ana>
    # PS C:\Users\ana> cd .
    # PS C:\Users\ana>


@item("terminal", "tab_clear_history", "Let her press Tab herself: it prevents typos.", run=False)
def terminal_tab_clear_history():
    """Tab, clearing the screen, history"""
    # PS C:\Users\ana> cd Pr        <- press Tab
    # PS C:\Users\ana> cd .\Projects\
    # clear   (or Ctrl + L)  cleans the screen
    # history                lists the commands typed before


@item("terminal", "echo_cat", "echo is the terminal's print; cat shows a file.", run=False)
def terminal_echo_cat():
    """echo and cat"""
    # PS C:\Users\ana> echo "Hello"
    # Hello
    # PS C:\Users\ana\Projects> cat groceries.txt
    # eggs
    # milk
    # coffee


@item("terminal", "run_python", "Be in the file's folder, then python <file>.", run=False)
def terminal_run_python():
    """Running a Python file"""
    # PS C:\Users\ana\Projects> python hello.py
    # Hello, world!
    # macOS / Linux: python3 hello.py


@item("terminal", "path_error", "This is a PATH problem, not a problem in her file.", run=False)
def terminal_path_error():
    """PATH: python is not recognized"""
    # PS C:\Users\ana> python
    # python : The term 'python' is not recognized as the name of a cmdlet, ...


@item("terminal", "mistake_wrong_folder", "Ask: in which folder is the file?", run=False)
def terminal_mistake_wrong_folder():
    """Running a file from the wrong folder"""
    # PS C:\Users\ana> python hello.py
    # python: can't open file 'C:\\Users\\ana\\hello.py': [Errno 2] No such file or directory
    # Fix:
    # PS C:\Users\ana> cd Projects
    # PS C:\Users\ana\Projects> python hello.py
    # Hello, world!


@item("terminal", "mistake_typo", "Tab would have avoided this.", run=False)
def terminal_mistake_typo():
    """Typing the folder name wrong"""
    # PS C:\Users\ana> cd projetcs
    # cd : Cannot find path 'C:\Users\ana\projetcs' because it does not exist.


@item("terminal", "mistake_spaces", "Fix with quotes, or better, never use spaces.", run=False)
def terminal_mistake_spaces():
    """Folder names with spaces"""
    # PS C:\Users\ana> cd My Projects
    # Set-Location : A positional parameter cannot be found that accepts argument 'Projects'.
    # Fix: cd "My Projects"   (better: rename to my-projects)


@item(
    "terminal", "mistake_stuck_repl", "Leave the REPL with exit() or Ctrl+Z then Enter.", run=False
)
def terminal_mistake_stuck_repl():
    """Typing python alone and getting stuck"""
    # PS C:\Users\ana\Projects> python
    # Python 3.13.0 ...
    # >>>                 <- this is the REPL, not the terminal
    # >>> exit()


@item("terminal", "ex01", "Ask her to predict before running. Answer below.", run=False)
def terminal_ex01():
    """Exercise 1: Where am I?"""
    # Start: PS C:\Users\ana>
    # cd Projects / cd course / cd .. / pwd
    # Answer: C:\Users\ana\Projects


@item("terminal", "ex02", "Ask her to predict before running. Answer below.", run=False)
def terminal_ex02():
    """Exercise 2: Up, up, up"""
    # In C:\Users\ana\Projects\course\week1, run: cd ..\..
    # Answer: C:\Users\ana\Projects   (week1 -> course -> Projects)


@item("terminal", "ex03", "Ask her to predict before running. Answer below.", run=False)
def terminal_ex03():
    """Exercise 3: The dot"""
    # In C:\Users\ana\Projects, run: cd .  then pwd
    # Answer: C:\Users\ana\Projects   (. means "this folder")


@item("terminal", "ex04", "Python looks for the file in the current folder.", run=False)
def terminal_ex04():
    """Exercise 4: The file that does not exist"""
    # cd Projects
    # python hello.py


@item("terminal", "ex05", "Two answers: quotes, or rename without spaces.", run=False)
def terminal_ex05():
    """Exercise 5: Two words"""
    # 1. cd "python course"
    # 2. Better: rename the folder to python-course, then cd python-course


@item("terminal", "ex06", "Same commands on macOS and Linux.", run=False)
def terminal_ex06():
    """Exercise 6: A full trip"""
    # pwd
    # ls
    # cd Projects
    # cat notes.txt
    # cd ..


@item("terminal", "ex07", "Let her do it on her own computer without the page.", run=False)
def terminal_ex07():
    """Exercise 7: Practice on your own computer"""
    # pwd
    # cd Doc        <- press Tab, it becomes cd .\Documents\
    # cd ..
    # clear         (or Ctrl + L)
    # history


# ===== python.md


@item("python", "hello", "Her first file: save with Ctrl+S, then run from the terminal.")
def python_hello():
    """Your first file"""
    print("Hello, world!")


@item("python", "top_to_bottom", "Python runs one line at a time, from the top.")
def python_top_to_bottom():
    """Top to bottom, one line at a time"""
    print("First")
    print("Second")
    print("Third")


@item("python", "repl", "Show it live: the REPL shows results without print.", run=False)
def python_repl():
    """The interactive mode (REPL)"""
    # PS C:\Users\ana> python
    # >>> 2 + 3
    # 5
    # >>> print("Hi")
    # Hi
    # >>> exit()


@item("python", "syntax", "Quotes and parentheses must open and close.")
def python_syntax():
    """Syntax: the grammar of Python"""
    print("Coffee")
    print("Tea")


@item("python", "comments", "Python skips everything after #.")
def python_comments():
    """Comments: notes for humans"""
    # This program greets the user
    print("Good morning!")  # a comment can also go at the end of a line


@item("python", "read_error", "Read the error from the bottom up: type, message, line.")
def python_read_error():
    """Reading an error message"""
    pront("Hello")  # noqa: F821


@item("python", "mistake_quotes", "The message says 'unterminated': the string never ended.")
def python_mistake_quotes():
    """Forgetting to close the quotes"""
    run_source('print("Hello)')


@item("python", "mistake_parenthesis", "Count the ( and the ).")
def python_mistake_parenthesis():
    """Forgetting to close the parenthesis"""
    run_source('print("Hello"')


@item("python", "mistake_typo", "In a terminal Python also adds: Did you mean: 'print'?")
def python_mistake_typo():
    """A typo in a name"""
    pront("Hello")  # noqa: F821


@item("python", "mistake_capital", "Print and print are different names.")
def python_mistake_capital():
    """Capital letters"""
    Print("Hello")  # noqa: F821


@item("python", "ex01", "Ask her to predict before running.")
def python_ex01():
    """Exercise 1: Order matters"""
    print("Lunch")
    print("Breakfast")
    print("Dinner")


@item("python", "ex02", "Ask her to predict before running.")
def python_ex02():
    """Exercise 2: Comments"""
    # print("one")
    print("two")
    # print("three")
    print("four")


@item("python", "ex03", "Answer: file shop.py, line 4, change prnt to print.", run=False)
def python_ex03():
    """Exercise 3: Reading an error"""
    # NameError: name 'prnt' is not defined. Did you mean: 'print'?
    # File: shop.py
    # Line: 4
    # Fix: change prnt to print


@item("python", "ex04", "Three bugs: closing quote, capital P, closing parenthesis.")
def python_ex04():
    """Exercise 4: Three small problems (fixed)"""
    print("Apples")
    print("Bananas")
    print("Cherries")


@item("python", "ex05", "Her answer uses her own data. Check the comment at the top.")
def python_ex05():
    """Exercise 5: About me"""
    # Prints a short introduction about me
    print("My name is Ana")
    print("I live in Lisbon")
    print("I love pasta")


@item("python", "ex06", "The REPL shows results by itself; a file needs print.")
def python_ex06():
    """Exercise 6: REPL vs file"""
    # In the REPL:  >>> 7 * 6   shows 42
    # In a file:
    print(7 * 6)


@item("python", "review01", "Review of terminal.md.", run=False)
def python_review01():
    """Review 1: From the terminal"""
    # cd Projects
    # python hello.py


@item("python", "review02", "Not her file: the terminal cannot find Python (PATH).", run=False)
def python_review02():
    """Review 2: Not recognized"""
    # The term 'python' is not recognized -> the problem is the PATH.
    # The file was never even opened.


# ===== software-engineering.md (habits: shown only)


@item("software-engineering", "projects_folder", "One home for every project.", run=False)
def se_projects_folder():
    """One home for all your projects"""
    # PS C:\Users\ana> mkdir Projects
    # PS C:\Users\ana> cd Projects
    # PS C:\Users\ana\Projects>


@item("software-engineering", "open_editor", "The dot means 'this folder'.", run=False)
def se_open_editor():
    """Opening the editor from the terminal"""
    # PS C:\Users\ana> cd Projects\python-course
    # PS C:\Users\ana\Projects\python-course> cursor .


@item("software-engineering", "mistake_spaces", "The space split the name in two.", run=False)
def se_mistake_spaces():
    """Spaces in names"""
    # PS C:\Users\ana\Projects> python my program.py
    # python: can't open file 'C:\\Users\\ana\\Projects\\my': [Errno 2] No such file or directory
    # Fix: rename to my_program.py


@item("software-engineering", "ex01", "Ask her to judge each name before showing.", run=False)
def se_ex01():
    """Exercise 1: Good name or bad name?"""
    # shopping_list.py   OK
    # Minhas Receitas    no: space, capitals    -> recipes
    # café.py            no: accent             -> coffee.py
    # class-03           OK (a folder)
    # 2nd try.py         no: space, starts with a number -> second_try.py


@item("software-engineering", "ex02", "Ask her to predict.", run=False)
def se_ex02():
    """Exercise 2: What does cursor . open?"""
    # C:\Users\ana\Projects\python-course\class-02   (. = the folder I am in)


@item("software-engineering", "ex03", "Ask her to describe the preview.", run=False)
def se_ex03():
    """Exercise 3: Markdown preview"""
    # A big title "Groceries", then a list: "eggs" (normal) and "milk" (bold).


@item("software-engineering", "ex04", "No spaces, no accents, lowercase, notes folder.", run=False)
def se_ex04():
    """Exercise 4: The messy folder"""
    # Projects/
    #   class-01/
    #     hello_world.py
    #   notes/
    #     python.md


@item("software-engineering", "ex05", "If Projects already exists, just continue.", run=False)
def se_ex05():
    """Exercise 5: Set up your workbench"""
    # cd ~
    # mkdir Projects
    # cd Projects
    # mkdir python-course
    # cd python-course
    # mkdir notes
    # cursor .


@item("software-engineering", "ex06", "Her notes must be in her own words.", run=False)
def se_ex06():
    """Exercise 6: Your first notes file"""
    # # Terminal
    # - `pwd`: shows the folder I am in
    # - `ls`: lists what is inside the folder
    # - `cd folder`: goes into a folder
    # - `cd ..`: goes up one folder
    # ## Running Python
    # (a powershell code block with: python hello.py)


@item("software-engineering", "review01", "Running cd .. twice also works.", run=False)
def se_review01():
    """Review 1: Where does cd .. take you?"""
    # From C:\Users\ana\Projects\python-course\notes:
    # cd ..\..


@item("software-engineering", "review02", "The white dot on the tab means unsaved.", run=False)
def se_review02():
    """Review 2: White dot"""
    # She did not save. Ctrl + S, then run again.


if __name__ == "__main__":
    main(sys.argv[1:])
