"""Teacher's guide for module 01: Building blocks.

Every example and every exercise answer from this module's lessons, ready to
show in class. Each item prints its own code and then runs it.

Usage (from this folder):
    uv run guide.py                  list sections and items
    uv run guide.py practice         run every item in a section
    uv run guide.py practice.ex07    run one item
    uv run guide.py all              run everything
"""

# The lessons teach type(...) and open(file, "r") on purpose, so keep them as written.
# ruff: noqa: UP003, UP015

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


# ===== data-types.md


@item("data-types", "create", "Read = from right to left: store 3 under the name cups.")
def dt_create():
    """Creating a variable"""
    cups = 3
    print(cups)


@item("data-types", "calculate", "Python calculates the right side first, then stores it.")
def dt_calculate():
    """Using variables in calculations"""
    price = 12
    quantity = 3
    total = price * quantity
    print(total)


@item("data-types", "reassign", "Ask what c is before running: a is already 0.")
def dt_reassign():
    """Reassignment: the latest value wins"""
    a = 2
    a = 0
    b = 5
    c = a + b
    print(c)


@item("data-types", "own_old_value", "Read the second line from the right.")
def dt_own_old_value():
    """A variable using its own old value"""
    steps = 10
    steps = steps + 5
    print(steps)


@item("data-types", "case", "Two different variables.")
def dt_case():
    """Upper and lower case matter"""
    name = "Ana"
    Name = "Bia"
    print(name)
    print(Name)


@item("data-types", "types", "10, 10.0 and '10' look alike but are three types.")
def dt_types():
    """The basic types"""
    print(type(10))
    print(type(10.0))
    print(type("10"))
    print(type(True))


@item("data-types", "arithmetic", "/ always gives a float, even 6 / 2.")
def dt_arithmetic():
    """Arithmetic"""
    print(7 + 2)
    print(7 * 2)
    print(7 / 2)
    print(6 / 2)


@item("data-types", "type_hint", "The hint is a note, not a lock.")
def dt_type_hint():
    """Type hints do not force a type"""
    a: int = 10
    print(a)
    a = "ten"
    print(a)


@item("data-types", "convert", "int('42') is a number; str(7) is text.")
def dt_convert():
    """Converting between types"""
    print(int("42") + 1)
    print(float("2.5") * 2)
    print(str(7) + "7")
    print(int(3.9))


@item("data-types", "mistake_before", "Top to bottom: total does not exist yet.")
def dt_mistake_before():
    """Using a variable before creating it"""
    run_source("print(total)\ntotal = 10")


@item("data-types", "mistake_case", "In a terminal Python adds: Did you mean: 'city'?")
def dt_mistake_case():
    """Wrong upper or lower case"""
    city = "Lisbon"  # noqa: F841
    print(City)  # noqa: F821


@item("data-types", "mistake_int_text", "ValueError: right type, wrong content.")
def dt_mistake_int_text():
    """Turning text that is not a number into a number"""
    age = int("thirty")  # noqa: F841


@item("data-types", "mistake_quotes", "No crash, which makes it sneaky.")
def dt_mistake_quotes():
    """Forgetting that quotes make text"""
    a = "5"
    b = "3"
    print(a + b)


@item("data-types", "ex01", "Ask her to predict before running.")
def dt_ex01():
    """Exercise 1: Last one wins"""
    coffee = 1
    coffee = 2
    coffee = 3
    print(coffee)


@item("data-types", "ex02", "Ask her to predict before running. y does not change later.")
def dt_ex02():
    """Exercise 2: Order matters"""
    x = 4
    y = x + 1
    x = 10  # noqa: F841
    print(y)


@item("data-types", "ex03", "Ask her to predict before running.")
def dt_ex03():
    """Exercise 3: What type is it?"""
    print(type(3))
    print(type("3"))
    print(type(3.0))
    print(type(False))


@item("data-types", "ex04", "Ask her to predict before running.")
def dt_ex04():
    """Exercise 4: Division"""
    print(10 / 2)
    print(10 / 4)


@item("data-types", "ex05", "height must exist before the line that uses it.")
def dt_ex05():
    """Exercise 5: The missing variable (fixed)"""
    width = 5
    height = 5
    area = width * height
    print(area)


@item("data-types", "ex06", "Without quotes they are numbers. Or int(bags) + int(extra).")
def dt_ex06():
    """Exercise 6: Text that should be a number (fixed)"""
    bags = 10
    extra = 5
    print(bags + extra)


@item("data-types", "ex07", "Good names: slices_per_pizza, not x.")
def dt_ex07():
    """Exercise 7: Pizza for everyone"""
    slices_per_pizza = 8
    pizzas = 3
    total_slices = slices_per_pizza * pizzas
    print(total_slices)


@item("data-types", "ex08", "The pattern savings = savings + 25.")
def dt_ex08():
    """Exercise 8: Saving money"""
    savings = 100
    savings = savings + 25
    savings = savings + 25
    savings = savings + 25
    print(savings)


@item("data-types", "ex09", "int() turns the text into a number before the math.")
def dt_ex09():
    """Exercise 9: From text to number"""
    typed = "1990"
    year = int(typed)
    age = 2026 - year
    print(age)


# ===== strings.md


@item("strings", "quotes", "Single or double, just be consistent.")
def st_quotes():
    """Quotes"""
    print("Hello")
    print('Hello')  # fmt: skip


@item("strings", "newline", "\\n is one invisible character: a line break.")
def st_newline():
    """New lines with \\n"""
    print("First line\nSecond line")


@item("strings", "concat", "+ does not add the space for you.")
def st_concat():
    """Joining strings with +"""
    first = "Maria"
    last = "Silva"
    print(first + " " + last)


@item("strings", "concat_error", "Ask her to predict the error before running.")
def st_concat_error():
    """+ only joins text with text"""
    cups = 2
    print("Cups: " + cups)


@item("strings", "concat_str", "Convert the number to text first.")
def st_concat_str():
    """Fixing it with str()"""
    cups = 2
    print("Cups: " + str(cups))


@item("strings", "fstring", "No str() needed: the f-string converts for you.")
def st_fstring():
    """f-strings: filling in the blanks"""
    name = "Maria"
    cups = 2
    print(f"{name} ordered {cups} cups.")


@item("strings", "expressions", "Anything inside {} is calculated first.")
def st_expressions():
    """Calculations and function calls inside {}"""
    price = 4.5
    cups = 2
    print(f"Total: {price * cups}")
    print(f"One plus one is {1 + 1}")
    print(f"The word 'coffee' has {len('coffee')} letters")


@item("strings", "no_f", "Without the f the braces are just characters.")
def st_no_f():
    """What happens without the f"""
    name = "Maria"
    print("Hello, {name}")
    print(f"Hello, {name}")


@item("strings", "sep_end", "sep goes between values; end goes after everything.")
def st_sep_end():
    """print with several values, sep and end"""
    print("Total:", 9, "reais")
    print("apple", "banana", "pear", sep=", ")
    print("apple", "banana", "pear", sep="\n")
    print("Loading", end="...")
    print("done")


@item("strings", "len", "Spaces count too.")
def st_len():
    """How long is a string?"""
    print(len("tea"))
    print(len("green tea"))


@item("strings", "for_letters", "Loops get a full lesson in module 02.")
def st_for_letters():
    """Going through each character"""
    for letter in "tea":
        print(letter)


@item("strings", "mistake_text_number", "Two fixes: str(age) or an f-string.")
def st_mistake_text_number():
    """Joining text and a number with +"""
    age = 30
    print("I am " + age + " years old")


@item("strings", "mistake_no_f", "No error, just the wrong text.")
def st_mistake_no_f():
    """Forgetting the f"""
    city = "Porto"  # noqa: F841
    print("I live in {city}")


@item("strings", "mistake_quotes", "Opened with \" and tried to close with '.")
def st_mistake_quotes():
    """Quotes that do not match"""
    run_source("print(\"Hello')")


@item("strings", "mistake_spaces", "Fix: first + ' ' + last, or an f-string.")
def st_mistake_spaces():
    """Missing spaces when joining"""
    first = "Ana"
    last = "Costa"
    print(first + last)


@item("strings", "ex01", "Ask her to predict before running.")
def st_ex01():
    """Exercise 1: With and without f"""
    food = "soup"
    print("I like {food}")
    print(f"I like {food}")


@item("strings", "ex02", "Ask her to predict before running. Both are text.")
def st_ex02():
    """Exercise 2: Joining text"""
    a = "5"
    b = "5"
    print(a + b)
    print(f"{a}{b}")


@item("strings", "ex03", "Ask her to predict before running.")
def st_ex03():
    """Exercise 3: Separators"""
    print("a", "b", "c")
    print("a", "b", "c", sep="-")
    print("a", "b", "c", sep="")


@item("strings", "ex04", "Ask her to predict before running. Only inside {} is math.")
def st_ex04():
    """Exercise 4: Math inside braces"""
    apples = 3
    print(f"{apples} apples")
    print(f"{apples * 2} apples")
    print(f"{apples} * 2 apples")


@item("strings", "ex05", "Two fixes: str() and an f-string.")
def st_ex05():
    """Exercise 5: The broken receipt (fixed)"""
    total = 18
    print("Total: " + str(total) + " reais")
    print(f"Total: {total} reais")


@item("strings", "ex06", "Or: f'{greeting} {time} {name}'.")
def st_ex06():
    """Exercise 6: Glued words (fixed)"""
    greeting = "Good"
    time = "morning,"
    name = "Ana"
    print(greeting + " " + time + " " + name)


@item("strings", "ex07", "One f-string with three variables.")
def st_ex07():
    """Exercise 7: Coffee order"""
    customer = "Lucas"
    drink = "latte"
    price = 9.5
    print(f"{customer} ordered a {drink} for {price} reais.")


@item("strings", "ex08", "Another way: print('Milk', 'Eggs', 'Bread', sep='\\n').")
def st_ex08():
    """Exercise 8: Three lines, one print"""
    print("Milk\nEggs\nBread")


@item("strings", "ex09", "A function call inside the braces.")
def st_ex09():
    """Exercise 9: Word length"""
    word = "pineapple"
    print(f"{word} has {len(word)} letters")


@item("strings", "review01", "Review of data-types. The type belongs to the value.")
def st_review01():
    """Review 1: Which type?"""
    value = "12"
    print(type(value))
    value = 12
    print(type(value))


@item("strings", "review02", "Review of data-types.")
def st_review02():
    """Review 2: Total price"""
    price = 3
    quantity = 4
    total = price * quantity
    print(f"Total: {total}")


# ===== built-in.md


@item("built-in", "inside_out", "Inside out: len first, then print.")
def bi_inside_out():
    """Calling a function: name plus parentheses"""
    print(len("coffee"))


@item("built-in", "name_vs_call", "This is her read vs read() confusion from class.")
def bi_name_vs_call():
    """The name alone is not a call"""
    print(len)
    print(len("tea"))


@item("built-in", "method_vs_call", "The 0x... address changes every run.")
def bi_method_vs_call():
    """Methods: upper vs upper()"""
    word = "tea"
    print(word.upper)
    print(word.upper())


@item("built-in", "print_many", "Commas put a space between values.")
def bi_print_many():
    """print()"""
    print("Pears:", 4, "Price:", 2.5)


@item("built-in", "input_text", "input() always gives back text, even digits.")
def bi_input_text():
    """input() always gives back text"""
    with typed("30"):
        age = input("How old are you? ")
        print(type(age))


@item("built-in", "input_int", "input() runs first, then int().")
def bi_input_int():
    """Converting what input() returned"""
    with typed("30"):
        age = int(input("How old are you? "))
        print(f"Next year you will be {age + 1}")


@item("built-in", "len", "Characters in a string, items in a list.")
def bi_len():
    """len()"""
    print(len("Lisbon"))
    print(len(["milk", "eggs", "bread"]))
    print(len(""))


@item("built-in", "conversions", "A quick reminder of data-types.")
def bi_conversions():
    """type(), int(), float(), str()"""
    print(type(2.5))
    print(int("8") + 2)
    print(float("1.5") + 1)
    print(str(8) + "2")


@item("built-in", "round", "The second argument is the number of decimal places.")
def bi_round():
    """round()"""
    print(round(3.7))
    print(round(3.14159, 2))
    print(round(9.876, 1))


@item("built-in", "enumerate", "Positions start at 0; start=1 is for people.")
def bi_enumerate():
    """enumerate(): numbering items in a loop"""
    groceries = ["milk", "eggs", "bread"]
    for position, item_name in enumerate(groceries):
        print(position, item_name)
    for number, item_name in enumerate(groceries, start=1):
        print(f"{number}. {item_name}")


@item("built-in", "keyword_name", "Keywords are grammar: they cannot be names.")
def bi_keyword_name():
    """A keyword used as a name"""
    run_source("return = 5")


@item("built-in", "shadow_str", "str now points to text, not to the tool.")
def bi_shadow_str():
    """Reusing a built-in name"""
    str = "hello"
    print(str(5))


@item("built-in", "mistake_parentheses", "A strange <built-in ...>? Check the ().")
def bi_mistake_parentheses():
    """Forgetting the parentheses"""
    name = "ana"
    print(name.upper)


@item("built-in", "mistake_input_math", "Text times 2 repeats the text.")
def bi_mistake_input_math():
    """Doing math with what input() returned"""
    with typed("3"):
        cups = input("How many cups? ")
        print(cups * 2)


@item("built-in", "mistake_not_callable", "Only functions can be called with ().")
def bi_mistake_not_callable():
    """Calling something that is not a function"""
    total = 10
    print(total())


@item("built-in", "mistake_len_name", "Pick another name: size or length.")
def bi_mistake_len_name():
    """Using a variable called len"""
    len = 3
    print(len("abc"))


@item("built-in", "ex01", "Ask her to predict before running.")
def bi_ex01():
    """Exercise 1: Inside out"""
    print(len("bread") + 1)


@item("built-in", "ex02", "Ask her to predict before running. Name vs call.")
def bi_ex02():
    """Exercise 2: Name or call?"""
    print(type)
    print(type(7))


@item("built-in", "ex03", "Ask her to predict before running.")
def bi_ex03():
    """Exercise 3: Rounding"""
    print(round(2.71828, 2))
    print(round(7.6))


@item("built-in", "ex04", "Ask her to predict before running.")
def bi_ex04():
    """Exercise 4: Counting from 1"""
    colors = ["red", "blue"]
    for n, color in enumerate(colors, start=1):
        print(n, color)


@item("built-in", "ex05", "Hint: input() always returns text.")
def bi_ex05():
    """Exercise 5: The doubled order (fixed)"""
    with typed("4"):
        plates = int(input("How many plates? "))
        print(plates * 2)


@item("built-in", "ex06", "list was a built-in name; rename the variable.")
def bi_ex06():
    """Exercise 6: The broken name (fixed)"""
    drinks = ["tea", "coffee"]
    print(len(drinks))
    items = list("abc")
    print(items)


@item("built-in", "ex07", "len() inside the f-string.")
def bi_ex07():
    """Exercise 7: Name length"""
    with typed("Carla"):
        name = input("What is your name? ")
        print(f"{name} has {len(name)} letters")


@item("built-in", "ex08", "float for money, int for people, round(value, 2).")
def bi_ex08():
    """Exercise 8: Splitting the bill"""
    with typed("100", "3"):
        total = float(input("Bill total? "))
        people = int(input("How many people? "))
        each = total / people
        print(f"Each person pays {round(each, 2)}")


@item("built-in", "ex09", "enumerate with start=1.")
def bi_ex09():
    """Exercise 9: Numbered to-do list"""
    tasks = ["water the plants", "call mom", "buy coffee"]
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


@item("built-in", "review01", "Review of strings: str() or an f-string.")
def bi_review01():
    """Review 1: Text plus number (fixed)"""
    print("Items: " + str(3))
    print(f"Items: {3}")


@item("built-in", "review02", "Ask her to predict. b kept the old value of a.")
def bi_review02():
    """Review 2: Predict the output"""
    a = 1
    b = a
    a = 5
    print(f"{a} {b}")


# ===== practice.md (the practice set for classes 1 to 3)


@item("practice", "ex01", "Ask her to predict before running.")
def pr_ex01():
    """Exercise 1: Fill the blank"""
    plant = "basil"
    print(f"I water the {plant} every day.")


@item("practice", "ex02", "Ask her to predict before running. Where is the f?")
def pr_ex02():
    """Exercise 2: Where is the f?"""
    book = "Dom Casmurro"
    print("Reading {book}")
    print(f"Reading {book}")


@item("practice", "ex03", "Ask her to predict before running. Only inside {} is math.")
def pr_ex03():
    """Exercise 3: Math in the braces"""
    price = 5
    print(f"Two coffees cost {price * 2} reais")
    print(f"Two coffees cost {price} * 2 reais")


@item("practice", "ex04", "The f-string removes the need for str().")
def pr_ex04():
    """Exercise 4: From + to f-string"""
    messages = 3
    print(f"You have {messages} new messages")


@item("practice", "ex05", "Her data will differ; check it is ONE f-string.")
def pr_ex05():
    """Exercise 5: A short introduction"""
    name = "Ana"
    city = "Lisbon"
    age = 39
    print(f"My name is {name}, I live in {city} and I am {age} years old.")


@item("practice", "ex06", "Ask her to predict. Defined is not called: no Hello!.")
def pr_ex06():
    """Exercise 6: Defined but never called"""

    def say_hello():
        print("Hello!")

    print("Start")
    print("End")


@item("practice", "ex07", "Ask her to predict. Each call runs the recipe once.")
def pr_ex07():
    """Exercise 7: Called twice"""

    def say_hello():
        print("Hello!")

    print("Start")
    say_hello()
    say_hello()
    print("End")


@item("practice", "ex08", "Ask her to predict. person is the parameter; 'Marta' the argument.")
def pr_ex08():
    """Exercise 8: Parameter and argument"""

    def greet(person):
        print(f"Good evening, {person}")

    greet("Marta")
    greet("Joel")


@item("practice", "ex09", "Ask her to predict. A file name is just text; nothing is opened.")
def pr_ex09():
    """Exercise 9: Outside name, inside name"""

    def show_file_name(name):
        print(f"File: {name}")

    file_name = "notes.txt"
    show_file_name(file_name)


@item("practice", "ex10", "Ask her to predict. Only two 8s: the lone return shows nothing.")
def pr_ex10():
    """Exercise 10: return versus print"""

    def double_print(n):
        print(n * 2)

    def double_return(n):
        return n * 2

    double_print(4)
    double_return(4)
    result = double_return(4)
    print(result)


@item("practice", "ex11", "Defined once, called three times.")
def pr_ex11():
    """Exercise 11: Your first function"""

    def welcome(name):
        print(f"Welcome, {name}!")

    welcome("Ana")
    welcome("Rui")
    welcome("Lia")


@item("practice", "ex12", "return inside, print outside.")
def pr_ex12():
    """Exercise 12: A function that returns"""

    def total_price(price, quantity):
        return price * quantity

    total = total_price(5, 3)
    print(f"Total: {total}")


@item("practice", "ex13_before", "Ask why None appears: no return means None.")
def pr_ex13_before():
    """Exercise 13 (before): the function only prints"""

    def make_greeting(name):
        print(f"Hi, {name}!")

    message = make_greeting("Bia")
    print(message)


@item("practice", "ex13", "Now the text is handed back and stored.")
def pr_ex13():
    """Exercise 13: From print to return (fixed)"""

    def make_greeting(name):
        return f"Hi, {name}!"

    message = make_greeting("Bia")
    print(message)


@item("practice", "ex14", "Ask her to predict. The third item is at position 2.")
def pr_ex14():
    """Exercise 14: Counting starts at 0"""
    fruits = ["apple", "banana", "grape"]
    print(fruits[0])
    print(fruits[2])


@item("practice", "ex15", "Ask her to predict. append adds at the end.")
def pr_ex15():
    """Exercise 15: How many?"""
    fruits = ["apple", "banana", "grape"]
    fruits.append("mango")
    print(len(fruits))
    print(fruits)


@item("practice", "ex16_before", "3 items live at 0, 1 and 2. There is no 3.")
def pr_ex16_before():
    """Exercise 16 (before): out of range"""
    days = ["mon", "tue", "wed"]
    print(days[3])


@item("practice", "ex16", "The last item is at len - 1.")
def pr_ex16():
    """Exercise 16: Out of range (fixed)"""
    days = ["mon", "tue", "wed"]
    print(days[2])


@item("practice", "ex17", "Start empty, append three times.")
def pr_ex17():
    """Exercise 17: Build a list"""
    shopping = []
    shopping.append("rice")
    shopping.append("beans")
    shopping.append("coffee")
    print(shopping)
    print(len(shopping))


@item("practice", "ex18", "Ask her to predict. pet holds the next item each turn.")
def pr_ex18():
    """Exercise 18: One item per turn"""
    pets = ["cat", "dog", "fish"]
    for pet in pets:
        print(f"I have a {pet}")


@item("practice", "ex19", "Ask her to predict. done is outside the loop.")
def pr_ex19():
    """Exercise 19: What is inside the loop?"""
    for pet in ["cat", "dog"]:
        print(pet)
    print("done")


@item("practice", "ex20", "Ask her to predict. Same list, two starting numbers.")
def pr_ex20():
    """Exercise 20: enumerate from 0 and from 1"""
    songs = ["intro", "chorus"]
    for i, song in enumerate(songs):
        print(i, song)
    for i, song in enumerate(songs, start=1):
        print(i, song)


@item("practice", "ex21", "A string is a sequence of letters.")
def pr_ex21():
    """Exercise 21: Looping over a word"""
    for letter in "python":
        print(letter)


@item("practice", "ex22", "total = 0 before the loop; print after it.")
def pr_ex22():
    """Exercise 22: Counting with a loop"""
    prices = [10, 25, 5, 40]
    total = 0
    for price in prices:
        total = total + price
    print(f"Total: {total}")


@item("practice", "ex23", "A loop inside a function, called with a list.")
def pr_ex23():
    """Exercise 23: Shopping list printer"""

    def print_list(items):
        for number, item_name in enumerate(items, start=1):
            print(f"{number}. {item_name}")

    print_list(["milk", "eggs", "bread"])


@item("practice", "ex24", "The function returns; the loop prints.")
def pr_ex24():
    """Exercise 24: Greetings for everyone"""

    def make_greeting(name):
        return f"Hello, {name}!"

    for person in ["Ana", "Rui", "Lia"]:
        print(make_greeting(person))


@item("practice", "ex25", "Two things per turn: print and add to total.")
def pr_ex25():
    """Exercise 25: Longest word"""
    words = ["sun", "ocean", "sky"]
    total = 0
    for word in words:
        print(f"{word}: {len(word)}")
        total = total + len(word)
    print(f"Total letters: {total}")


@item("practice", "ex26", "The first 2 lines only create the sample file. read() WITH ().")
def pr_ex26():
    """Exercise 26: Notes from a file"""
    with scratch_folder():
        with open("notes.txt", "w") as file:
            file.write("buy coffee\ncall the dentist\nwater the plants\n")

        with open("notes.txt", "r") as file:
            content = file.read()
        notes = content.splitlines()
        for number, note in enumerate(notes, start=1):
            print(f"{number}. {note}")


@item("practice", "ex27", "The last three lines tell the whole story: file, ask, add, show.")
def pr_ex27():
    """Exercise 27: Add a note, then show all"""
    with scratch_folder(), typed("pay the rent"):
        with open("notes.txt", "w") as file:
            file.write("buy coffee\ncall the dentist\nwater the plants\n")

        def add_note(file_name, note):
            with open(file_name, "a") as file:
                file.write(note + "\n")

        def show_notes(file_name):
            with open(file_name, "r") as file:
                notes = file.read().splitlines()
            for number, note in enumerate(notes, start=1):
                print(f"{number}. {note}")

        notes_file = "notes.txt"
        new_note = input("New note: ")
        add_note(notes_file, new_note)
        show_notes(notes_file)


if __name__ == "__main__":
    main(sys.argv[1:])
