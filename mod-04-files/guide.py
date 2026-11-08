"""Teacher's guide for module 04: Files.

Every example and every exercise answer from this module's lessons, ready to
show in class. Each item prints its own code and then runs it.

Usage (from this folder):
    uv run guide.py                  list sections and items
    uv run guide.py files            run every item in a section
    uv run guide.py files.ex03       run one item
    uv run guide.py all              run everything
"""

# The lessons write open(name, "r") on purpose, to make the mode visible.
# ruff: noqa: UP015

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
# files.md


@item("files", "name_is_string", "A file name is only text. Nothing is opened or created.")
def name_is_string():
    """A file name is just a string"""
    file_name = "shopping.txt"
    print(file_name)
    print(type(file_name))


@item("files", "write_w", "Read the with line slowly: open, mode, encoding, as file, block.")
def write_w():
    """Creating a file with open and mode 'w'"""
    with scratch_folder():
        with open("shopping.txt", "w", encoding="utf-8") as file:
            file.write("milk\n")
            file.write("eggs\n")
            file.write("bread\n")

        print("Saved!")


@item("files", "read_whole", "read() returns the whole file as ONE string. Point at the ().")
def read_whole():
    """Reading the whole file with read()"""
    with scratch_folder():
        with open("shopping.txt", "w", encoding="utf-8") as file:
            file.write("milk\n")
            file.write("eggs\n")

        with open("shopping.txt", "r", encoding="utf-8") as file:
            content = file.read()

        print(content)


@item("files", "print_file_object", "Opening is not reading: the notebook is open, nobody read it.")
def print_file_object():
    """Opening is not reading: printing the file object"""
    with scratch_folder():
        with open("shopping.txt", "w", encoding="utf-8") as file:
            file.write("milk\n")

        with open("shopping.txt", "r", encoding="utf-8") as file:
            print(file)


@item("files", "read_without_parens", "The number at the end changes every run. read vs read().")
def read_without_parens():
    """Forgetting the parentheses: file.read is the method itself"""
    with scratch_folder():
        with open("shopping.txt", "w", encoding="utf-8") as file:
            file.write("milk\n")

        with open("shopping.txt", "r", encoding="utf-8") as file:
            print(file.read)


@item("files", "no_newline", "Ask her to predict before running. write() adds no line break.")
def no_newline():
    """Why "\\n" matters: words glued together"""
    with scratch_folder():
        with open("colors.txt", "w", encoding="utf-8") as file:
            file.write("red")
            file.write("green")
            file.write("blue")

        with open("colors.txt", "r", encoding="utf-8") as file:
            print(file.read())


@item("files", "with_newline", "Same program with \\n at the end of each line.")
def with_newline():
    """Adding "\\n" puts each word on its own line"""
    with scratch_folder():
        with open("colors.txt", "w", encoding="utf-8") as file:
            file.write("red\n")
            file.write("green\n")
            file.write("blue\n")

        with open("colors.txt", "r", encoding="utf-8") as file:
            print(file.read())


@item("files", "append", "Mode a keeps what is there and adds to the end.")
def append():
    """Adding without erasing: mode 'a'"""
    with scratch_folder():
        with open("diary.txt", "w", encoding="utf-8") as file:
            file.write("Monday: rain\n")

        with open("diary.txt", "a", encoding="utf-8") as file:
            file.write("Tuesday: sun\n")

        with open("diary.txt", "a", encoding="utf-8") as file:
            file.write("Wednesday: wind\n")

        with open("diary.txt", "r", encoding="utf-8") as file:
            print(file.read())


@item("files", "w_erases", "Ask her to predict before running. Monday and Tuesday disappear.")
def w_erases():
    """Mode 'w' erases first, then writes"""
    with scratch_folder():
        with open("diary.txt", "w", encoding="utf-8") as file:
            file.write("Monday: rain\n")
            file.write("Tuesday: sun\n")

        with open("diary.txt", "w", encoding="utf-8") as file:
            file.write("Wednesday: wind\n")

        with open("diary.txt", "r", encoding="utf-8") as file:
            print(file.read())


@item("files", "splitlines", "A clean list of lines, without \\n. The beginner's best choice.")
def splitlines():
    """Reading line by line with read().splitlines()"""
    with scratch_folder():
        with open("shopping.txt", "w", encoding="utf-8") as file:
            file.write("milk\neggs\nbread\n")

        with open("shopping.txt", "r", encoding="utf-8") as file:
            lines = file.read().splitlines()

        print(lines)


@item("files", "readlines", "Compare with splitlines: here every line keeps its \\n.")
def readlines():
    """readlines() keeps the "\\n" at the end of each line"""
    with scratch_folder():
        with open("shopping.txt", "w", encoding="utf-8") as file:
            file.write("milk\neggs\nbread\n")

        with open("shopping.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        print(lines)


@item("files", "for_lines", "Ask what happens without .strip() (an empty line after each item).")
def for_lines():
    """A for loop directly on the file, with .strip()"""
    with scratch_folder():
        with open("shopping.txt", "w", encoding="utf-8") as file:
            file.write("milk\neggs\nbread\n")

        with open("shopping.txt", "r", encoding="utf-8") as file:
            for line in file:
                print("-", line.strip())


@item("files", "numbered", "Once it is a list, everything about lists works: enumerate, len.")
def numbered():
    """A numbered list read from a file"""
    with scratch_folder():
        with open("shopping.txt", "w", encoding="utf-8") as file:
            file.write("milk\neggs\nbread\n")

        with open("shopping.txt", "r", encoding="utf-8") as file:
            items = file.read().splitlines()

        for number, item in enumerate(items, start=1):
            print(f"{number}. {item}")

        print(f"Total: {len(items)} items")


@item(
    "files", "functions", "The file name is a parameter, so the same function works for any file."
)
def functions():
    """Functions that use files"""
    with scratch_folder():

        def write_line(file_name, text):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(text + "\n")

        def read_lines(file_name):
            with open(file_name, "r", encoding="utf-8") as file:
                return file.read().splitlines()

        write_line("movies.txt", "Spirited Away")
        write_line("movies.txt", "Amélie")
        print(read_lines("movies.txt"))


@item("files", "missing_file", "Mode r needs the file to exist. Read the error message together.")
def missing_file():
    """When the file does not exist: FileNotFoundError"""
    with scratch_folder():
        with open("recipes.txt", "r", encoding="utf-8") as file:
            print(file.read())


@item(
    "files", "create_then_read", "Opening with a first creates the file without erasing anything."
)
def create_then_read():
    """Creating the file with "a" before reading it"""
    with scratch_folder():
        with open("recipes.txt", "a", encoding="utf-8") as file:
            file.write("")

        with open("recipes.txt", "r", encoding="utf-8") as file:
            print(repr(file.read()))


@item("files", "relative_paths", "Show it live in the terminal with pwd and ls.", run=False)
def relative_paths():
    """Where is the file? Relative paths"""
    # The file is created in the folder where the TERMINAL is, not where the .py is.
    #
    # PS C:\Users\you\Projects> python lists\shopping.py
    #   -> shopping.txt is created in Projects
    #
    # PS C:\Users\you\Projects> cd lists
    # PS C:\Users\you\Projects\lists> python shopping.py
    #   -> shopping.txt is created in Projects\lists
    #
    # Check with: pwd (where am I?) and ls (was the file created here?)
    pass


@item("files", "mistake_read_parens", "No error, but no text either. Fix: file.read()")
def mistake_read_parens():
    """Common mistake: forgetting the parentheses on read"""
    with scratch_folder():
        with open("shopping.txt", "w", encoding="utf-8") as file:
            file.write("milk\n")
        with open("shopping.txt", "r", encoding="utf-8") as file:
            content = file.read
        print(content)


@item("files", "mistake_w_vs_a", "No error message, which makes it sneaky. Simulates 3 runs.")
def mistake_w_vs_a():
    """Common mistake: using 'w' when you meant 'a'"""
    with scratch_folder():
        for note in ["buy milk", "call grandma", "pay rent"]:
            with open("notes.txt", "w", encoding="utf-8") as file:
                file.write(note + "\n")

        with open("notes.txt", "r", encoding="utf-8") as file:
            print(file.read())


@item("files", "mistake_glued", 'Fix: file.write(note + "\\n")')
def mistake_glued():
    """Common mistake: lines glued together"""
    with scratch_folder():
        with open("notes.txt", "a", encoding="utf-8") as file:
            for note in ["buy milk", "call grandma", "pay rent"]:
                file.write(note)

        with open("notes.txt", "r", encoding="utf-8") as file:
            print(file.read())


@item("files", "mistake_missing_file", "Ask: never created? Spelled differently? Wrong folder?")
def mistake_missing_file():
    """Common mistake: reading a file that does not exist"""
    with scratch_folder():
        with open("notes.txt", "r", encoding="utf-8") as file:
            print(file.read())


@item("files", "mistake_closed_file", "After the with block, the notebook is back in the drawer.")
def mistake_closed_file():
    """Common mistake: using a file outside the with block"""
    with scratch_folder():
        with open("shopping.txt", "w", encoding="utf-8") as file:
            file.write("milk\n")

        file.write("eggs\n")


@item("files", "mistake_write_number", 'write() only accepts strings. Fix: f"{42}\\n" or str(42).')
def mistake_write_number():
    """Common mistake: writing a number"""
    with scratch_folder():
        with open("scores.txt", "w", encoding="utf-8") as file:
            file.write(42)


@item("files", "ex01", "Predict the output. Ask her to predict before running.")
def files_ex01():
    """Exercise 1: write then read"""
    with scratch_folder():
        with open("pets.txt", "w", encoding="utf-8") as file:
            file.write("cat\n")
            file.write("dog\n")

        with open("pets.txt", "r", encoding="utf-8") as file:
            print(file.read())


@item("files", "ex02", "Predict the output. Ask her to predict before running. The cat is gone.")
def files_ex02():
    """Exercise 2: write twice"""
    with scratch_folder():
        with open("pets.txt", "w", encoding="utf-8") as file:
            file.write("cat\n")

        with open("pets.txt", "w", encoding="utf-8") as file:
            file.write("fish\n")

        with open("pets.txt", "r", encoding="utf-8") as file:
            print(file.read())


@item("files", "ex03", "Predict the output. Ask her to predict before running. lines[-1] is last.")
def files_ex03():
    """Exercise 3: append"""
    with scratch_folder():
        with open("pets.txt", "w", encoding="utf-8") as file:
            file.write("cat\n")

        with open("pets.txt", "a", encoding="utf-8") as file:
            file.write("fish\n")

        with open("pets.txt", "r", encoding="utf-8") as file:
            lines = file.read().splitlines()

        print(len(lines))
        print(lines[-1])


@item("files", "ex04", "Predict the output. Ask her to predict before running.")
def files_ex04():
    """Exercise 4: no line breaks"""
    with scratch_folder():
        with open("word.txt", "w", encoding="utf-8") as file:
            for letter in ["s", "u", "n"]:
                file.write(letter)

        with open("word.txt", "r", encoding="utf-8") as file:
            print(file.read())


@item("files", "ex05", "Fix the bug. The broken version used mode w; the fix is mode a.")
def files_ex05():
    """Exercise 5: the list that never grows (fixed)"""
    with scratch_folder():

        def add_book(title):
            with open("books.txt", "a", encoding="utf-8") as file:
                file.write(title + "\n")

        add_book("Dom Casmurro")
        add_book("The Hobbit")

        with open("books.txt", "r", encoding="utf-8") as file:
            print(file.read())


@item("files", "ex06", "Fix the bug. The broken version printed line without .strip().")
def files_ex06():
    """Exercise 6: empty lines everywhere (fixed)"""
    with scratch_folder():
        with open("shopping.txt", "w", encoding="utf-8") as file:
            file.write("rice\nbeans\n")

        with open("shopping.txt", "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())


@item("files", "ex07", "Fix the bug. The broken version printed file instead of file.read().")
def files_ex07():
    """Exercise 7: the text that never appears (fixed)"""
    with scratch_folder():
        with open("greeting.txt", "w", encoding="utf-8") as file:
            file.write("Good morning!\n")

        with open("greeting.txt", "r", encoding="utf-8") as file:
            print(file.read())


@item("files", "ex08", "Write it. Her foods will differ; check w + \\n, splitlines, enumerate.")
def files_ex08():
    """Exercise 8: your favorite foods"""
    with scratch_folder():
        with open("foods.txt", "w", encoding="utf-8") as file:
            file.write("feijoada\n")
            file.write("lasagna\n")
            file.write("açaí\n")

        with open("foods.txt", "r", encoding="utf-8") as file:
            foods = file.read().splitlines()

        for number, food in enumerate(foods, start=1):
            print(f"{number}. {food}")


@item("files", "ex09", "Write it. The for loop must be INSIDE the with block.")
def files_ex09():
    """Exercise 9: save a whole list"""
    with scratch_folder():

        def save_list(file_name, items):
            with open(file_name, "w", encoding="utf-8") as file:
                for item in items:
                    file.write(item + "\n")

        plants = ["fern", "cactus", "basil", "orchid"]
        save_list("plants.txt", plants)

        with open("plants.txt", "r", encoding="utf-8") as file:
            lines = file.read().splitlines()

        print(f"The file has {len(lines)} lines.")


@item("files", "ex10", "Write it. Counter at 0, then if word in line inside the for.")
def files_ex10():
    """Exercise 10: count matching lines"""
    with scratch_folder():

        def count_lines_with(file_name, word):
            with open(file_name, "r", encoding="utf-8") as file:
                lines = file.read().splitlines()
            count = 0
            for line in lines:
                if word in line:
                    count = count + 1
            return count

        with open("tasks.txt", "w", encoding="utf-8") as file:
            file.write("buy milk\n")
            file.write("call the bank\n")
            file.write("buy stamps\n")
            file.write("water the plants\n")

        print(count_lines_with("tasks.txt", "buy"))
        print(count_lines_with("tasks.txt", "plants"))


@item("files", "review01", "Review of module 01. Ask her to predict before running.")
def files_review01():
    """Review 1: f-strings"""
    item = "coffee"
    price = 12.5
    print(f"One {item} costs R$ {price}")


@item("files", "review02", "Review of module 03. Ask her to predict: what does it RETURN?")
def files_review02():
    """Review 2: return vs print"""

    def double(number):
        print("Calculating...")
        return number * 2

    result = double(4)
    print(result + 1)


@item("files", "review03", "Review of module 02. Only items with more than 4 letters.")
def files_review03():
    """Review 3: lists and for"""
    fruits = ["kiwi", "mango", "fig", "banana"]
    for fruit in fruits:
        if len(fruit) > 4:
            print(fruit)


# --------------------------------------------------------------------------
# project-notebook.md


@item("notebook", "setup", "Run these in the terminal before writing any code.", run=False)
def notebook_setup():
    """Creating the project folder"""
    # Windows (PowerShell):
    #   cd ~\Projects
    #   mkdir notes
    #   cd notes
    #   cursor .
    #
    # macOS or Linux: the same, with ~/Projects
    pass


@item("notebook", "step1", "A constant: CAPITALS mean set once, never changed. Opens nothing.")
def notebook_step1():
    """Step 1: a constant for the file name"""
    NOTES_FILE = "notes.txt"
    print(NOTES_FILE)


@item("notebook", "step2", "Parameters file_name and note. Mode a so the list grows. Then test.")
def notebook_step2():
    """Step 2: a function that saves one note"""
    with scratch_folder():

        def save_note(file_name, note):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(note + "\n")

        save_note("notes.txt", "buy coffee")
        save_note("notes.txt", "call the dentist")

        with open("notes.txt", "r", encoding="utf-8") as file:
            print(file.read())


@item("notebook", "step3", "The a-mode trick avoids FileNotFoundError. It RETURNS, never prints.")
def notebook_step3():
    """Step 3: a function that reads all notes"""
    with scratch_folder():

        def save_note(file_name, note):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(note + "\n")

        def read_notes(file_name):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write("")
            with open(file_name, "r", encoding="utf-8") as file:
                return file.read().splitlines()

        print(read_notes("notes.txt"))
        save_note("notes.txt", "buy coffee")
        print(read_notes("notes.txt"))


@item("notebook", "step4", "Receives a LIST, not a file name. It only shows.")
def notebook_step4():
    """Step 4: a function that shows the notes"""

    def show_notes(notes):
        print("Your notes:")
        for number, note in enumerate(notes, start=1):
            print(f"{number}. {note}")

    show_notes(["buy coffee", "call the dentist", "water the plants"])


@item("notebook", "step5", "input() is simulated here: the typed text is shown.")
def notebook_step5():
    """Step 5: a function that asks for a note"""

    def ask_note():
        return input("Write a note: ")

    with typed("buy coffee"):
        note = ask_note()
    print(repr(note))


@item("notebook", "step6", "Read main() aloud like a recipe. The last line is the CALL.")
def notebook_step6():
    """Step 6: main(), the head chef"""
    with scratch_folder():
        NOTES_FILE = "notes.txt"

        def save_note(file_name, note):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(note + "\n")

        def read_notes(file_name):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write("")
            with open(file_name, "r", encoding="utf-8") as file:
                return file.read().splitlines()

        def show_notes(notes):
            print("Your notes:")
            for number, note in enumerate(notes, start=1):
                print(f"{number}. {note}")

        def ask_note():
            return input("Write a note: ")

        def main():
            note = ask_note()
            save_note(NOTES_FILE, note)
            notes = read_notes(NOTES_FILE)
            show_notes(notes)

        with typed("buy coffee"):
            main()


@item("notebook", "complete", "Two runs in a row: the first note is still there on the second.")
def notebook_complete():
    """The complete program, run twice"""
    with scratch_folder():
        NOTES_FILE = "notes.txt"

        def save_note(file_name, note):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(note + "\n")

        def read_notes(file_name):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write("")
            with open(file_name, "r", encoding="utf-8") as file:
                return file.read().splitlines()

        def show_notes(notes):
            print("Your notes:")
            for number, note in enumerate(notes, start=1):
                print(f"{number}. {note}")

        def ask_note():
            return input("Write a note: ")

        def main():
            note = ask_note()
            save_note(NOTES_FILE, note)
            notes = read_notes(NOTES_FILE)
            show_notes(notes)

        print("> python notes.py")
        with typed("buy coffee"):
            main()
        print("> python notes.py")
        with typed("call the dentist"):
            main()


@item("notebook", "param_vs_argument", "file_name is a PARAMETER; NOTES_FILE is the ARGUMENT.")
def notebook_param_vs_argument():
    """Parameter or global? file_name and NOTES_FILE"""
    NOTES_FILE = "notes.txt"

    def save_note(file_name, note):
        print(f"Inside the function, file_name is {file_name!r} and note is {note!r}")

    save_note(NOTES_FILE, "buy coffee")


@item("notebook", "mistake_never_called", "Nothing happens, no error. Fix: add main() at the end.")
def notebook_mistake_never_called():
    """Common mistake: defining but never calling main()"""

    def main():
        print("This never runs")

    print("(the program ends here: main was defined, never called)")


@item(
    "notebook", "mistake_call_before_define", "In a real file Python also adds: Did you mean min?"
)
def notebook_mistake_call_before_define():
    """Common mistake: calling a function before it is defined"""
    program = "main()\n\n\ndef main():\n    print('Hello')\n"
    print(program)
    exec(program, {})


@item("notebook", "mistake_print_not_return", "A function without return gives back None.")
def notebook_mistake_print_not_return():
    """Common mistake: printing instead of returning"""

    def show_notes(notes):
        for number, note in enumerate(notes, start=1):
            print(f"{number}. {note}")

    show_notes(None)


@item(
    "notebook", "ex01", "Predict the output. Ask her to predict before running. notes[0] is first."
)
def notebook_ex01():
    """Exercise 1: what gets saved?"""
    with scratch_folder():

        def save_note(file_name, note):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(note + "\n")

        def read_notes(file_name):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write("")
            with open(file_name, "r", encoding="utf-8") as file:
                return file.read().splitlines()

        save_note("notes.txt", "pay rent")
        save_note("notes.txt", "buy bread")
        notes = read_notes("notes.txt")
        print(len(notes))
        print(notes[0])


@item("notebook", "ex02", "Fix the bug. One character: w erases every time; change back to a.")
def notebook_ex02():
    """Exercise 2: the notebook with amnesia (broken, then fixed)"""
    with scratch_folder():

        def save_note_broken(file_name, note):
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(note + "\n")

        def save_note(file_name, note):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(note + "\n")

        save_note_broken("broken.txt", "pay rent")
        save_note_broken("broken.txt", "buy bread")
        save_note("fixed.txt", "pay rent")
        save_note("fixed.txt", "buy bread")
        with open("broken.txt", encoding="utf-8") as file:
            print("with w:", file.read().splitlines())
        with open("fixed.txt", encoding="utf-8") as file:
            print("with a:", file.read().splitlines())


@item("notebook", "ex03", "Write it. The len line goes AFTER the loop, not inside it.")
def notebook_ex03():
    """Exercise 3: show the count"""

    def show_notes(notes):
        print("Your notes:")
        for number, note in enumerate(notes, start=1):
            print(f"{number}. {note}")
        print(f"You have {len(notes)} notes.")

    show_notes(["buy coffee", "call the dentist"])


@item("notebook", "ex04", "Write it. The decision lives in main(); save_note stays simple.")
def notebook_ex04():
    """Exercise 4: ignore empty notes"""
    with scratch_folder():
        NOTES_FILE = "notes.txt"

        def save_note(file_name, note):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(note + "\n")

        def read_notes(file_name):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write("")
            with open(file_name, "r", encoding="utf-8") as file:
                return file.read().splitlines()

        def show_notes(notes):
            print("Your notes:")
            for number, note in enumerate(notes, start=1):
                print(f"{number}. {note}")

        def ask_note():
            return input("Write a note: ")

        def main():
            note = ask_note()
            if note.strip() == "":
                print("Empty note, nothing saved.")
            else:
                save_note(NOTES_FILE, note)
            notes = read_notes(NOTES_FILE)
            show_notes(notes)

        with typed("buy coffee"):
            main()
        with typed("   "):
            main()


@item(
    "notebook", "ex05", "Challenge. while True + break; input returns a string, compare with '1'."
)
def notebook_ex05():
    """Exercise 5: a menu that keeps going"""
    with scratch_folder():
        NOTES_FILE = "notes.txt"

        def save_note(file_name, note):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(note + "\n")

        def read_notes(file_name):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write("")
            with open(file_name, "r", encoding="utf-8") as file:
                return file.read().splitlines()

        def show_notes(notes):
            print("Your notes:")
            for number, note in enumerate(notes, start=1):
                print(f"{number}. {note}")

        def ask_note():
            return input("Write a note: ")

        def show_menu():
            print("1) Add a note")
            print("2) Show notes")
            print("0) Exit")

        def main():
            while True:
                show_menu()
                choice = input("Choose: ")
                if choice == "0":
                    print("Bye!")
                    break
                elif choice == "1":
                    note = ask_note()
                    save_note(NOTES_FILE, note)
                elif choice == "2":
                    show_notes(read_notes(NOTES_FILE))
                else:
                    print("Unknown option, try again.")

        with typed("1", "buy coffee", "2", "0"):
            main()


@item("notebook", "review01", "Review of module 03. Parameters in the def, arguments in the call.")
def notebook_review01():
    """Review 1: parameter or argument?"""

    def greet(name, time_of_day):
        print(f"Good {time_of_day}, {name}!")

    greet("Ana", "evening")


@item("notebook", "review02", "Review of module 01. Ask which line crashes before running.")
def notebook_review02():
    """Review 2: concatenation vs interpolation"""
    count = 3
    print(f"You have {count} notes")
    print("You have " + str(count) + " notes")
    print("You have " + count + " notes")


if __name__ == "__main__":
    main(sys.argv[1:])
