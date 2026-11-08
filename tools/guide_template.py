"""Teacher's guide for module NN: <module title>.

Every example and every exercise answer from this module's lessons, ready to
show in class. Each item prints its own code and then runs it.

Usage (from this folder):
    uv run guide.py                  list sections and items
    uv run guide.py strings          run every item in a section
    uv run guide.py strings.ex03     run one item
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
# Items: one section per lesson file, in reading order. Example:


@item("strings", "concat_error", "Ask her to predict the error before running.")
def concat_error():
    """Joining text and a number with + fails"""
    age = 39
    print("Age: " + age)


@item("strings", "ex01", "Answer to Exercise 1.")
def strings_ex01():
    """Exercise 1: greeting with an f-string"""
    name = "Ana"
    print(f"Hello, {name}!")


@item("files", "write_and_read", "Runs in a temporary folder.")
def write_and_read():
    """Write a file, then read it back"""
    with scratch_folder():
        with open("notes.txt", "w", encoding="utf-8") as file:
            file.write("Buy coffee\n")
        with open("notes.txt", encoding="utf-8") as file:
            print(file.read())


@item("input", "ask_name", "input() is simulated: the typed text is shown.")
def ask_name():
    """Ask for a name"""
    with typed("Ana"):
        name = input("What is your name? ")
        print(f"Hello, {name}!")


@item("web", "flask_hello", "Needs Flask: shown only.", run=False)
def flask_hello():
    """A minimal Flask app"""
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello!"


if __name__ == "__main__":
    main(sys.argv[1:])
